import pygame
from pygame.locals import *
import time
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SIZE = 40

running=True
playing=True

class Apple:
    def __init__(self,screen):
        self.x=400
        self.y=400
        self.screen=screen
        self.image=pygame.image.load("snake_rs/apple.png")
        self.image =pygame.transform.scale(self.image, (40, 40))
    def move(self):
        self.x= random.randrange(1,19)*SIZE
        self.y= random.randrange(1,19)*SIZE 
    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))

class Snake:
    def __init__(self,screen):
        self.x= [120,80,40]
        self.y= [120,120,120]
        self.head=pygame.image.load("snake_rs/block.png")
        self.head =pygame.transform.scale(self.head, (40, 40))
        self.image=pygame.image.load("snake_rs/player1.png")
        self.image =pygame.transform.scale(self.image, (40, 40))
        self.screen=screen
        self.dir='up'
    def move(self):
        if self.dir== 'right':
            self.x.insert(1,self.x[0])
            self.y.insert(1,self.y[0])
            self.x.pop()
            self.y.pop()
            self.x[0] += SIZE

        if self.dir== 'left':
            self.x.insert(1,self.x[0])
            self.y.insert(1,self.y[0])
            self.x.pop()
            self.y.pop()
            self.x[0] -= SIZE
        if self.dir== 'up':
            self.x.insert(1,self.x[0])
            self.y.insert(1,self.y[0])
            self.x.pop()
            self.y.pop()
            self.y[0] += SIZE
        if  self.dir== 'down':
            self.x.insert(1,self.x[0])
            self.y.insert(1,self.y[0])
            self.x.pop()
            self.y.pop()
            self.y[0] -= SIZE
        self.draw()

    def draw(self):
        self.length=len(self.x)
        for i in range(1,self.length):
            self.screen.blit(self.image,(self.x[i],self.y[i]))
        self.screen.blit(self.head,(self.x[0],self.y[0]))

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Codebasics Snake And Apple Game")
        self.surface = pygame.display.set_mode((800, 800))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        global running
        global playing
        self.surface.fill((255, 255, 255))
        self.apple.draw()
        self.snake.move()
        self.score()
        if self.collision(self.apple.x,self.apple.y,self.snake.x[0], self.snake.y[0]):
            self.snake.x.append(-100)
            self.snake.y.append(-100)
            self.apple.move()
        for i in range(3,self.snake.length):
            if self.collision(self.snake.x[i],self.snake.y[i],self.snake.x[0], self.snake.y[0]):
                playing=False
        if self.snake.x[0] < 0 or self.snake.x[0]+SIZE >800 or self.snake.y[0] < 0 or self.snake.y[0] + SIZE > 800:
            playing=False
    
    def collision(self, x1, y1,x2,y2):
        if x1<=x2 and x2<x1+SIZE:
            if y1 <=y2 and y2 < y1+SIZE:
                return True
        return False

    def game_over(self):
        self.font = pygame.font.SysFont("Time News Roman", 100,True,False)
        self.line1 = self.font.render(f"GAME OVER!",True, BLACK)
        self.surface.blit(self.line1, (150,300))
        self.line2 = self.font.render(f"Your score is {self.snake.length-3}",True, BLACK,WHITE)
        self.surface.blit(self.line2, (120,370))
    def score(self):
        self.font = pygame.font.SysFont("Time News Roman", 40,True,False)
        self.mask = self.font.render(f"SCORE: {self.snake.length-3}",True, BLACK)
        self.surface.blit(self.mask, (600,50))

    def control(self):
        global running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT and self.snake.dir != 'left':
                    self.snake.dir='right'
                if event.key == K_LEFT and self.snake.dir != 'right':
                    self.snake.dir='left'
                if event.key == K_DOWN and self.snake.dir != 'down':
                    self.snake.dir='up'
                if event.key == K_UP and self.snake.dir != 'up':
                    self.snake.dir='down'

    def run(self):
        global running
        global SIZE
        while running:
            self.play()
            if playing:
                self.control()
            else: 
                SIZE=0
                self.game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            time.sleep(0.2)

game = Game()
game.run()
pygame.quit()