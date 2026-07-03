from pyray import *
from typing import Any

from player import Player
from config import GameConfig
from data import SaveManager

def main() -> None:
    save_manager: SaveManager = SaveManager("data.json")
    data: dict[str, Any] = save_manager.load()
    player: Player = Player(data)

    # The virtual resolution
    virtual_width: int = int(GameConfig.virtual_resolution.x)
    virtual_height: int = int(GameConfig.virtual_resolution.y)

    init_window(virtual_width * 3, virtual_height * 3, "Silly Fishing")
    set_window_state(ConfigFlags.FLAG_WINDOW_RESIZABLE)

    if ((data["fullscreen"] and not is_window_state(ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE))
            or (not data["fullscreen"] and is_window_state(ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE))):
        toggle_borderless_windowed()

    set_target_fps(data["fps"])

    target: RenderTexture = load_render_texture(virtual_width, virtual_height)
    set_texture_filter(target.texture, TextureFilter.TEXTURE_FILTER_POINT)

    while not window_should_close():
        # Calculate how much the resolution scale has to change to fit the 16:9 resolution
        scale: float = min(
            get_screen_width() / virtual_width,
            get_screen_height() / virtual_height
        )

        # Drawn resolution
        draw_width: float = virtual_width * scale
        draw_height: float = virtual_height * scale

        # Offset the game to keep it centered
        offset_x: float = (get_screen_width() - draw_width) / 2
        offset_y: float = (get_screen_height() - draw_height) / 2

        begin_texture_mode(target)

        # Background color
        clear_background(RAYWHITE)

        player.update()

        end_texture_mode()

        begin_drawing()

        # The color of the offset
        clear_background(BLACK)

        # Drawing the game window
        draw_texture_pro(
            target.texture,
            Rectangle(0, 0, virtual_width, -virtual_height),
            Rectangle(offset_x, offset_y, draw_width, draw_height),
            Vector2(0, 0),
            0,
            WHITE
        )

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()
