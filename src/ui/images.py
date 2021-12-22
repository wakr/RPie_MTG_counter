import os
from pygame.image import load
from pygame.transform import scale


base_path = os.path.dirname(__file__)

splash = load(r"C:\Users\k-r-i\Documents\Projects\RPie_MTG_counter\src\images\splash.jpg")
splash = scale(splash, (540, 180))


print("Images loaded")