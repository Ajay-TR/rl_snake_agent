import pygame
from enum import Enum

class Direction(Enum):
  UP = pygame.Vector2(0, -1)
  DOWN = pygame.Vector2(0, 1)
  LEFT = pygame.Vector2(-1, 0)
  RIGHT = pygame.Vector2(1, 0)

class OppositeDirection(Enum):
  UP = "DOWN"
  DOWN = "UP"
  LEFT = "RIGHT"
  RIGHT = "LEFT"


class Snake():

  def __init__(self, init_x, init_y, init_length = 30, color="white", headColor = "red", unitSize = 3, speed = 1) -> None:
    """ initialise the snake and its items """
    print("Snake Initialised with head at (x:{x}, y:{y})".format(x=init_x, y=init_y))
    self.color = color
    self.headColor = headColor
    self.width = unitSize
    self.length = init_length
    self.body = [pygame.Vector2((x, init_y)) for x in range(init_x, init_x - init_length, -1)]
    self.speed = speed
    self.currentDirection = pygame.Vector2(0, 0)
    self.currentVelocity = self.speed * pygame.Vector2(0, 0)

  def self_collision(self) -> bool:
    return True if self.body[0] in self.body[1:] else False

  def increase_snake_length(self, length = 10):
    self.length += length

  def get_snake_body(self):
    return self.body
  
  def get_snake_head_coordinates(self):
    return self.body[0]

  def render_snake_body(self, screen):
    # print(self.body)
    pygame.draw.lines(screen, self.color, False, self.body, self.width)
    pygame.draw.circle(screen, self.headColor, self.body[0], self.width)

  # Snake Movement Methods
  def update_snake_movement(self, direction):
    if type(direction) == str:
      # Check if valid change in direction is requested
      if self.currentDirection != Direction[direction].value and self.currentDirection != Direction[OppositeDirection[direction].value].value:          
        # print("f:", self.currentDirection != Direction[direction])
        # print("s:", self.currentDirection != Direction[OppositeDirection[direction].value])
        # print("Direction Changed From: {fromD} to: {toD}".format(fromD=self.currentDirection, toD=Direction[direction].value))
        self.currentDirection = Direction[direction].value
        self.currentVelocity = self.speed * self.currentDirection
    else:
      if direction is not None:
        raise ValueError("direction must be one of the following: UP, DOWN, RIGHT, LEFT")
    
    self.__update_snake_position()
    
  def __update_snake_position(self):
    if self.currentVelocity != (0, 0):      
      newHead = self.body[0] + self.currentVelocity
      self.body.insert(0, newHead)
      if len(self.body) > self.length:
        self.body.pop()