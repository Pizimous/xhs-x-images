#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xhs-x-images: 小红书图片生成器
支持 Google Imagen API
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
import base64
import time

# 风格到提示词的映射
STYLE_PROMPTS = {
    "cute": "可爱甜美风格，粉色系，卡通插画风格，小红书风格，柔和光线，精致细节",
    "fresh": "清新自然风格，绿色系，清爽干净，小清新风格，自然光线，简洁设计",
    "warm": "温暖友好风格，暖色调，温馨舒适，生活感，柔和光线，温馨氛围",
    "bold": "强烈吸睛风格，高对比度，醒目大字，视觉冲击力强，时尚潮流",
    "minimal": "极简精致风格，黑白灰，简约设计，线条简洁，现代感，高级感",
    "retro": "复古怀旧风格，复古配色，怀旧元素，80/90年代，复古滤镜",
    "pop": "活泼醒目风格，鲜艳配色，波普艺术，潮流元素，充满活力",
    "notion": "简约手栏风格，白底黑线，手绘插画，知识感，效率风格",
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
    parser = argparse.ArgumentParser(description="XHS Image Generator")
    parser.add_argument("--topic", "-t", help="Topic")
    parser.add_argument("--style", "-s", default="cute", help="Style")
    parser.add_argument("--layout", "-l", default="balanced", help="Layout")
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--api-key", help="Google API Key")
    return parser.parse_args()

def generate_prompt(topic, style, layout):
    style_prompt = STYLE_PROMPTS.get(style, STYLE_PROMPTS["cute"])
    layout_prompt = LAYOUT_PROMPTS.get(layout, LAYOUT_PROMPTS["balanced"])
    
    prompt = f"""Xiaohongshu social media image card, topic: {topic}, style: {style_prompt}, layout: {layout_prompt}, high quality, professional design, Chinese text, vibrant colors, modern card layout"""
    
    return prompt

def call_imagen_api(prompt, api_key, output_path):
    print("Calling Google Imagen API to generate image...")
    
    # Use Imagen 3.0 Generate API
    url = f"https://vision.googleapis.com/v1/projects/-/locations/us-central1:predict?key={api_key}"
    
    data = {
        "instances": [{
            "prompt": prompt
        }],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9"
        }
    }
    
    json_data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"Imagen response: {json.dumps(result, indent=2, ensure_ascii=False)}")
            return False
    except urllib.error.HTTPError as e:
        print(f"Imagen HTTP Error: {e.code}")
        try:
            error_body = e.read().decode('utf-8')
            print(f"Error: {error_body}")
        except:
            pass
        return False

def call_veo_api(prompt, api_key, output_path):
    print("Calling Google Veo API to generate image...")
    
    # Veo is for video, let's use a different approach
    # Try the image generation via the predict endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key={api_key}"
    
    data = {
        "instances": [{
            "prompt": prompt
        }],
        "parameters": {
            "sampleCount": 1
        }
    }
    
    json_data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"Veo/Imagen response: {json.dumps(result, indent=2, ensure_ascii=False)}")
            return False
    except urllib.error.HTTPError as e:
        print(f"Veo HTTP Error: {e.code}")
        try:
            error_body = e.read().decode('utf-8')
            print(f"Error: {error_body}")
        except:
            pass
        return False

def call_gemini_vision(prompt, api_key, output_path):
    """Try using Gemini with vision to describe/create an image concept"""
    print("Using Gemini to analyze/create image concept...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    # Ask Gemini to create a detailed image prompt
    analysis_prompt = f"""Create a detailed prompt for an AI image generator to create a Xiaohongshu (Chinese social media) style image card.

Topic: {prompt}

Create a prompt that describes:
- The visual composition
- Colors and style
- Text layout
- Overall mood

Respond ONLY with the image generation prompt, nothing else."""

    data = {
        "contents": [{
            "parts": [{
                "text": analysis_prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.9,
            "maxOutputTokens": 1024
        }
    }
    
    json_data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    for part in candidate['content']['parts']:
                        if 'text' in part:
                            print(f"Gemini's image prompt:\n{part['text']}")
                            return True
            
            print(f"Response: {json.dumps(result, indent=2)}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    args = parse_args()
    
    api_key = args.api_key or os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        print("Error: Please provide Google API Key")
        sys.exit(1)
    
    if not args.topic:
        if len(sys.argv) > 1:
            for arg in sys.argv[1:]:
                if not arg.startswith("-"):
                    args.topic = arg
                    break
        
        if not args.topic:
            print("Error: Please provide topic")
            sys.exit(1)
    
    prompt = generate_prompt(args.topic, args.style, args.layout)
    print(f"Topic: {args.topic}")
    print(f"Style: {args.style}")
    print(f"Layout: {args.layout}")
    print(f"Prompt: {prompt}")
    
    if not args.output:
        clean_topic = ''.join(c for c in args.topic if c.isalnum() or c in ' -_').strip()[:20]
        args.output = f"xhs-{clean_topic}.png"
    
    print("\n--- Trying different APIs ---\n")
    
    # Try different approaches
    success = call_gemini_api_v2(prompt, api_key, args.output)
    
    if success:
        print("\n[OK] Image generated!")
    else:
        print("\n[INFO] Let me try Gemini to create an image prompt...")
        call_gemini_vision(prompt, api_key, args.output)
        print("\n[INFO] Note: This API key may not have image generation enabled.")
        print("Please check Google Cloud Console to enable Gemini image generation API.")

def call_gemini_api_v2(prompt, api_key, output_path):
    """Try gemini-2.5-flash-image model"""
    print("Trying gemini-2.5-flash-image model...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={api_key}"
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    json_data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode('utf-8'))
            
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    for part in candidate['content']['parts']:
                        if 'inlineData' in part:
                            image_data = part['inlineData']['data']
                            img_bytes = base64.b64decode(image_data)
                            with open(output_path, 'wb') as f:
                                f.write(img_bytes)
                            print(f"Image saved to: {output_path}")
                            return True
                        elif 'text' in part:
                            print(f"Response: {part['text']}")
            
            print(f"Response: {json.dumps(result, indent=2)}")
            return False
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        try:
            error_body = e.read().decode('utf-8')
            print(f"Error: {error_body}")
        except:
            pass
        return False

if __name__ == "__main__":
    main()
