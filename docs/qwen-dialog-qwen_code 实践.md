# Qwen Code 实践记录

## 项目信息

- **项目名称**: qwen-api-demo
- **GitHub 仓库**: https://github.com/Evixjoyan/qwen-api-demo
- **创建时间**: 2026-03-11
- **环境**: WSL2 (Ubuntu 24.04.4) + Node.js 22.x

---

## 环境搭建

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

---

## OpenClaw 安装与配置

### 安装 OpenClaw

```bash
npm install -g openclaw
```

### 配置 Qwen OAuth

```bash
openclaw configure
```

配置项：
- Gateway 端口：18789
- 认证方式：Token
- 模型提供商：Qwen OAuth（已自动认证）

### 启动 Gateway

```bash
systemctl --user start openclaw-gateway
systemctl --user status openclaw-gateway
```

### Dashboard 地址

```
http://127.0.0.1:18789/#token=<你的 token>
```

---

## 项目文件结构

```
qwen-api-demo/
├── qwen_chat.py        # Qwen API 基础聊天脚本（Python）
├── test_qwen_api.py    # Python 交互式对话脚本
├── qwen-api-node.js    # Node.js 交互式对话脚本
├── README.md           # 项目说明文档
├── QWEN_CODE.md        # Qwen Code 配置说明
└── docs/
    └── qwen-dialog-qwen_code 实践.md  # 本文件
```

---

## Git 提交历史

| 提交哈希 | 日期 | 提交信息 |
|----------|------|----------|
| 987171e | 2026-03-11 | docs: 给 API 脚本添加注释，补充项目说明 |
| c397193 | 2026-03-11 | fix: 修复 Node.js 版本显示异常及 API 调用超时问题 |
| badd8a2 | 2026-03-11 | feat: 编写 Node.js 调用 Qwen API 的对话脚本 |
| 8bf6577 | 2026-03-11 | feat: 编写 Python 调用 Qwen API 的对话脚本 |
| 653a299 | 2026-03-11 | chore: 安装 Qwen Code 并配置 API Key |
| b9ff3fc | 2026-03-11 | init: 完成 WSL 和 Node.js 22.x 环境搭建 |
| 35b5cfb | 2026-03-11 | init: 初始化 Qwen API 演示项目 |

---

## 功能测试结果

### 1. 代码生成 - Python 函数
✅ 成功生成求和函数并附带使用示例

### 2. 代码生成 - HTML 页面
✅ 成功创建 HTML 文件到工作区

### 3. 知识问答 - RESTful API
✅ 成功解释概念和示例

### 4. 天气查询
✅ 成功获取实时天气数据（使用 weather 技能）

### 5. 模型列表
✅ 9 个可用模型（Qwen Coder, Vision 等）

### 6. 技能列表
✅ 51 个技能（2 个就绪：tmux, weather）

---

## API 配置

### Qwen API 配置

```javascript
const API_KEY = 'sk-846d3522bff246b991fedcf31f47a5b6';
const BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1';
const MODEL = 'qwen3.5-plus';
```

### 环境变量方式

```bash
export QWEN_API_KEY="sk-846d3522bff246b991fedcf31f47a5b6"
```

---

## SSH 配置（GitHub 推送）

### 生成 SSH Key

```bash
ssh-keygen -t ed25519 -C "3450967713@qq.com"
```

### SSH 配置（使用端口 443）

```ssh
# ~/.ssh/config
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

### 推送命令

```bash
git remote add origin git@github.com:Evixjoyan/qwen-api-demo.git
git push -u origin master
```

---

## 常用命令

### OpenClaw

```bash
# 查看状态
openclaw status

# 健康检查
openclaw health

# 查看日志
openclaw logs

# 运行对话
openclaw agent --session-id "test" --message "你好"

# 打开 Dashboard
openclaw dashboard
```

### Git

```bash
# 查看状态
git status

# 添加文件
git add .

# 提交
git commit -m "提交信息"

# 推送
git push

# 查看历史
git log --oneline
```

### Node.js

```bash
# 运行 Node.js 脚本
node qwen-api-node.js

# 安装依赖
npm install axios
```

### Python

```bash
# 运行 Python 脚本
python3 test_qwen_api.py

# 安装依赖
pip3 install requests
```

---

## 参考链接

- [OpenClaw 文档](https://docs.openclaw.ai/)
- [Qwen API 文档](https://help.aliyun.com/zh/dashscope/)
- [nvm GitHub](https://github.com/nvm-sh/nvm)
- [Node.js 官网](https://nodejs.org/)

---

**文档更新时间**: 2026-03-11
