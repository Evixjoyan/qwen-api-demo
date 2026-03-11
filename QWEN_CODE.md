# Qwen Code 配置说明

## 安装 Qwen Code

```bash
# 使用 npm 全局安装
npm install -g @anthropic/qwen-code
```

## 配置 API Key

### 方式一：环境变量

```bash
export QWEN_API_KEY="sk-846d3522bff246b991fedcf31f47a5b6"
```

### 方式二：配置文件

创建 `~/.qwen-code/config.json`：

```json
{
  "apiKey": "sk-846d3522bff246b991fedcf31f47a5b6",
  "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
  "model": "qwen3.5-plus"
}
```

### 方式三：.env 文件

在项目根目录创建 `.env` 文件：

```env
QWEN_API_KEY=sk-846d3522bff246b991fedcf31f47a5b6
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
QWEN_MODEL=qwen3.5-plus
```

## 验证安装

```bash
qwen-code --version
qwen-code --help
```

## 使用示例

```bash
# 运行对话
qwen-code chat "你好，请介绍一下自己"

# 代码生成
qwen-code generate "创建一个 Python Flask 应用"

# 文件分析
qwen-code analyze ./src
```

## 注意事项

⚠️ **安全提示**：
- 不要将 API Key 提交到 Git 仓库
- 将 `.env` 添加到 `.gitignore`
- 生产环境使用环境变量管理密钥

## 相关资源

- [Qwen Code 文档](https://help.aliyun.com/zh/dashscope/)
- [DashScope API 文档](https://dashscope.aliyuncs.com/)
