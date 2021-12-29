from pygame.image import load
from pygame.transform import scale

from logic.utils import resolve_relative_path

splash = load(resolve_relative_path(__file__, "../images/splash.jpg"))
splash = scale(splash, (540, 180))


print("Images loaded")