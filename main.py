import pygame

from constants import *

from player import *

from asteroid import *

from asteroidfield import *

from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0

    print(
        f"Starting asteroids!\n"
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
          )

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers =(updatable,drawable,shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = my_clock.tick(60)/1000
        pygame.Surface.fill(screen,color=(0,0,0,1))
        for blob in updatable:
            blob.update(dt)
        for blob in asteroids:
            if blob.collide(player) == True:
                print("Game over!")
                return
        for blob in asteroids:
            for stuff in shots:
                if blob.collide(stuff) == True:
                    blob.split()
                    stuff.kill()
        for blob in drawable:
            blob.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()