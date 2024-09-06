import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import os


# 定义一个函数来导出数据到JSON文件
def export_to_json(df, key_col, value_col, output_file):
    data_dict = {}
    for index, row in df.iterrows():
        key = str(row[key_col]).strip()
        value = str(row[value_col]).strip()
        data_dict[key] = value

    json_data = json.dumps(data_dict, ensure_ascii=False, indent=4)
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print(f"Excel数据已成功导出为{output_file}格式。")


# 处理xlsx文件并导出为JSON
def process_and_export_xlsx(excel_file, output_dir, json_file1, json_file2):
    try:
        df = pd.read_excel(excel_file)

        # 构建完整的JSON文件路径
        json_file1_path = os.path.join(output_dir, json_file1)
        json_file2_path = os.path.join(output_dir, json_file2)

        # 导出第一列和第三列数据到json_file1
        export_to_json(df, 0, 2, json_file1_path)
        # 导出第一列和第五列数据到json_file2
        export_to_json(df, 0, 4, json_file2_path)

        messagebox.showinfo("成功", "JSON文件已成功创建！")
    except Exception as e:
        messagebox.showerror("错误", f"处理xlsx文件或导出JSON时出错: {e}")


# GUI处理函数
def on_submit():
    global xlsx_file
    # 选择xlsx文件
    xlsx_file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not xlsx_file:
        return
    select_label.config(text=xlsx_file)


def execute():
    global xlsx_file
    json_file1 = pt.get()
    json_file2 = eng.get()
    output_dir = out_label.cget("text")

    # 检查是否选择了xlsx文件
    if not xlsx_file:
        messagebox.showwarning("警告", "请先选择一个Excel文件")
        return

    # 检查是否设置了输出目录
    if not output_dir:
        messagebox.showwarning("警告", "请选择有效的目录")
        return

    # 执行文件处理和导出
    process_and_export_xlsx(xlsx_file, output_dir, json_file1, json_file2)


def select_out_file():
    output_dir = filedialog.askdirectory(title="选择保存JSON文件的目录")
    out_label.config(text=output_dir)


# 创建GUI
def create_gui():
    global eng
    global pt
    global select_label
    global out_label
    global xlsx_file
    xlsx_file = None

    root = tk.Tk()
    root.title("语言包转化工具")
    root.geometry("400x400")

    tk.Label(root, text="点击按钮选择xlsx文件并选择保存JSON文件的目录").pack(pady=10)

    # pt
    left_frame = tk.Frame(root)
    left_frame.pack(pady=10)
    tk.Label(left_frame, text="葡萄牙语文件名：").pack(side=tk.LEFT)
    pt = tk.Entry(left_frame)
    pt.insert(0, "pt.json")
    pt.pack()

    # en
    right_frame = tk.Frame(root)
    right_frame.pack(pady=10)
    tk.Label(right_frame, text="英语文件名：").pack(side=tk.LEFT)
    eng = tk.Entry(right_frame)
    eng.insert(0, "eng.json")
    eng.pack()

    # 选择文件
    select_frame = tk.Frame(root)
    select_frame.pack(pady=10)
    select_label_title = tk.Label(select_frame, text="选择的文件名地址：")
    select_label_title.pack(side=tk.LEFT)
    select_label = tk.Label(select_frame, text="")
    select_label.pack()
    tk.Button(root, text="选择xlsx文件", command=on_submit).pack()

    # 输入文件
    out_frame = tk.Frame(root)
    out_frame.pack(pady=10)
    out_label_title = tk.Label(out_frame, text="选择文件目录：")
    out_label_title.pack(side=tk.LEFT)
    out_label = tk.Label(out_frame, text="")
    out_label.pack()
    tk.Button(root, text="选择输出文件目录", command=select_out_file).pack(pady=10)

    tk.Button(root, text="执行", command=execute).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
