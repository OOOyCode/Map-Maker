import pygame
from settings import *
from tile import Tile
from ui import UI
from support import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Map maker")
clock = pygame.time.Clock()
running = True

camera_x = 0
camera_pos = 0
camera_moved = 0
menu = False
chosen = (0, 0)
grid = [[("X", "X", "X") for y in range(rows)] for x in range(cols)]

ui = UI()

tile_sprites = pygame.sprite.Group()

for x in range(cols):
    for y in range(rows):
        Tile(x * TILE_WIDTH, y * TILE_HEIGHT, tile_sprites)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if menu:
            ui.input(event)
            chosen = ui.selected
            print(chosen)

    keys = pygame.key.get_just_released()

    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_a]:
        camera_x += 32

        # ajouter une nouvelle colonne à droite
        new_col = [("X", "X", "X") for _ in range(rows)]
        grid.append(new_col)

        # ajouter les tiles correspondants
        x = len(grid) - 1
        for y in range(rows):
            Tile(x * TILE_WIDTH, y * TILE_HEIGHT, tile_sprites)
        camera_pos += 1

    if keys[pygame.K_z]:
        camera_x -= 32
        camera_pos -= 1

    if keys[pygame.K_e]:
        chosen = (3, 3)

    if keys[pygame.K_m]:
        menu = not menu

    if keys[pygame.K_s]:
        with open("map.csv", "w") as file:
            for y in range(rows):
                line = []
                for x in range(len(grid)):
                    line.append(f"{grid[x][y][0]}-{grid[x][y][1]}")
                file.write(",".join(line) + "\n")

    screen.fill("black")

    if pygame.mouse.get_pressed()[0] and not menu:
        mx, my = pygame.mouse.get_pos()

        mx += camera_x

        for tile in tile_sprites:
            if tile.rect.collidepoint((mx, my)):
                tile.image = get_tile(chosen[0], chosen[1], 16, 16)
                tile.image = pygame.transform.scale(tile.image, (32, 32))

                x = mx // TILE_WIDTH
                y = my // TILE_HEIGHT

                if not chosen == (3, 3):
                    grid[x][y] = chosen
                else:
                    grid[x][y] = ("X", "X")
                

    for tile in tile_sprites:
        screen.blit(tile.image, (tile.rect.x - camera_x, tile.rect.y))

    # UI
    if menu:
        ui.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()