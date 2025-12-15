"""App name to package name mapping for supported applications."""

APP_PACKAGES: dict[str, str] = {
    "浏览器": "浏览器",
    "微信": "微信",
    "QQ": "QQ",
    "微博": "微博",
    "淘宝": "淘宝",
    "京东": "京东",
    "拼多多": "拼多多",
    "淘宝闪购": "淘宝闪购",
    "京东秒送": "京东秒送",
    "小红书": "小红书",
    "豆瓣": "豆瓣",
    "知乎": "知乎",
    "高德地图": "高德地图",
    "百度地图": "百度地图",
    "美团": "美团",
    "大众点评": "大众点评",
    "饿了么": "饿了么",
    "肯德基": "肯德基",
    "携程": "携程",
    "铁路12306": "铁路12306",
    "12306": "12306",
    "去哪儿": "去哪儿",
    "去哪儿旅行": "去哪儿旅行",
    "滴滴出行": "滴滴出行",
    "bilibili": "bilibili",
    "抖音": "抖音",
    "快手": "快手",
    "腾讯视频": "腾讯视频",
    "爱奇艺": "爱奇艺",
    "优酷视频": "优酷视频",
    "芒果TV": "芒果TV",
    "红果短剧": "红果短剧",
    "网易云音乐": "网易云音乐",
    "QQ音乐": "QQ音乐",
    "汽水音乐": "汽水音乐",
    "喜马拉雅": "喜马拉雅",
    "番茄小说": "番茄小说",
    "番茄免费小说": "番茄免费小说",
    "七猫免费小说": "七猫免费小说",
    "飞书": "飞书",
    "QQ邮箱": "QQ邮箱",
    "豆包": "豆包",
    "keep": "keep",
    "美柚": "美柚",
    "腾讯新闻": "腾讯新闻",
    "今日头条": "今日头条",
    "贝壳找房": "贝壳找房",
    "安居客": "安居客",
    "同花顺": "同花顺",
    "星穹铁道": "星穹铁道",
    "崩坏：星穹铁道": "崩坏：星穹铁道",
    "恋与深空": "恋与深空",
}


def get_package_name(app_name: str) -> str | None:
    """
    Get the package name for an app.

    Args:
        app_name: The display name of the app.

    Returns:
        The Android package name, or None if not found.
    """
    return APP_PACKAGES.get(app_name)


def get_app_name(package_name: str) -> str | None:
    """
    Get the app name from a package name.

    Args:
        package_name: The Android package name.

    Returns:
        The display name of the app, or None if not found.
    """
    for name, package in APP_PACKAGES.items():
        if package == package_name:
            return name
    return None


def list_supported_apps() -> list[str]:
    """
    Get a list of all supported app names.

    Returns:
        List of app names.
    """
    return list(APP_PACKAGES.keys())


