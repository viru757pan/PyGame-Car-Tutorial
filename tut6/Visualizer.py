import pygame
from utils import lerp, getRGB


class Visualizer:
    @staticmethod
    def draw_network(screen, network):
        margin = 50
        top = margin
        left = margin
        width = screen.get_width() - margin * 2
        height = screen.get_height() - margin * 2

        levelHeight = height / len(network.levels)

        for i in range(len(network.levels)-1, -1, -1):
            levelTop = top + lerp((height - levelHeight), 0,
                                  (0.5 if len(network.levels) == 1 else i / (len(network.levels))))

            Visualizer.draw_level(
                screen, network.levels[i], left, levelTop, width, levelHeight, (['W', 'A', 'D', 'S'] if i == len(network.levels) - 1 else []))

    @staticmethod
    def draw_level(screen, level, left, top, width, height, output_labels):
        right = left + width
        bottom = top + height

        inputs = level.inputs
        outputs = level.outputs
        weights = level.weights
        biases = level.biases

        node_radius = 14

        for i in range(len(inputs)):
            for j in range(len(outputs)):
                start_x = Visualizer.get_node_x(inputs, i, left, right)
                start_y = bottom-137
                end_x = Visualizer.get_node_x(outputs, j, left, right)
                end_y = top

                # Draw dashed line
                rgb = getRGB(weights[i][j])
                pygame.draw.line(
                    screen, rgb, (start_x, start_y), (end_x, end_y), 2)

                # Full Black Circle
                pygame.draw.circle(screen, (0, 0, 0),
                                   (start_x, start_y), node_radius)
                pygame.draw.circle(screen, (0, 0, 0),
                                   (end_x, end_y), node_radius)

                # Outline Circle
                rgb2 = (128, 128, 128)
                pygame.draw.circle(screen, rgb2,
                                   (start_x, start_y), node_radius, 2)
                pygame.draw.circle(screen, rgb2,
                                   (end_x, end_y), node_radius, 2)

        for i in range(len(inputs)):
            x = Visualizer.get_node_x(inputs, i, left, right)
            y = bottom-137

            if inputs[i] is not None:
                rgb = getRGB(inputs[i])
            else:
                rgb = (128, 128, 128)
            pygame.draw.circle(screen, rgb,
                               (int(x), int(y)), node_radius*0.6, 14)

        for i in range(len(outputs)):
            x = Visualizer.get_node_x(outputs, i, left, right)
            y = top

            if outputs[i] is not None:
                rgb = getRGB(outputs[i])
            else:
                rgb = (128, 128, 128)
            pygame.draw.circle(screen, rgb,
                               (int(x), int(y)), node_radius*0.6, 14)

            if i < len(output_labels) and output_labels[i]:
                font = pygame.font.Font(None, int(node_radius * 1.3))
                text = font.render(output_labels[i], True, (0, 0, 0))
                text_rect = text.get_rect(
                    center=(int(x), int(top + node_radius * 0.1)))
                screen.blit(text, text_rect)

    @staticmethod
    def get_node_x(nodes, index, left, right):
        return lerp(left, right, (0.5 if len(nodes) == 1 else index / (len(nodes) - 1)))
