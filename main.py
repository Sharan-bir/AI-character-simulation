import pygame
import config
from loading_screen import LoadingScreen
from main_menu import GameMenu


def main():
    pygame.init()
    pygame.mixer.init()

    icon = pygame.image.load(config.GAME_ICON)
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.GAME_CAPTION)

    # --- 1. SHOW LOADING SCREEN ---
    loading = LoadingScreen(screen)
    result = loading.run()

    if result == "quit":
        return

    # --- 2. SHOW GAME MENU ---
    menu = GameMenu(screen)
    menu_result = menu.run() # Capture the result

    if menu_result == "quit":
        return
    
    # --- 3. START GAME (Chat Screen) ---
    if menu_result == "start_game":
        # We need a new class for the game itself!
        # from game_screen import ChatScreen 
        # game = ChatScreen(screen) 
        # game.run() 
        print("Game Started! Time to implement the Chat Screen.") 

if __name__ == "__main__":
    main()
