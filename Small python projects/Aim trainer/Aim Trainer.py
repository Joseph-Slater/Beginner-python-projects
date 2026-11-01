import pygame
import math
import random
import time
from pathlib import Path
pygame.init()

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

BG_COLOUR = (0, 21, 255)

file_path = Path(__file__).parent / "highscore.txt"

LIVES = 3

# Creating display
TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.SysFont("comicsans", 24)
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOUR1 = "red"
    COLOUR2 = "white"
    def __init__(self, x, y):
        self.x = y
        self.y = x
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    # Drawing the target
    def draw(self, win):
        pygame.draw.circle(win, self.COLOUR1, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.COLOUR2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOUR1, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.COLOUR2, (self.x, self.y), self.size * 0.3)

    def collide(self, x, y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size
        
def draw(win, targets):
    win.fill(BG_COLOUR)

    for target in targets:
        target.draw(win)


def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000 / 100))
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)
    return f"{minutes:02d}:{seconds:02d}.{milli}"

def get_best_accuracy():
    try:
        with open(file_path, "r") as f:
            return float(f.read())
    except (FileNotFoundError, ValueError):
        return None
    
def start_screen(win):
    pygame.time.wait(10)
    start = True
# High score on start screen
    best_accuracy = get_best_accuracy()
    if best_accuracy is None:
        label_highscore = LABEL_FONT.render(f"Play to set a high score", 1, "white")
        win.blit(label_highscore, (get_middle(label_highscore), 300))
    else:
        label_highscore = LABEL_FONT.render(f"Current high score: {best_accuracy}%", 1, "white")
        win.blit(label_highscore, (get_middle(label_highscore), 300))

    while start:
        prompt = LABEL_FONT.render("Press a key to start", 1, "white")
        win.blit(prompt, (5, 5))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                start = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        


def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "white", (0,0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed}", 1, "black")

    hit_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")

    lives_label = LABEL_FONT.render(f"Lives: {LIVES}", 1, "black")

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (205, 5))
    win.blit(hit_label, (405, 5))
    win.blit(lives_label, (605, 5))

def end_screen(win, elapsed_time, targets_pressed, clicks):
    pygame.time.wait(10)
    win.fill(BG_COLOUR) #clears whole screen
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "white")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed}", 1, "white")

    hit_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "white")

    accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "white")

    win.blit(time_label, (get_middle(time_label), 150))
    win.blit(speed_label, (get_middle(speed_label), 250))
    win.blit(hit_label, (get_middle(hit_label), 350))
    win.blit(accuracy_label, (get_middle(accuracy_label), 450))

    pygame.display.update()

    best_accuracy = get_best_accuracy()
    if best_accuracy is None or accuracy > best_accuracy:
        with open(file_path, "w") as f:
            f.write(str(accuracy))

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False


def get_middle(surface: pygame.Surface) -> float:
    return WIDTH / 2 - surface.get_width()/2

def main():
    start_screen(WIN)
    run = True
    targets = []
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0
    global LIVES
    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    # To close tab when X is pressed
    while run:
        clock.tick(60)
        click = False
        hit_any = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
             #loops through all current events
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
        for target in targets:
            target.update()

            #Delete old targets to remove lag
            #Keep if before update otherwise new growing targets wont spawn
            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                target_pressed += 1
                hit_any = True

        if click and not hit_any:
                LIVES -= 1

        if LIVES <= 0:
            end_screen(WIN, elapsed_time, target_pressed, clicks)
            run = False

        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, target_pressed, misses)
        pygame.display.update()

    pygame.quit()

# So that if we import functions in another file it doesn't cause the game to run
if __name__ == "__main__":
    main()

