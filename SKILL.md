---
name: baoyu-xhs-images
description: 生成小红书风格的图文卡片。支持多种视觉风格和布局，用于社交媒体内容创作。
version: 1.0.0
author: Pizimous (基于 baoyu-skills 改造)
tags:
  - xiaohongshu
  - social-media
  - image-generation
  - chinese
---

# baoyu-xhs-images

生成小红书（XHS）风格的图文卡片。

## 功能

- 支持多种视觉风格：可爱、简约、复古、漫画等
- 支持多种信息布局：稀疏、平衡、密集、对比等
- 调用 AI 生成高质量图片

## 使用方法

### 基本用法

```
生成一张关于 [主题] 的小红书图片
```

### 指定风格

```
生成一张 [主题] 的图片，风格用 cute/ fresh/ warm/ bold/ minimal/ retro/ pop/ notion/ chalkboard
```

### 指定布局

```
生成一张 [主题] 的图片，布局用 sparse/ balanced/ dense/ list/ comparison/ flow
```

### 完整参数

```
生成一张 [主题] 的图片，风格用 [style]，布局用 [layout]
```

## 风格说明

| 风格 | 描述 | 适用场景 |
|------|------|----------|
| cute | 甜美可爱 | 美妆、时尚、生活 |
| fresh | 清新自然 | 健康、自然、美食 |
| warm | 温暖友好 | 情感、生活方式 |
| bold | 强烈吸睛 | 干货、警告、必看 |
| minimal | 极简精致 | 知识、干货、效率 |
| retro | 复古怀旧 | 经典、传统、情怀 |
| pop | 活泼醒目 | 活动、促销、创意 |
| notion | 简约手绘 | 知识、效率、SaaS |
| chalkboard | 粉笔风格 | 教程、教育、学习 |

## 布局说明

| 布局 | 描述 | 适用场景 |
|------|------|----------|
| sparse | 稀疏（1-2点） | 封面、引用 |
| balanced | 平衡（3-4点） | 常规内容 |
| dense | 密集（5-8点） | 知识卡、清单 |
| list | 列表（4-7项） | 排行榜、步骤 |
| comparison | 对比（2侧） | 优缺点对比 |
| flow | 流程（3-6步） | 教程、时间线 |

## 示例

```
生成一张关于"AI工具推荐"的小红书图片
生成一张"5个实用APP"的图片，风格用 notion，布局用 list
```

## 注意事项

- 需要配置 AI 生图 API（支持 Google/OpenAI/DashScope）
- 图片生成可能需要一些时间
- 如遇 API 限制，请稍后重试
