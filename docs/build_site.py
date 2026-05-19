#!/usr/bin/env python3
"""Build multi-page AUTOSAR book site with navigation sidebar."""

import re

# Read the source HTML
with open('/home/mark/.openclaw/workspace/docs/AUTOSAR_中文版.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the body content (everything inside <body>...</body>)
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
body = body_match.group(1)

# Find all chapter boundaries
chapters_raw = re.split(r'(\s*<!-- Chapter \d+ -->\s*)', body)

# The first item is everything before Chapter 1 (cover + TOC)
preamble = chapters_raw[0]

# Extract chapter info
chapter_info = []
for i in range(1, len(chapters_raw), 2):
    comment = chapters_raw[i]
    content = chapters_raw[i+1] if i+1 < len(chapters_raw) else ''
    # Get chapter number from comment
    ch_num = re.search(r'Chapter (\d+)', comment).group(1)
    chapter_info.append((int(ch_num), content))

# Chapter titles mapping
chapter_titles = {
    1: '探索 AUTOSAR 的起源与目标',
    2: 'AUTOSAR 软件层简介',
    3: 'AUTOSAR 方法论与数据交换格式',
    4: '使用软件组件与 RTE',
    5: '设计与实现事件和接口',
    6: 'AUTOSAR 操作系统入门',
    7: '探索通信栈',
    8: '使用 Crypto 与安全栈保护 AUTOSAR 系统',
    9: '内存与模式管理',
    10: '总结与知识拓展用例',
}

# We need to fix the H1 titles for chapters that have mismatched ones
# (Some <h1> tags in the content don't match the chapter title exactly due to book structure)

# We'll keep the original H1 from content but override if needed
# Based on my reading, chapters 4, 5, 6, 8 have alternate chapter titles inside the content
# due to the book's structure (previous chapter summary section bleeds into next chapter).

# Actually, looking more carefully at the structure:
# - ch04 starts at "第4章 使用软件组件与 RTE" but the actual h1 in content is "第4章 使用软件组件与 RTE"
# - ch05 starts at "第5章 设计与实现事件和接口" - Content has that as h1
# - ch06 starts at "第6章 AUTOSAR 操作系统入门" - Content has "第6章 AUTOSAR 操作系统入门" as h1
# - ch07 starts at "第7章 探索通信栈" - Content has "第7章 探索通信栈" as h1
# - ch08 starts at "第8章 使用 Crypto 与安全栈保护 AUTOSAR 系统" - Content has that as h1
# - ch09 starts at "第9章 内存与模式管理" - Content has "第9章 内存与模式管理" as h1
# - ch10 starts at "第10章 总结与知识拓展用例" - Content has "第10章 总结与知识拓展用例" as h1

# The content within each chapter already has its own <h1>. Good.

# But we need to fix ch04 - let me check... Looking at line 1162-1165:
# <!-- Chapter 4 -->
# <div class="chapter-page">
# <div class="container">
# <h1>第4章 使用软件组件与 RTE</h1>
# Good, fine.

# Note: ch08 has inline CSS styles. We need to handle this - strip the container-specific styles
# and use our common stylesheet approach.

# Navigation HTML template
def nav_html(current_ch):
    items = []
    for num in range(1, 11):
        title = chapter_titles[num]
        active = ' active' if num == current_ch else ''
        items.append(f'        <li><a href="ch{num:02d}.html" class="nav-chapter{active}">第{num}章 {title}</a></li>')
    return '\n'.join(items)

def generate_page(ch_num, content, current_ch):
    """Generate a complete HTML page for a chapter."""
    title = chapter_titles[ch_num]
    
    # For chapter 8, strip inline styles (they'll be handled by our global CSS)
    if ch_num == 8:
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    # Strip the outer <div class="chapter-page"> wrapper from the source content
    # since our template already provides one.
    content = re.sub(r'^\s*<div class="chapter-page">\s*', '', content)
    content = re.sub(r'\s*</div>\s*$', '', content)
    
    page = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第{ch_num}章 {title} — AUTOSAR 基础与应用</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="sidebar">
  <div class="sidebar-header">
    <a href="index.html" class="book-title">AUTOSAR 基础与应用</a>
  </div>
  <nav class="nav-list">
    <ul>
{nav_html(current_ch)}
    </ul>
  </nav>
</div>

<button class="sidebar-toggle" onclick="toggleSidebar()" aria-label="切换导航">☰</button>

<div class="main-content">
  <div class="chapter-page">
{content.strip()}
  </div>
</div>

<script src="scripts.js"></script>
</body>
</html>'''
    return page


# Generate index.html
def generate_index():
    toc_items = []
    for num in range(1, 11):
        title = chapter_titles[num]
        toc_items.append(f'''        <div class="toc-item">
          <a href="ch{num:02d}.html">
            <span class="toc-chapter">第{num}章</span>
            <span class="toc-title">{title}</span>
          </a>
        </div>''')
    
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AUTOSAR 基础与应用</title>
<link rel="stylesheet" href="styles.css">
</head>
<body class="index-page">
  <div class="index-container">
    <div class="book-cover">
      <div class="cover-badge">中文版</div>
      <h1 class="cover-title">AUTOSAR 基础与应用</h1>
      <p class="cover-subtitle">AUTOSAR Fundamentals and Applications</p>
      <div class="cover-divider"></div>
      <div class="cover-authors">
        <p>原著：Dhanabal Kamatchi · Indhumathi Sundarasamy · Nandhini Ganesan</p>
        <p>Dinesh Kumar · Basu Dev Shivahare · K. Senthilvadivu</p>
      </div>
      <div class="cover-translator">
        <p>AI 辅助翻译</p>
        <p>翻译完成：2026年5月</p>
      </div>
    </div>
    
    <div class="toc-section">
      <h2 class="toc-heading">目 录</h2>
      <div class="toc-list">
{''.join(toc_items)}
      </div>
    </div>
    
    <footer class="index-footer">
      <p>本书共10章，涵盖 AUTOSAR Classic Platform 的核心概念与实践</p>
    </footer>
  </div>
</body>
</html>'''


# Process each chapter and write files
for ch_num, content in chapter_info:
    page = generate_page(ch_num, content, ch_num)
    filename = f'/home/mark/.openclaw/workspace/docs/ch{ch_num:02d}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'Generated {filename} ({len(page)} chars)')

# Write index.html
index_html = generate_index()
with open('/home/mark/.openclaw/workspace/docs/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print(f'Generated index.html ({len(index_html)} chars)')

print('Done!')
