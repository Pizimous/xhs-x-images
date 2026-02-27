# baoyu-xhs-images

小红书风格图片生成器 - OpenClaw Skill 版本

## 简介

这是一个基于 [baoyu-skills](https://github.com/JimLiu/baoyu-skills) 改造的 OpenClaw Skill，专门用于生成小红书（XHS）风格的图文卡片。

## 功能

- 🎨 支持多种视觉风格：cute, fresh, warm, bold, minimal, retro, pop, notion, chalkboard
- 📐 支持多种布局：sparse, balanced, dense, list, comparison, flow
- 🤖 支持多种 AI 生图后端：Google Gemini, OpenAI, 阿里云 DashScope

## 安装

```bash
npx clawhub install baoyu-xhs-images
```

或手动安装：

```bash
git clone https://github.com/Pizimous/baoyu-xhs-images.git
cd baoyu-xhs-images
```

## 配置

需要设置 AI 生图 API Key：

```bash
# Google Gemini (推荐)
export GOOGLE_API_KEY=your_google_api_key

# 或 OpenAI
export OPENAI_API_KEY=your_openai_api_key

# 或阿里云 DashScope
export DASHSCOPE_API_KEY=your_dashscope_api_key
```

## 使用方法

### 基本用法

```
生成一张关于 [主题] 的小红书图片
```

### 指定风格

```
生成一张 [主题] 的图片，风格用 cute
```

支持的风格：
- cute (默认) - 甜美可爱
- fresh - 清新自然
- warm - 温暖友好
- bold - 强烈吸睛
- minimal - 极简精致
- retro - 复古怀旧
- pop - 活泼醒目
- notion - 简约手绘
- chalkboard - 粉笔风格

### 指定布局

```
生成一张 [主题] 的图片，布局用 dense
```

支持的布局：
- sparse - 稀疏（1-2点）
- balanced (默认) - 平衡（3-4点）
- dense - 密集（5-8点）
- list - 列表（4-7项）
- comparison - 对比
- flow - 流程

### 完整示例

```
生成一张"AI工具推荐"的图片，风格用 notion，布局用 list
```

## 示例输出

生成的图片风格参考：

- cute + balanced: 甜美风格，平衡布局
- notion + dense: 知识卡片风格
- bold + list: 干货清单风格

## 技术细节

- 语言：Python
- 依赖：无（仅使用标准库）
- API：支持 Google Gemini, OpenAI, 阿里云 DashScope

## 开发

### 本地测试

```bash
python script.py --topic "AI工具推荐" --style notion --layout list
```

### 项目结构

```
baoyu-xhs-images/
├── SKILL.md          # Skill 元数据和说明
├── script.py         # 主程序
└── README.md         # 本文件
```

## 注意事项

1. 需要有效的 AI API Key 才能生成图片
2. 不同 API 提供商可能有不同的速率限制
3. 生成的图片仅供个人学习和使用

## 相关链接

- 原版 baoyu-skills: https://github.com/JimLiu/baoyu-skills
- OpenClaw: https://openclaw.ai
- ClawHub: https://clawhub.com

## License

MIT License
