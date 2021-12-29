import pygame
import pygame_gui
import time
import logging

import logic.state as state
from ui.ui_main import UIMain
import ui.images as sprites
import config

# VARS
WINDOW_SIZE = width, height = 800, 600
FPS_TARGET = 30

pygame.init()
pygame.display.set_caption(f'MTG - {config.config_data.get("version")}')

window_surface = pygame.display.set_mode(WINDOW_SIZE) # base box
background = pygame.Surface(WINDOW_SIZE)
manager = pygame_gui.UIManager((width, height))
clock = pygame.time.Clock()

is_running = True

hello_btn = None

def splash(start_time):
    delta = pygame.time.get_ticks() - start_time
    if delta <= 3000:
        background.fill((255,255,255))
        background.blit(sprites.splash, (100,100))
    else:
        state.CURRENT_STATE = state.AppState.INIT

        
def init():
    hello_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)


def game():
    p1_camera = pygame.Rect(0,0,400,300)
    p2_camera = pygame.Rect(400,0,400,300)
    p3_camera = pygame.Rect(0,300,400,300)
    p4_camera = pygame.Rect(400,300,400,300)

    sub1 = background.subsurface(p1_camera)
    sub2 = background.subsurface(p2_camera)
    sub3 = background.subsurface(p3_camera)
    sub4 = background.subsurface(p4_camera)

    pygame.draw.line(sub2, (255,255,255), (0,0), (0,300), 10)
    pygame.draw.line(sub4, (255,255,255), (0,0), (0,300), 10)
    pygame.draw.line(sub3, (255,255,255), (0,0), (400,0), 10)
    pygame.draw.line(sub4, (255,255,255), (0,0), (400,0), 10)

    window_surface.blit(sub1, (0,0))
    window_surface.blit(sub2, (400, 0))
    window_surface.blit(sub3, (0, 300))
    window_surface.blit(sub4, (400, 300))

def main():
    global window_surface, background, manager, clock, is_running

    start_time = pygame.time.get_ticks()

    while is_running:
        background.fill((0,0,0))
        time_delta = clock.tick(FPS_TARGET)/1000.0
        print(f"CURRENT STATE = {state.CURRENT_STATE}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_btn:
                        print("MOI!")
                

            manager.process_events(event)

        # DEBUG
        myfont = pygame.font.SysFont("Arial", 14)
        letter = myfont.render(str(int(clock.get_fps())),0,(0,255,0))
        background.blit(letter,(0,0))

        # Show splash for 5s
        if state.CURRENT_STATE == state.AppState.SPLASH:
            splash(start_time)

        if state.CURRENT_STATE == state.AppState.INIT:
            game()

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)       

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()