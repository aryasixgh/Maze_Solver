import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, x=10, y=10):
    display_surf = pygame.display.get_surface()
    lines = str(info).splitlines()  # Split by \n

    for i, line in enumerate(lines):
        debug_surf = font.render(line, True, "purple")
        debug_rect = debug_surf.get_rect(topleft=(x, y + i * 18))  # 18 px spacing
        display_surf.blit(debug_surf, debug_rect)

    