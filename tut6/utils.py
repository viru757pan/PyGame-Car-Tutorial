import pygame

pygame.init()


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_text_center(win, font, text):
    pygame.font.init()
    render = font.render(text, 1, (255, 0, 0))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))


def lerp(A, B, t):
    return A + (B - A) * t


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


def getIntersection1(A, B, C, D):
    tTop = (D['x'] - C['x']) * (A['y'] - C['y']) - \
        (D['y'] - C['y']) * (A['x'] - C['x'])
    uTop = (C['y'] - A['y']) * (A['x'] - B['x']) - \
        (C['x'] - A['x']) * (A['y'] - B['y'])
    bottom = (D['y'] - C['y']) * (B['x'] - A['x']) - \
        (D['x'] - C['x']) * (B['y'] - A['y'])

    if bottom != 0:
        t = tTop / bottom
        u = uTop / bottom
        if t >= 0 and t <= 1 and u >= 0 and u <= 1:
            return {
                'x': lerp(A['x'], B['x'], t),
                'y': lerp(A['y'], B['y'], t),
                'offset': t
            }

    return None


def polysIntersect(poly1, poly2):
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            touch = getIntersection1(
                poly1[i],
                poly1[(i + 1) % len(poly1)],
                poly2[j],
                poly2[(j + 1) % len(poly2)]
            )
            if touch:
                return True

    return False


def getRGB(value):
    if value is None:
        return (0, 0, 255)
    R = 0 if value < 0 else 255
    G = R
    B = 0 if value > 0 else 255

    return (R, G, B)
