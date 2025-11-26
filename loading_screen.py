import pygame
import config
from asset_loader import load_font, load_and_play_music


class LoadingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.start_time = pygame.time.get_ticks()
        self.text_alpha = 0
        self.show_text = False
        self.music_played = False

        # Font
        logo_font = load_font(config.FONT_NAME, config.FONT_SIZE)
        self.logo_text = logo_font.render("UWU", True, config.WHITE)
        self.logo_text = self.logo_text.convert_alpha()
        self.logo_rect = self.logo_text.get_rect(
            center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2)
        )

    def run(self):
        """Returns when loading screen finishes (after 3 seconds)."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

            elapsed = pygame.time.get_ticks() - self.start_time

            # Fade text after 1 second
            if elapsed >= 1000:
                self.show_text = True

            # Play music after 1 second
            if elapsed >= 1000 and not self.music_played:
                load_and_play_music(config.MUSIC_FILE)
                self.music_played = True

            # End loading screen after 3 seconds
            if elapsed >= 3000:
                return "done"

            self.screen.fill(config.BLACK)

            if self.show_text:
                if self.text_alpha < 255:
                    self.text_alpha += 5
                self.logo_text.set_alpha(self.text_alpha)
                self.screen.blit(self.logo_text, self.logo_rect)

            pygame.display.flip()
            self.clock.tick(60)
