# WSL 和 Node.js 22.x 环境搭建指南

## 系统环境

- **操作系统**: Ubuntu 24.04.4 LTS (WSL2)
- **Node.js**: v22.22.1
- **npm**: v10.9.4
- **包管理器**: nvm (Node Version Manager)

## 安装步骤

### 1. 安装 nvm

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
```

### 2. 安装 Node.js 22

```bash
nvm install 22
nvm alias default 22
nvm use 22
```

### 3. 验证安装

```bash
node --version  # v22.22.1
npm --version   # 10.9.4
```

## 项目结构

```
qwen-api-demo/
└── qwen_chat.py    # Qwen API 聊天示例
```

## 使用说明

### Python 版本

```bash
pip3 install requests
python3 qwen_chat.py
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

## 参考链接

- [nvm GitHub](https://github.com/nvm-sh/nvm)
- [Node.js 官网](https://nodejs.org/)
- [Qwen API 文档](https://help.aliyun.com/zh/dashscope/)
