import xmltodict
import json
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# XML文件路径
xml_file_path = None

# 读取XML文件，确保使用UTF-8编码
def read_xml_file():
    global xml_file_path
    xml_file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if xml_file_path:
        with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
            xml_content = xml_file.read()
        return xml_content
    return None

# 将XML内容转换为Python字典
def parse_xml_to_dict(xml_content):
    return xmltodict.parse(xml_content, encoding='utf-8')

# 筛选数据
def filter_event_memory(data):
    results = []
    for ecu in data['protocol']['vehicle']['communications']['ecus']['ecu']:
        ecu_master_list = ecu.get('ecu_master', [])
        for item in ecu_master_list:
            if isinstance(item, dict) and '@type' in item:
                if item['@type'] == 'event_memory':
                    event_memory = {
                        'ecu_id': ecu['ecu_id'],
                        'ecu_name': ecu['ecu_name'],
                        'display_name': item['display_name'],
                        'errors': []
                    }
                    if 'values' in item and isinstance(item['values'], list):
                        for value in item['values']:
                            if isinstance(value, dict):
                                event_error = {
                                    'ti_name': value.get('ti_name', ''),
                                    'display_name': value.get('display_name', ''),
                                    'fault_number': value.get('fault_number', ''),
                                    'hex_fault_number': value.get('hex_fault_number', ''),
                                    'sae_number': value.get('sae_number', ''),
                                    'dtc_text': value.get('dtc_text', 'not Available')
                                }
                                event_memory['errors'].append(event_error)
                    results.append(event_memory)
    return results

# 执行筛选操作并保存为JSON文件
def process_xml_and_save_json(xml_content):
    global xml_file_path
    if xml_content:
        dict_data = parse_xml_to_dict(xml_content)
        filtered_results = filter_event_memory(dict_data)
        return save_json(filtered_results)

# 将筛选结果保存为JSON文件，确保使用UTF-8编码
def save_json(data):
    global xml_file_path
    base_name = os.path.basename(xml_file_path)
    new_name = base_name.split('.')[0] + '.JSON'
    output_json_path = os.path.join(os.path.dirname(xml_file_path), new_name)
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    return output_json_path

# 创建GUI
def create_gui(root):
    root.title("XML to JSON Converter")
    root.geometry("300x150")

    button = tk.Button(root, text="Select XML File", command=lambda: handle_button_click(root))
    button.pack(pady=20)

def handle_button_click(root):
    xml_content = read_xml_file()
    if xml_content:
        output_json_path = process_xml_and_save_json(xml_content)
        if output_json_path:
            messagebox.showinfo("Success", f"JSON file has been saved to: {output_json_path}")
            root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root)
    root.mainloop()
