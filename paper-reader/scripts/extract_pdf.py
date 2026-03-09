#!/usr/bin/env python3
"""
提取PDF文本的脚本
用法: python extract_pdf.py <pdf_path> [output_path]
"""

import sys
import pdfplumber


def extract_pdf_text(pdf_path):
    """提取PDF所有页面的文本内容"""
    text_parts = []

    with pdfplumber.open(pdf_path) as pdf:
        text_parts.append(f"PDF共有 {len(pdf.pages)} 页\n")
        text_parts.append("=" * 80)

        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            text_parts.append(f"\n--- 第 {i+1} 页 ---\n")
            text_parts.append(page_text if page_text else "[本页无文本内容]")
            text_parts.append("\n")

    return "\n".join(text_parts)


def main():
    if len(sys.argv) < 2:
        print("用法: python extract_pdf.py <pdf_path> [output_path]", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        text = extract_pdf_text(pdf_path)

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"文本已保存至: {output_path}")
        else:
            print(text)

    except FileNotFoundError:
        print(f"错误: 找不到文件 '{pdf_path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
