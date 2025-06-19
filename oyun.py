import pygame

# Pygame'i başlat
pygame.init()

# Ekran oluşturma
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Oyuncu Kontrolleri")

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Oyuncu özellikleri
player_size = (50, 50)
player_x = 375
player_y = 500
speed = 5
jump_force = -15
gravity = 1
velocity_y = 0
on_ground = True

# Saat ve FPS ayarı
clock = pygame.time.Clock()
FPS = 60

# Oyun döngüsü
running = True
while running:
    screen.fill(WHITE)
    
    # Etkinlikleri kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tuş kontrolleri
    keys = pygame.key.get_pressed()
    move_x = 0

    if keys[pygame.K_LEFT]:
        move_x = -speed
    if keys[pygame.K_RIGHT]:
        move_x = speed

    # Zıplama işlemi
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_force
        on_ground = False
    
    # Yerçekimi
    velocity_y += gravity
    player_y += velocity_y

    # Oyuncu zemine değdi mi?
    if player_y >= 500:
        player_y = 500
        on_ground = True
        velocity_y = 0

    # Oyuncuyu güncelle
    player_x += move_x
    pygame.draw.rect(screen, RED, (player_x, player_y, *player_size))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()