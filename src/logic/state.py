from enum import Enum

class AppState(Enum):
    SPLASH = 0
    INIT = 1
    PLAY = 2
    RESET = 3

CURRENT_STATE = AppState.SPLASH

class UIState():
    splash = 0
    