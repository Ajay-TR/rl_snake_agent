import pygame
from Snake import Snake
from enum import Enum
from Food import Food

class GameState(Enum):
  QUIT = 0
  RUNNING = 1
  GAME_OVER = 2
  PAUSED = 3
  RESTART = 4

class SnakeGame():

  DEFAULT_INITAL_FPS = 60
  GAME_FPS = 60
  def __init__(self, initSnakeLength = 50, playArea = (500, 500), windowTitle = "SNAKE GAME", fps = DEFAULT_INITAL_FPS) -> None:
    pygame.init()
    
    self.GAME_FPS = fps
    self.DEFAULT_INITAL_FPS = fps
    self.GAME_AREA = playArea
    self.GAME_TITLE = windowTitle
    
    self.screen = pygame.display.set_mode(self.GAME_AREA)
    self.initialLength = initSnakeLength

    self.font = pygame.font.Font(None, 36)
    self.clock = pygame.time.Clock()

    self.boundaryWidth = 2
    self.boundaryColor = "green"
    self.boundaryRect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height()) 
    pygame.display.set_caption(self.GAME_TITLE)
    # print(self.snake.get_snake_body())

  def start_game(self):

    initial_xy = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
    self.snake =  Snake(int(initial_xy.x), int(initial_xy.y), self.initialLength)
    food = Food(xlim=[0, self.screen.get_width()], ylim=[0, self.screen.get_width()], xy_exclude=self.snake.get_snake_body())

    GAME_STATE = GameState.RUNNING

    while GAME_STATE == GameState.RUNNING or GAME_STATE == GameState.PAUSED:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          GAME_STATE = GAME_STATE.QUIT
        if event.type == pygame.KEYDOWN:
          newGameState = self.get_game_state(event.key)
          if newGameState is not None:
            GAME_STATE = newGameState
            
      
            
      if GAME_STATE == GAME_STATE.RUNNING:
        # FILL OR CLEAR THE LAST FRAME
        self.screen.fill("black")
        self.render_game_boundary()
        # GAME RENDER LOGIC/CODE HERE
        food.render_food(self.screen)
        direction = self.get_movement_direction()
        # print(direction)
        self.snake.update_snake_movement(direction)
        self.snake.render_snake_body(self.screen)

        if self.check_snake_eats_food(food):
          self.snake.increase_snake_length()
          self.increase_game_speed()
          food = Food(xlim=[0, self.screen.get_width()], ylim=[0, self.screen.get_width()], xy_exclude=self.snake.get_snake_body())

      if self.snake.self_collision() or self.check_snake_hits_boundary(self.snake.get_snake_head_coordinates()):
        GAME_STATE = GameState.GAME_OVER
      
      if GAME_STATE == GameState.GAME_OVER:
        print("GAME OVER: Hit Boundary or Eats Itself!")
        # If game GAME_over is true, draw game GAME_over
        text = self.font.render("GAME OVER", True, "white")
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.blit(text, [text_x, text_y])
      
      if GAME_STATE == GameState.PAUSED:
        print("GAME PAUSED: Press U to unpause")
        # If game GAME_over is true, draw game GAME_over
        text = self.font.render("GAME PAUSED press U to Unpause", True, "white")
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.blit(text, [text_x, text_y])
      
      # if framesRendered < self.GAME_FPS:
      #    framesRendered += 1
      # else:
      #   self.snake.speed += 0.2
      #   framesRendered = 0
      # print("Current Snake Speed:", self.snake.speed)
      self.clock.tick(self.GAME_FPS) # set framerate
      # flip() the display to put work on screen -> The Render stuff
      pygame.display.flip()
    
    return GAME_STATE

  def check_snake_eats_food(self, food):
    return food.collision_with_point(self.snake.get_snake_head_coordinates())

  def increase_game_speed(self):
    if self.GAME_FPS < 200:
      self.GAME_FPS += 10

  def reset(self):
    self.GAME_FPS = self.DEFAULT_INITAL_FPS

  def run(self):
    game_state = GameState.RESTART
    while game_state != GameState.QUIT:
      if game_state == GameState.RESTART:
        self.reset()
        game_state = self.start_game()
      if game_state == GameState.GAME_OVER:
        after_gameover_event = pygame.event.wait()
        if after_gameover_event.type == pygame.QUIT:
          game_state = GameState.QUIT
        elif after_gameover_event.type == pygame.KEYDOWN:
          newGameState = self.get_game_state(after_gameover_event.key)
          if newGameState is not None:
            game_state = newGameState

    pygame.quit()

  def render_game_boundary(self):
    pygame.draw.rect(self.screen, self.boundaryColor, self.boundaryRect, self.boundaryWidth)

  def check_snake_hits_boundary(self, xy_head):
    x = xy_head.x
    y = xy_head.y

    xlim = (self.boundaryRect.x + 2*self.boundaryWidth, self.boundaryRect.width - 2*self.boundaryWidth)
    ylim = (self.boundaryRect.y + 2*self.boundaryWidth, self.boundaryRect.height - 2*self.boundaryWidth)

    return x < xlim[0] or x > xlim[1] or y < ylim[0] or y > ylim[1] 

  def get_game_state(self, key):
    if key == pygame.K_q:
      print("Pressed Q: Game Quit")
      return GameState.QUIT
    if key == pygame.K_p:
      print("Pressed P: Game Paused")
      return GameState.PAUSED
    if key == pygame.K_r:
      print("Pressed R: Game Restarted")
      return GameState.RESTART
    if key == pygame.K_u:
      print("Pressed U: Game Unpaused")
      return GameState.RUNNING 
    return None

  def get_movement_direction(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        return "UP"
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        return "DOWN"
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        return "LEFT"
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        return "RIGHT"
    return None