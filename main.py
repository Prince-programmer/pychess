import os
import pygame
import sys
from ChessMain import main

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1050, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (255, 0, 0)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def display_text(text, screen, pos: list, font_size=32, color=(0, 0, 0)):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = pos[0] - text_surface.get_width() // 2
    text_rect.y = pos[1] - text_surface.get_height() // 2
    screen.blit(text_surface, text_rect)
    return text_rect

class Game:
    def __init__(self):
        pygame.init()
        # Load the icon image
        icon = pygame.image.load(resource_path('chess-icon.png'))

        # Set the application icon
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Pychess")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_state = "Intro"
        self.intro_texts = ["Welcome to the Game!","A Project by Prince Parmar","Loading..."]
        self.current_text_index = 0
        self.text_duration = 2000  # 2 seconds in milliseconds
        self.start_time = pygame.time.get_ticks()
        self.box_functions = [
            "Player vs Player",
            "Player vs Computer"
        ]
        self.player_one = True  # Default to player vs player
        self.player_two = True

    def render_intro(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if elapsed_time >= self.text_duration:
            self.current_text_index += 1
            self.start_time = pygame.time.get_ticks()  # Reset start time

        if self.current_text_index < len(self.intro_texts):
            self.screen.fill(BLACK)
            for i in range(7):
                display_text(self.intro_texts[self.current_text_index], self.screen, ((SCREEN_WIDTH // 2)+i, (SCREEN_HEIGHT // 2)+i),font_size=64, color=(255-(i*25),255-(i*25),255-(i*25)))
        else:
            self.current_state = "Main Menu"  # Transition to main menu

        pygame.display.flip()

    def render_menu(self):
        self.screen.fill(WHITE)  # Fill the screen with white color

        if self.current_state == "Main Menu":
            # Define the positions and dimensions of the boxes
            box_width = 350
            box_height = 250
            box_spacing = 20
            start_x = (SCREEN_WIDTH - (box_width * 2 + box_spacing)) // 2
            start_y = (SCREEN_HEIGHT - box_height) // 2

            # Draw and render the boxes with text
            for i, text in enumerate(self.box_functions):
                box_rect = pygame.Rect(start_x + (box_width + box_spacing) * i, start_y, box_width, box_height)
                pygame.draw.rect(self.screen, BLACK, box_rect)
                # Check for mouse hover on the boxes
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if box_rect.collidepoint(mouse_x, mouse_y):
                    pygame.draw.rect(self.screen, HOVER_COLOR, box_rect)
                for i in range(5):
                    display_text(text, self.screen, (box_rect.centerx+i, box_rect.centery+i), color=(0+(i*50),0+(i*50),0+(i*50)))
                # display_text(text, self.screen, (box_rect.centerx, box_rect.centery), color=WHITE)

                

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                self.handle_box_click()

    def handle_box_click(self):
        if self.current_state == "Main Menu":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            box_width = 350
            box_height = 250
            box_spacing = 20
            start_x = (SCREEN_WIDTH - (box_width * 2 + box_spacing)) // 2
            start_y = (SCREEN_HEIGHT - box_height) // 2
            for i, text in enumerate(self.box_functions):
                box_rect = pygame.Rect(start_x + (box_width + box_spacing) * i, start_y, box_width, box_height)
                if box_rect.collidepoint(mouse_x, mouse_y):
                    if text == "Player vs Player":
                        self.player_one = True
                        self.player_two = True
                        print("player vs player")
                    elif text == "Player vs Computer":
                        self.player_one = True
                        self.player_two = False
                        print("player vs computer")
                    self.current_state = "Gameplay"  # Transition to gameplay state


    def run(self):
        while self.running:
            if self.current_state == "Intro":
                self.render_intro()
            elif self.current_state == "Main Menu":
                self.handle_events()
                self.render_menu()
            elif self.current_state == "Gameplay":
                main(self)
                self.current_state = "Main Menu"
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()
