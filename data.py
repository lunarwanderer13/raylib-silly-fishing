import json
from pathlib import Path
from config import DefaultConfig

class SaveManager:
    def __init__(self, path: str | Path) -> None:
        self.path: Path = Path(path)

    def load(self) -> dict[str, object]:
        if not self.path.exists():
            self.save(None)

        with open(self.path, "r") as file:
            return json.load(file)

    def save(self, data: dict[str, object] | None = None) -> None:
        if not data: data: dict[str, object] = {
            "keybinds": DefaultConfig.keybinds,
            "fps": DefaultConfig.fps,
            "fullscreen": DefaultConfig.fullscreen,
        }

        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)