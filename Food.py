import pygame
import random

class Food():
    DEFAULT_FOOD_RADIUS = 5
    DEFAULT_FOOD_COLOR = "red"
    def __init__(self, xy_coordinates, radius = DEFAULT_FOOD_RADIUS, color = DEFAULT_FOOD_COLOR) -> None:
      self.color = color
      self.center = pygame.Vector2(xy_coordinates)
      self.radius = radius

    def __init__(self, xlim, ylim, xy_exclude: list[tuple], radius = DEFAULT_FOOD_RADIUS, color = DEFAULT_FOOD_COLOR) -> None:
      (x, y) = xy_exclude[0]
      while (x, y) in xy_exclude:
        x = random.randint(xlim[0], xlim[1])
        y = random.randint(ylim[0], ylim[1])

      self.color = color
      self.center = pygame.Vector2(x,y)
      self.radius = radius

    def render_food(self, screen):
      pygame.draw.circle(screen, self.color, self.center, self.radius)

    def collision_with_point(self, xy_point):
      x = xy_point.x
      y = xy_point.y
      return (x - self.center.x)**2 + (y - self.center.y)**2 - self.radius**2 <= 0

