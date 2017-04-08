import pygame

keys = [False] * 350


def invoke(key, event):
    if event == pygame.KEYDOWN:
        keys[key] = True
    elif event == pygame.KEYUP:
        keys[key] = False


def is_key_down(key):
    return keys[key]
