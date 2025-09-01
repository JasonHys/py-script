import json
import os
import pandas as pd

# 多语言 JSON 文件所在目录
i18n_dir = "./json"
# 输出的 Excel 文件
output_excel = "./out/langs.xlsx"

# 扫描目录下的所有 json 文件
lang_files = [f for f in os.listdir(i18n_dir) if f.endswith(".json")]

# 读取所有语言 JSON
langs_data = {}
for file in lang_files:
    lang_code = os.path.splitext(file)[0]  # 文件名作为语言代码，比如 zh-CN
    with open(os.path.join(i18n_dir, file), "r", encoding="utf-8") as f:
        langs_data[lang_code] = json.load(f)

# 获取所有 key（去重）
all_keys = set()
for lang, data in langs_data.items():
    all_keys.update(data.keys())

# 构建 DataFrame
rows = []
for key in sorted(all_keys):
    row = {"key": key}
    for lang in langs_data:
        row[lang] = langs_data[lang].get(key, "")
    rows.append(row)

df = pd.DataFrame(rows)

# 保存到 Excel
df.to_excel(output_excel, index=False)

print(f"✅ 已生成 {output_excel}")
