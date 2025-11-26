import pygame
import os

def load_font(font_name, size):
    """
    Loads a font from file or system.
    - If font_name is a path to a .ttf/.otf file → load it directly.
    - Otherwise, try loading from system fonts.
    """

    # Check if it's a file path like "assets/font/Audiowide-Regular.ttf"
    if os.path.exists(font_name):
        try:
            print(f"INFO: Successfully loaded and displayed font: {font_name}")
            return pygame.font.Font(font_name, size)
            
        except pygame.error as e:
            print(f"ERROR: Unable to load font file '{font_name}': {e}")
            return pygame.font.Font(None, size)

    # Otherwise treat as system font
    font_path = pygame.font.match_font(font_name)

    if font_path:
        print(f"INFO: Successfully loaded and displayed font: {font_path}")
        return pygame.font.Font(font_path, size)

    print(f"WARNING: Font '{font_name}' not found. Using default font.")
    return pygame.font.Font(None, size)


def load_and_play_music(file_path):
    """
    Loads and starts playing background music in an infinite loop.
    Handles file existence and Pygame mixer errors gracefully.

    :param file_path: The path to the music file (e.g., 'bgm.mp3').
    :return: True if music started successfully, False otherwise.
    """
    if not pygame.mixer.get_init():
        print("WARNING: Pygame mixer is not initialized. Cannot load music.")
        return False

    if not os.path.exists(file_path):
        print(f"WARNING: Music file not found at: {file_path}. Music will not play.")
        return False
     
    try:
        pygame.mixer.music.load(file_path)
        # Play the music. 0 means it plays once.
        pygame.mixer.music.play(0)
        print(f"INFO: Successfully loaded and started music: {file_path}")
        return True
        
    except pygame.error as e:
        print(f"ERROR: Failed to load or play music file '{file_path}': {e}")
        return False
    
def load_sprite_frames(base_path, count, file_extension=".png"):
    """
    Loads a sequence of image files for animation. 
    Assumes files are named sequentially (e.g., 'sprite_0.png', 'sprite_1.png', etc.).

    :param base_path: Base path/name (e.g., 'assets/menu_sprite_')
    :param count: Number of frames to load (e.g., 6)
    :return: A list of pygame.Surface objects.
    """
    frames = []
    for i in range(count):
        file_path = f"{base_path}{i}{file_extension}"
        if not os.path.exists(file_path):
            print(f"WARNING: Sprite frame not found: {file_path}. Skipping frame {i}.")
            continue
        try:
            # Use convert_alpha() for transparency and faster blitting
            frame = pygame.image.load(file_path).convert_alpha()
            frames.append(frame)
        except pygame.error as e:
            print(f"ERROR: Failed to load image {file_path}: {e}")

    return frames

def load_image(file_path):
    # This is where you'd handle loading, converting, and optimizing images
    pass