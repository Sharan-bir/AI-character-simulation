import pygame
import config
from asset_loader import load_font, load_sprite_frames

class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.start_time = pygame.time.get_ticks()
        self.text_alpha = 0
        self.show_text = False
        self.clock = pygame.time.Clock()
        self.BG_COLOR = (20, 20, 20)
        
        # --- Text Setup (Title/Menu Item) ---
        title_font = load_font(config.FONT_NAME, 60)
        self.title_text = title_font.render(config.GAME_TITLE, True, config.WHITE)
        self.title_rect = self.title_text.get_rect(
            center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT * 0.2) 
        )

        # --- Dialogue Box Text Setup ---
        dialogue_font = load_font(config.FONT_NAME, 14)
        self.dialogue_text = dialogue_font.render(config.MENU_TEXT, True, config.DIALOGUE_TEXT_COLOR)
        self.dialogue_rect = self.dialogue_text.get_rect()
        
        # Define Dialogue Box dimensions
        self.box_padding = 4
        self.box_width = self.dialogue_rect.width + 2 * self.box_padding
        self.box_height = self.dialogue_rect.height + 2 * self.box_padding
        
        # Define Dialogue Box position (Bottom Center)
        self.box_x = config.SCREEN_WIDTH // 2 - self.box_width // 2
        self.box_y = config.SCREEN_HEIGHT - self.box_height - 60 
        self.dialogue_box_rect = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)
        
        # Center the dialogue text within the box
        self.dialogue_rect.center = self.dialogue_box_rect.center


        # --- Sprite Animation Setup ---
        SPRITE_COUNT = 6
        # The base path should include the folder and part of the file name before the index
        self.sprite_frames = load_sprite_frames("assets/characters/menu_girl/front_Idle_", SPRITE_COUNT)
        
        self.current_frame = 0
        self.animation_speed = 10 
        self.frame_counter = 0 
        
        self.sprite_rect = None
        if self.sprite_frames:
            first_frame = self.sprite_frames[0]
            self.sprite_rect = first_frame.get_rect(
                bottomright=(config.SCREEN_WIDTH - 260, config.SCREEN_HEIGHT - 1)
            )


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                
                # --- NEW: Input Logic ---
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: # Detect the ENTER key
                        return "start_game" # Return a different value to start the game

            # --- Update Animation State ---
            if self.sprite_frames:
                self.frame_counter += 1
                if self.frame_counter >= self.animation_speed:
                    self.frame_counter = 0
                    self.current_frame = (self.current_frame + 1) % len(self.sprite_frames)

            elapsed = pygame.time.get_ticks() - self.start_time
            # Fade text after 1 second
            if elapsed >= 1000:
                self.show_text = True
                
            # --- Drawing ---
            self.screen.fill(self.BG_COLOR)

            self.screen.blit(self.title_text, self.title_rect)

            # 2. Animated sprite
            if self.sprite_frames:
                current_image = self.sprite_frames[self.current_frame]
                self.screen.blit(current_image, self.sprite_rect)

            # Fade logic only
            if self.show_text and self.text_alpha < 255:
                self.text_alpha += 5

            # Draw dialogue box & text (always)
            if self.show_text:

                pygame.draw.rect(self.screen, config.DIALOGUE_BOX_COLOR,
                                self.dialogue_box_rect, border_radius=6)

                faded_text = self.dialogue_text.copy()
                faded_text.set_alpha(self.text_alpha)
                self.screen.blit(faded_text, self.dialogue_rect)

            pygame.display.flip()
            self.clock.tick(60)
