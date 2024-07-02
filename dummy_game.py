# IMPORTS
import pygame

# GAME CONFIGS
GAME_TITLE: str = "DEEP-RL BASED SNAKE GAME"
""" Game Window Title """

GAME_AREA: tuple = (500, 500) 
""" Area of Play (Width X Height) """

GAME_FPS: int = 60
""" FPS/framerate set for the game """

DUMMY_CIRCLE_RADIUS = 5
DUMMY_CIRCLE_COLOR = "white"

def start_and_run_game() -> None:
  """ Starts and keeps the game running until stopped """
  pygame.init()
  clock = pygame.time.Clock() 
  screen = pygame.display.set_mode(GAME_AREA)
  pygame.display.set_caption(GAME_TITLE)    

  dt = 0
  pos_xy = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
  
  STOP_GAME: bool = False
  while not STOP_GAME:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        STOP_GAME = True
    
    # FILL OR CLEAR THE LAST FRAME
    screen.fill("black")
    # GAME RENDER LOGIC/CODE HERE
    pos_xy = get_dummy_circle_center_xy(pos_xy, dt)
    render_dummy_circle(screen, pos_xy, DUMMY_CIRCLE_RADIUS)

    # flip() the display to put work on screen -> The Render stuff
    pygame.display.flip()
    # clock.tick(GAME_FPS) # set framerate
    # Set time elapsed since last frame
    dt = clock.tick(GAME_FPS) / 1000 # sets framerate and also returns time elapsed since the last frame
  
  pygame.quit()


def get_dummy_circle_center_xy(prev_xy, dt):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
      prev_xy.y -= 300 * dt
  if keys[pygame.K_s]:
      prev_xy.y += 300 * dt
  if keys[pygame.K_a]:
      prev_xy.x -= 300 * dt
  if keys[pygame.K_d]:
      prev_xy.x += 300 * dt

  return prev_xy
    

def render_dummy_circle(screen, center_xy, radius = 40) -> None:
  pygame.draw.circle(screen, DUMMY_CIRCLE_COLOR, center_xy, radius)


start_and_run_game()