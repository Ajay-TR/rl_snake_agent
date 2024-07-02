# IMPORTS
import pygame
# from Snake import Snake
from SnakeGame import SnakeGame

snake_game = SnakeGame(initSnakeLength=100, fps=60)
snake_game.run()

# # GAME CONFIGS
# GAME_TITLE: str = "DEEP-RL BASED SNAKE GAME"
# """ Game Window Title """

# GAME_AREA: tuple = (500, 500) 
# """ Area of Play (Width X Height) """

# GAME_FPS: int = 100
# """ FPS/framerate set for the game """

# DUMMY_CIRCLE_RADIUS = 5
# DUMMY_CIRCLE_COLOR = "white"

# def start_and_run_game() -> None:
#   """ Starts and keeps the game running until stopped """
#   pygame.init()
#   font = pygame.font.Font(None, 36)
#   clock = pygame.time.Clock() 
#   screen = pygame.display.set_mode(GAME_AREA)
#   pygame.display.set_caption(GAME_TITLE)    

#   initial_xy = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#   snake = Snake(int(initial_xy.x), int(initial_xy.y), 70)
#   print(snake.get_snake_body())

#   dt = 0
  
#   STOP_GAME: bool = False
#   GAME_OVER: bool = False
#   while not STOP_GAME:
#     for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#         STOP_GAME = True
#       if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_p:
#           print("Pressed P")

#     # FILL OR CLEAR THE LAST FRAME
#     screen.fill("black")
#     # GAME RENDER LOGIC/CODE HERE
#     direction = get_movement_direction()
#     # print(direction)
#     snake.update_snake_movement(direction)
    
#     if not GAME_OVER:
#       snake.render_snake_body(screen)
    
#     if GAME_OVER:
#       print("GAME OVER: Snake Ate Itself!")
#       # If game over is true, draw game over
#       text = font.render("Game Over", True, "white")
#       text_rect = text.get_rect()
#       text_x = screen.get_width() / 2 - text_rect.width / 2
#       text_y = screen.get_height() / 2 - text_rect.height / 2
#       screen.blit(text, [text_x, text_y])
    
#     if snake.self_collision():
#       GAME_OVER = True
#     # clock.tick(GAME_FPS) # set framerate
#     # Set time elapsed since last frame
#     dt = clock.tick(GAME_FPS) / 1000 # sets framerate and also returns time elapsed since the last frame
#     # flip() the display to put work on screen -> The Render stuff
#     pygame.display.flip()
  
#   pygame.quit()


# def get_movement_direction():
#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_w] or keys[pygame.K_UP]:
#       return "UP"
#   if keys[pygame.K_s] or keys[pygame.K_DOWN]:
#       return "DOWN"
#   if keys[pygame.K_a] or keys[pygame.K_LEFT]:
#       return "LEFT"
#   if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
#       return "RIGHT"
#   return None


# start_and_run_game()