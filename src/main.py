import pygame
import pygame_gui
import time
import logging

import logic.state as state
from ui.ui_main import UIMain
import ui.images as sprites

WINDOW_SIZE = width, height = 800, 600
FPS_TARGET = 30

print(f"CURRENT STATE = {state.CURRENT_STATE}")

pygame.init()
pygame.display.set_caption('MTG')

window_surface = pygame.display.set_mode(WINDOW_SIZE) # base box
background = pygame.Surface(WINDOW_SIZE)
manager = pygame_gui.UIManager((width, height))

clock = pygame.time.Clock()
is_running = True

def splash(start_time):
    delta = pygame.time.get_ticks() - start_time
    if delta <= 10000:
        background.blit(sprites.splash, (100,100))



def init():
    pass

def game():
    pass

def main():
    global window_surface, background, manager, clock, is_running

    start_time = pygame.time.get_ticks()

    while is_running:
        background.fill((0,0,0))
        time_delta = clock.tick(FPS_TARGET)/1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)

        myfont = pygame.font.SysFont("Arial", 14)
        letter = myfont.render(str(int(clock.get_fps())),0,(255,255,255))
        background.blit(letter,(0,0))

        # Show splash for 5s
        splash(start_time)

        
        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)       

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()