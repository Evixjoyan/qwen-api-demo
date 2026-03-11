/**
 * Qwen API 对话测试脚本 - Node.js 版本
 * 用于测试 Qwen API 的对话功能
 */

const axios = require('axios');

// API 配置
const API_KEY = 'sk-846d3522bff246b991fedcf31f47a5b6';
const BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1';
const MODEL = 'qwen3.5-plus';

/**
 * 调用 Qwen API
 * @param {string} prompt - 用户输入
 * @param {Array} history - 对话历史
 * @returns {Promise<string>} AI 回复
 */
async function callQwen(prompt, history = []) {
    const messages = [...history, { role: 'user', content: prompt }];
    
    try {
        const response = await axios.post(
            `${BASE_URL}/chat/completions`,
            {
                model: MODEL,
                messages: messages,
                temperature: 0.7,
                max_tokens: 2048
            },
            {
                headers: {
                    'Authorization': `Bearer ${API_KEY}`,
                    'Content-Type': 'application/json'
                },
                timeout: 30000
            }
        );
        return response.data.choices[0].message.content;
    } catch (error) {
        if (error.response) {
            return `错误：${error.message} - ${JSON.stringify(error.response.data)}`;
        }
        return `错误：${error.message}`;
    }
}

/**
 * 主函数 - 交互式对话
 */
async function main() {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log('='.repeat(50));
    console.log('Qwen API 对话测试 (Node.js)');
    console.log('='.repeat(50));
    console.log("输入 'quit' 或 'exit' 退出\n");

    const history = [];

    const ask = () => {
        readline.question('你：', async (userInput) => {
            const input = userInput.trim().toLowerCase();
            
            if (['quit', 'exit', 'q'].includes(input)) {
                console.log('再见！');
                readline.close();
                return;
            }

            if (!userInput.trim()) {
                ask();
                return;
            }

            process.stdout.write('Qwen 思考中...\r');
            
            try {
                const response = await callQwen(userInput, history);
                console.log(`Qwen：${response}\n`);
                
                // 更新对话历史
                history.push({ role: 'user', content: userInput });
                history.push({ role: 'assistant', content: response });
            } catch (error) {
                console.log(`错误：${error.message}\n`);
            }
            
            ask();
        });
    };

    ask();
}

// 运行主函数
main();
