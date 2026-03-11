# Qwen API 演示项目

基于阿里云 Qwen（通义千问）大模型的 API 调用演示项目，提供 Python 和 Node.js 两种实现。

## 系统环境

- **操作系统**: Ubuntu 24.04.4 LTS (WSL2)
- **Node.js**: v22.22.1
- **npm**: v10.9.4
- **Python**: 3.12+
- **包管理器**: nvm (Node Version Manager)

## 项目结构

```
qwen-api-demo/
├── qwen_chat.py        # Qwen API 基础聊天脚本（Python）
├── test_qwen_api.py    # Python 交互式对话脚本
├── qwen-api-node.js    # Node.js 交互式对话脚本
├── README.md           # 项目说明文档
└── QWEN_CODE.md        # Qwen Code 配置说明
```

## 快速开始

### Python 版本

#### 安装依赖

```bash
pip3 install requests
```

#### 运行脚本

```bash
# 基础版本
python3 qwen_chat.py

# 交互式版本
python3 test_qwen_api.py
```

### Node.js 版本

#### 安装依赖

```bash
npm install axios
```

#### 运行脚本

```bash
node qwen-api-node.js
```

## API 配置

在脚本中修改以下配置：

```javascript
// API 配置
const API_KEY = 'sk-xxxxxxxxxxxxx';  // 替换为你的 API Key
const BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1';
const MODEL = 'qwen3.5-plus';
```

## 功能特性

| 脚本 | 功能 | 语言 |
|------|------|------|
| `qwen_chat.py` | 单次对话，适合测试 | Python |
| `test_qwen_api.py` | 多轮对话，支持上下文 | Python |
| `qwen-api-node.js` | 多轮对话，支持重试机制 | Node.js |

## 环境搭建

### 安装 nvm

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
```

### 安装 Node.js 22

```bash
nvm install 22
nvm alias default 22
nvm use 22
```

### 验证安装

```bash
node --version  # v22.22.1
npm --version   # 10.9.4
```

## 常见问题

### Node.js 版本切换

```bash
# 查看已安装版本
nvm list

# 切换到特定版本
nvm use 20
nvm use 22
```

### nvm 命令未找到

```bash
source ~/.nvm/nvm.sh
```

### API 调用失败

1. 检查 API Key 是否正确
2. 检查网络连接
3. 查看错误信息

## 参考链接

- [nvm GitHub](https://github.com/nvm-sh/nvm)
- [Node.js 官网](https://nodejs.org/)
- [Qwen API 文档](https://help.aliyun.com/zh/dashscope/)
- [DashScope 控制台](https://dashscope.console.aliyun.com/)

## 许可证

MIT
