"""Input utilities for Android device text input."""

import pyautogui
import pyperclip
import time


def type_text(text: str, device_id: str | None = None) -> None:
    pyperclip.copy(text)
    pyautogui.hotkey("command", "v")
    # pyautogui.typewrite(app_name)
    time.sleep(0.2)
    pass


def clear_text(device_id: str | None = None) -> None:
    pyautogui.press('backspace', presses=5)
    pass


def detect_and_set_adb_keyboard(device_id: str | None = None) -> str:
    return ""


def restore_keyboard(ime: str, device_id: str | None = None) -> None:
    pass
