---
name: paper-reader
description: 当用户需要处理PDF论文文件时使用此skill：提取PDF论文的文字内容；对论文进行结构化解析（提取基础信息、实验设计、核心结果、结论等）；将论文转换为Markdown格式的结构化报告；批量处理论文文件。功能：提取PDF文本并生成包含基本信息、实验设计、核心结果、结论的Markdown报告，完成后删除临时文件仅保留报告。
---

# Paper Reader Skill

## 功能概述

本skill用于：
1. 提取PDF论文的完整文本内容
2. 按照标准化格式对论文进行结构化解析
3. 生成包含基本信息、实验设计、核心结果、结论与创新点的Markdown报告
4. 清理临时文件，仅保留最终报告

## 工作流程

### Step 1: 检查Python环境

```bash
# 检查虚拟环境是否存在
if [ ! -d ".venv" ]; then
    uv venv
fi

# 激活虚拟环境
source .venv/bin/activate
```

### Step 2: 检查并安装依赖

```bash
# 使用skill提供的脚本检查依赖
uv run python .claude/skills/paper-reader/scripts/check_deps.py
```

或手动安装：
```bash
uv pip install pdfplumber -q
```

### Step 3: 提取PDF文本

```bash
# 使用skill提供的脚本提取PDF文本
uv run python .claude/skills/paper-reader/scripts/extract_pdf.py <pdf_path> <output_txt_path>
```

### Step 4: 结构化解析

读取提取的文本，按照reference文件的要求进行结构化解析：

1. **基本信息** → 参考 `references/01-basic-info.md`
2. **实验设计** → 参考 `references/02-experimental-design.md`
3. **核心结果** → 参考 `references/03-core-results.md`
4. **结论与创新点** → 参考 `references/04-conclusion.md`
5. **技术路线** → 参考 `references/05-technical-roadmap.md`

### Step 5: 生成报告

将解析结果保存为Markdown文件：
```
paper-reader—[论文标题].md
```

### Step 6: 清理临时文件

```bash
# 删除临时提取的文本文件
rm <output_txt_path>
```

## 完整工作流程示例

```bash
# 1. 确保Python环境就绪
if [ ! -d ".venv" ]; then uv venv; fi
source .venv/bin/activate

# 2. 检查并安装依赖
uv run python .claude/skills/paper-reader/scripts/check_deps.py

# 3. 提取PDF文本（临时文件与PDF同目录）
uv run python .claude/skills/paper-reader/scripts/extract_pdf.py \
    "paper.pdf" \
    "paper_extract_temp.txt"

# 4. 分析文本并生成结构化报告（此步骤由Claude完成）
# 读取 paper_extract_temp.txt
# 按照reference文件要求进行结构化解析
# 生成 paper-reader—[标题].md

# 5. 清理临时文件
rm paper_extract_temp.txt
```

## Reference文件清单

| 文件 | 用途 |
|------|------|
| `references/01-basic-info.md` | 基本信息提取要求 |
| `references/02-experimental-design.md` | 实验设计要求 |
| `references/03-core-results.md` | 核心结果提取要求 |
| `references/04-conclusion.md` | 结论与创新点要求 |
| `references/05-technical-roadmap.md` | 技术路线要求 |

## Scripts清单

| 文件 | 用途 |
|------|------|
| `scripts/extract_pdf.py` | 提取PDF文本 |
| `scripts/check_deps.py` | 检查并安装依赖 |

## 依赖项

- Python 3.10+
- uv (Python包管理器)
- pdfplumber (PDF文本提取)

## 关键要求

1. **使用uv管理依赖**：始终使用 `uv pip install` 而非直接使用 pip
2. **虚拟环境**：所有Python操作在虚拟环境中执行
3. **原文出处标注**：所有结论必须标注原文位置
4. **技术路线中文**：技术路线树状图全部使用中文
5. **文件清理**：处理完成后删除临时文本文件，仅保留最终Markdown报告
6. **准确性**：要求报告严谨，及其准确，完全基于文档内容作答，不允许有任何编造