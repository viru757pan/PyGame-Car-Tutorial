import pygame
pygame.font.init()


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))


def lerp1(A, B, t):
    return {
        'x': A['x'] + (B['x'] - A['x']) * t,
        'y': A['y'] + (B['y'] - A['y']) * t
    }


def getIntersection(A, B, C, D):
    tTop = (D['x'] - C['x']) * (A['y'] - C['y']) - \
        (D['y'] - C['y']) * (A['x'] - C['x'])
    uTop = (C['y'] - A['y']) * (A['x'] - B['x']) - \
        (C['x'] - A['x']) * (A['y'] - B['y'])
    bottom = (D['y'] - C['y']) * (B['x'] - A['x']) - \
        (D['x'] - C['x']) * (B['y'] - A['y'])

    if bottom != 0:
        t = tTop / bottom
        u = uTop / bottom
        if 0 <= t <= 1 and 0 <= u <= 1:
            return {
                'x': lerp1(A, B, t)['x'],
                'y': lerp1(A, B, t)['y'],
                'offset': t
            }

    return None
