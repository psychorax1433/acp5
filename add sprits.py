import pygame
import sys

# ── basic setup ────────────────────────────────────────────────────────────────
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two‑Sprite Demo")

WHITE      = (255, 255, 255)
PLAYER_COL = ( 30, 144, 255)   # DodgerBlue
BLOCK_COL  = (220,  20,  60)   # Crimson
FPS        = 60
SPEED      = 5

# ── sprite classes ─────────────────────────────────────────────────────────────
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size=(60, 60)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(PLAYER_COL)
        self.rect = self.image.get_rect(center=pos)

    def update(self, keys):
        if keys[pygame.K_LEFT]  or keys[pygame.K_a]: self.rect.x -= SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: self.rect.x += SPEED
        if keys[pygame.K_UP]    or keys[pygame.K_w]: self.rect.y -= SPEED
        if keys[pygame.K_DOWN]  or keys[pygame.K_s]: self.rect.y += SPEED

        # keep inside the window
        self.rect.clamp_ip(screen.get_rect())

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size=(80, 80)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(BLOCK_COL)
        self.rect = self.image.get_rect(center=pos)

# ── create sprites & groups ────────────────────────────────────────────────────
player = Player((WIDTH//4, HEIGHT//2))
block  = Block((3*WIDTH//4, HEIGHT//2))

all_sprites = pygame.sprite.Group(block, player)  # draw order: block behind

# ── main loop ──────────────────────────────────────────────────────────────────
clock = pygame.time.Clock()
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update & draw
    player.update(keys)
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
