from phone_agent.ios.screenshot import grab_screen_image
from phone_agent.adb.screenshot import Screenshot
from phone_agent.ios.apps import APP_PACKAGES
import time
import pyautogui
import pyperclip

window_left = 0
window_top = 0


def focus_window():
    global window_left, window_top
    pyautogui.click(window_left + 200, window_top + 40)
    print('focus window')
    time.sleep(0.2)


def get_current_app(device_id: str | None = None) -> str:
    return "未知"


def get_screenshot(device_id: str | None = None, timeout: int = 10) -> Screenshot:
    position, img_base64 = grab_screen_image(save=True)
    global window_left, window_top
    window_left = position[0]
    window_top = position[1]

    return Screenshot(
        base64_data=img_base64, width=position[2], height=position[3], is_sensitive=False
    )


def launch_app(app_name: str, device_id: str | None = None, delay: float = 1.0) -> bool:
    if app_name not in APP_PACKAGES:
        return False

    global window_left, window_top

    focus_window()

    # 切换到HOME
    pyautogui.hotkey("command", "1")
    time.sleep(1)

    # 聚焦
    pyautogui.hotkey("command", "3")
    time.sleep(1)

    pyautogui.press('backspace', presses=5)
    time.sleep(0.5)

    app_pinyin = APP_PACKAGES[app_name]
    pyperclip.copy(app_pinyin)
    pyautogui.hotkey("command", "v")
    time.sleep(1)

    pyautogui.click(window_left + 50, window_top + 150, interval=0.5)
    time.sleep(1)

    time.sleep(delay)
    return True


def tap(x: int, y: int, device_id: str | None = None, delay: float = 1.0) -> None:
    global window_left, window_top
    pyautogui.moveTo(window_left + x, window_top + y)
    time.sleep(1)
    pyautogui.click(window_left + x, window_top + y)
    time.sleep(delay)


def double_tap(
        x: int, y: int, device_id: str | None = None, delay: float = 1.0
) -> None:
    global window_left, window_top
    pyautogui.doubleClick(window_left + x, window_top + y)
    time.sleep(delay)


def long_press(
        x: int,
        y: int,
        duration_ms: int = 3000,
        device_id: str | None = None,
        delay: float = 1.0,
) -> None:
    global window_left, window_top
    pyautogui.mouseDown(window_left + x, window_top + y, duration=1)
    time.sleep(delay)


def swipe(
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        duration_ms: int | None = None,
        device_id: str | None = None,
        delay: float = 1.0,
) -> None:
    global window_left, window_top
    pyautogui.moveTo(window_left + 150, window_top + 200)
    time.sleep(0.5)
    pyautogui.scroll(end_y - start_y)
    time.sleep(delay)


def back(device_id: str | None = None, delay: float = 1.0) -> None:
    time.sleep(delay)


def home(device_id: str | None = None, delay: float = 1.0) -> None:
    focus_window()

    # 切换到HOME
    pyautogui.hotkey("command", "1")
    time.sleep(1)

    time.sleep(delay)
