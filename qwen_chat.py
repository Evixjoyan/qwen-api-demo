import requests
import json

# ===================== 核心配置（替换为你的信息）=====================
API_KEY = "sk-846d3522bff246b991fedcf31f47a5b6"  # 你的阿里云 API Key
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"  # 国内地域（新加坡用 dashscope-intl.aliyuncs.com）
MODEL_NAME = "qwen3.5-plus"  # 模型名称

# ===================== API 调用核心函数 =====================
def call_qwen_api(prompt):
    """调用 Qwen API 并返回响应结果"""
    # 1. 构建请求头（认证核心）
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 2. 构建请求体（对话参数）
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}  # 用户提问内容
        ],
        "temperature": 0.7,  # 随机性（0-1，越小越精准）
        "max_tokens": 2048   # 最大返回字符数
    }

    # 3. 发送请求并处理响应
    try:
        response = requests.post(
            url=f"{BASE_URL}/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )
        response.raise_for_status()  # 捕获 HTTP 错误（如 401/403/500）
        
        # 解析响应结果
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return f"API 响应格式异常：{result}"
    
    except requests.exceptions.HTTPError as e:
        return f"HTTP 错误：{e}，响应内容：{response.text}"
    except requests.exceptions.ConnectionError:
        return "网络连接错误，请检查网络或 Base URL 是否正确"
    except Exception as e:
        return f"未知错误：{str(e)}"

# ===================== 测试调用 =====================
if __name__ == "__main__":
    # 测试提问（可替换为你想测试的问题）
    test_prompt = "请解释 Python 中的列表推导式，并给出示例代码"
    
    # 调用 API 并打印结果
    print("=== Qwen API 调用结果 ===")
    print(f"提问：{test_prompt}\n")
    print(f"回答：{call_qwen_api(test_prompt)}")
