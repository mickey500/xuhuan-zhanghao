import os
import re

# 指定目录路径
directory = '/Users/mikey/Documents/OB/mikey/004_B站/尚硅谷-禹神/vue3+TypeScript'

# 遍历目录下的所有 HTML 文件
for filename in os.listdir(directory):
    if filename.endswith('.md'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            html_content = file.read()
        # 使用正则表达式匹配 img 元素
        img_regex = r'<img src="(.+?)"(.*)>'
        img_matches = re.findall(img_regex, html_content)
        # 替换为 Markdown 图片
        for img_match in img_matches:
            markdown_image = '![alt text](' + img_match[0] + ')'
            html_content = html_content.replace(
                '<img src="' + img_match[0] + '"' + img_match[1] + '>', markdown_image)
        # 保存替换后的内容
        with open(file_path, 'w') as file:
            file.write(html_content)
