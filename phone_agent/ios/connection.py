from phone_agent.ios.screenshot import get_ios_title


class IosConnection:

    def connect(self, timeout: int = 10) -> tuple[bool, str]:
        title = get_ios_title()

        if title is None:
            return False, '未启动 iPhone镜像'

        return True, '成功连接到 iPhone镜像'
