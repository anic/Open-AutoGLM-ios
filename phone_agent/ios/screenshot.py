import pygetwindow as gw
from PIL import ImageGrab
import base64
import io
import uuid
import os

save_path = 'screenshots'


def get_ios_title():
    titles = gw.getAllTitles()
    for title in titles:
        if 'iPhone镜像' in title:
            return title
    return None


def grab_screen_image(title=None, save=False, dx=0, dy=0, max_width=10000, max_height=10000):
    if title is None:
        title = get_ios_title()

    if title is None:
        return None, None

    left, top, width, height = gw.getWindowGeometry(title)
    # 不需要向量为np.array
    start_x = left + dx
    start_y = top + dy
    end_x = start_x + (width if width < max_width else max_width)
    end_y = start_y + (height if height < max_height else max_height)

    screen = ImageGrab.grab(bbox=(int(start_x), int(start_y), int(end_x), int(end_y)))
    screen = screen.convert('RGB')

    if save:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        screen.save(f'{save_path}/{uuid.uuid4()}.jpg')

    # 创建一个内存中的字节流对象
    buffered = io.BytesIO()
    # 将图像保存到字节流中，这里以 JPEG 格式为例
    screen.save(buffered, format="JPEG")
    # 获取字节流中的二进制数据
    img_byte = buffered.getvalue()
    # 将二进制数据编码为 Base64 字符串
    img_base64 = base64.b64encode(img_byte).decode('utf-8')
    return (left, top, width, height), img_base64
