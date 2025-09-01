import pandas as pd
import os
import json

# 输入 Excel 文件
excel_file = "langs.xlsx"
# 输出目录
output_dir = "./out"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取 Excel
df = pd.read_excel(excel_file)

# 第一列必须是 key
if "key" not in df.columns:
    raise ValueError("Excel 文件必须包含 'key' 列")

# 获取所有语言列（除 key 外）
languages = [col for col in df.columns if col != "key"]

# 按语言生成 JSON 文件
for lang in languages:
    lang_dict = {}
    for _, row in df.iterrows():
        lang_dict[row["key"]] = row[lang] if pd.notna(row[lang]) else ""

    output_path = os.path.join(output_dir, f"{lang}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(lang_dict, f, ensure_ascii=False, indent=2)

    print(f"✅ 已生成 {output_path}")
