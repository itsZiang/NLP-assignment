import os
import json

# Hàm đọc tất cả các file JSON trong một thư mục
def read_all_json_files_in_folder(folder_path):
    data = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                data.extend(json.load(f))  # Nối dữ liệu từ mỗi file
    return data

# Đọc file JSON chứa dialogue acts và span_info
with open('dialog_acts.json', 'r', encoding='utf-8') as f:
    data_dialogue_acts = json.load(f)

# Danh sách các thư mục và tệp đầu ra
folders = {
    "dev": "data_slot_filling_dev.json",
    "train": "data_slot_filling_train.json",
    "test": "data_slot_filling_test.json"
}

# Xử lý từng thư mục và xuất kết quả
for folder_name, output_file in folders.items():
    folder_path = os.path.join(folder_name)  # Đường dẫn thư mục
    data_utterances = read_all_json_files_in_folder(folder_path)
    extracted_data = []

    # Quá trình xử lý dữ liệu
    for dialogue in data_utterances:
        dialogue_id = dialogue['dialogue_id']
        
        for turn in dialogue['turns']:
            turn_id = turn['turn_id']
            utterance = turn['utterance']
            
            # Lấy thông tin span_info từ data_dialogue_acts
            span_info = data_dialogue_acts.get(dialogue_id, {}).get(str(turn_id), {}).get("span_info", [])
            
            # Chỉ thêm dữ liệu nếu span_info không rỗng
            if span_info:
                entry = {
                    "utterance": utterance,
                    "span_info": span_info
                }
                extracted_data.append(entry)

    # Lưu kết quả vào file JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)

    print(f"Data has been saved to {output_file}")
