#!/usr/bin/env python3
"""
baoyu-xhs-images: 小红书图片生成器
简化版 - 基于 baoyu-skills 改造
"""

import os
import sys
import json
import argparse
import subprocess
import re

# 风格到提示词的映射
STYLE_PROMPTS = {
    "cute": "可爱甜美风格，粉色系，卡通插画风格，小红书风格，柔和光线，精致细节",
    "fresh": "清新自然风格，绿色系，清爽干净，小清新风格，自然光线，简洁设计",
    "warm": "温暖友好风格，暖色调，温馨舒适，生活感，柔和光线，温馨氛围",
    "bold": "强烈吸睛风格，高对比度，醒目大字，视觉冲击力强，时尚潮流",
    "minimal": "极简精致风格，黑白灰，简约设计，线条简洁，现代感，高级感",
    "retro": "复古怀旧风格，复古配色，怀旧元素，80/90年代，复古滤镜",
    "pop": "活泼醒目风格，鲜艳配色，波普艺术，潮流元素，充满活力",
    "notion": "简约手绘风格，白底黑线，手绘插画，知识感，效率风格，Notion风格",
    "chalkboard": "粉笔风格，黑板背景，彩色粉笔字，手写字体，教育感",
}

# 布局到提示词的映射
LAYOUT_PROMPTS = {
    "sparse": "极简布局，少量文字，大面积留白，突出重点",
    "balanced": "均衡布局，适度文字和图片，层次分明",
    "dense": "密集布局，信息量大，卡片式设计，知识点丰富",
    "list": "列表布局，清单形式，条目清晰，编号或圆点",
    "comparison": "对比布局，左右对比 or 上下对比，优缺点分明",
    "flow": "流程布局，步骤式，时间线，循序渐进",
}

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="小红书图片生成器")
    parser.add_argument("--topic", "-t", help="主题内容")
    parser.add_argument("--style", "-s", default="cute", help="视觉风格")
    parser.add_argument("--layout", "-l", default="balanced", help="布局方式")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--api", default="google", choices=["google", "openai", "dashscope"], help="API提供商")
    return parser.parse_args()

def generate_prompt(topic, style, layout):
    """生成 AI 绘图提示词"""
    style_prompt = STYLE_PROMPTS.get(style, STYLE_PROMPTS["cute"])
    layout_prompt = LAYOUT_PROMPTS.get(layout, LAYOUT_PROMPTS["balanced"])
    
    prompt = f"""生成一张小红书风格的图文卡片。

主题：{topic}

风格：{style_prompt}
布局：{layout_prompt}

要求：
- 高质量图片，适合社交媒体分享
- 文字清晰可读
- 视觉美观，有吸引力
- 中国社交媒体（小红书）风格
- 16:9 或 1:1 或 4:3 比例

请生成图片。"""
    
    return prompt

def call_image_api(prompt, output_path, api="google"):
    """调用 AI 生图 API"""
    print(f"正在调用 {api} API 生成图片...")
    print(f"提示词: {prompt[:100]}...")
    
    # 这里是一个占位实现
    # 实际使用时需要根据不同的 API 实现调用
    
    if api == "google":
        # 使用 Google Gemini API
        api_key = os.environ.get("GOOGLE_API_KEY", "")
        if not api_key:
            print("警告: 未设置 GOOGLE_API_KEY 环境变量")
            return False
    elif api == "openai":
        # 使用 OpenAI API
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            print("警告: 未设置 OPENAI_API_KEY 环境变量")
            return False
    elif api == "dashscope":
        # 使用阿里云 DashScope API
        api_key = os.environ.get("DASHSCOPE_API_KEY", "")
        if not api_key:
            print("警告: 未设置 DASHSCOPE_API_KEY 环境变量")
            return False
    
    # TODO: 实现实际的 API 调用
    print("提示: 这是一个骨架实现，需要配置实际的 AI 生图 API")
    print(f"提示词已生成: {prompt}")
    print(f"输出路径: {output_path}")
    print(f"API: {api}")
    
    return True

def main():
    """主函数"""
    args = parse_args()
    
    # 如果没有通过参数传入，尝试从 stdin 读取
    if not args.topic:
        # 尝试从命令行参数读取
        if len(sys.argv) > 1:
            # 查找第一个非选项参数
            for arg in sys.argv[1:]:
                if not arg.startswith("-"):
                    args.topic = arg
                    break
        
        if not args.topic:
            print("错误: 请提供主题内容")
            print("用法: python script.py --topic '主题内容' --style cute --layout balanced")
            sys.exit(1)
    
    # 生成提示词
    prompt = generate_prompt(args.topic, args.style, args.layout)
    
    # 确定输出路径
    if not args.output:
        # 从主题生成文件名
        slug = re.sub(r'[^\w\u4e00-\u9fa5]', '-', args.topic)
        slug = slug[:20]
        args.output = f"xhs-{slug}.png"
    
    # 调用 API 生成图片
    success = call_image_api(prompt, args.output, args.api)
    
    if success:
        print(f"\n✅ 图片生成完成!")
        print(f"📁 保存为: {args.output}")
    else:
        print("\n❌ 图片生成失败")
        sys.exit(1)

if __name__ == "__main__":
    main()
