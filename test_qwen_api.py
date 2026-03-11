#!/usr/bin/env python3
"""
Qwen API 对话测试脚本
用于测试 Qwen API 的对话功能
"""

import requests
import json

# API 配置
API_KEY = "sk-846d3522bff246b991fedcf31f47a5b6"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL = "qwen3.5-plus"


def call_qwen(prompt, history=None):
    """
    调用 Qwen API
    
    Args:
        prompt: 用户输入
        history: 对话历史列表
        
    Returns:
        str: AI 回复
    """
    messages = history.copy() if history else []
    messages.append({"role": "user", "content": prompt})
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2048
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"错误：{str(e)}"


def main():
    """主函数 - 交互式对话"""
    print("=" * 50)
    print("Qwen API 对话测试")
    print("=" * 50)
    print("输入 'quit' 或 'exit' 退出\n")
    
    history = []
    
    while True:
        user_input = input("你：").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("再见！")
            break
        
        if not user_input:
            continue
        
        print("\nQwen 思考中...", end="\r")
        response = call_qwen(user_input, history)
        
        print(f"Qwen：{response}\n")
        
        # 更新对话历史
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
