# 只用一行代码，轻松调用ChatGPT！OpenAI官方Python库到底有多强？

## OpenAI Python库介绍
OpenAI官方提供的Python SDK。

## 安装使用
```bash
pip install openai
```

## 基本用法
```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## 高级功能
- 流式输出
- 函数调用
- 图像生成
- 音频处理

## 最佳实践
- 错误处理
- API密钥安全
- 请求限制管理
