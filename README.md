# Open-AutoGLM-ios

这是一个 [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) 适配 ios/iphone 的方案，原项目通过`adb`
与安卓手机进行交互，但无法用于iphone。本项目对此进行一定的改造和尝试，使用`macos`上的`iphone镜像`，操作iphone手机

## 注意事项

使用iphone真机进行测试，可能产生风险，请慎重，请慎重，请慎重！

## 技术说明

项目通过`pyautogui`模拟键鼠操作，与`iphone镜像`中的iphone进行操作和交互
[demo.mp4](https://raw.githubusercontent.com/anic/Open-AutoGLM-ios/main/resources/ios-demo.mp4)

由于ios的封闭性，很多操作不如安卓的`adb`，请大神优化

- 无法获取到当前应用信息
- 输入中文会受输入法限制，建议更多使用点击操作
- 使用`command+v`从剪贴板粘贴内容模拟输入，但非100%生效
- 进入应用内点击可能会弹出奇怪的面板

## 使用方法

参考官方 demo ，其中 AgentConfig 的 os 设置为`ios`

```python
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig
from phone_agent.agent import AgentConfig

# Configure model
model_config = ModelConfig(
    base_url='https://open.bigmodel.cn/api/paas/v4/',
    model_name='AutoGLM-Phone',
    api_key='填写key'
)

agent_config = AgentConfig(
    max_steps=100,
    verbose=True,
    lang='cn',
    os='ios',  # 指定使用ios模式
)

# 创建 Agent
agent = PhoneAgent(model_config=model_config,
                   agent_config=agent_config)

# 执行任务
result = agent.run("打开浏览器，搜索openai，查看openai的官网网址")
print(result)

```
