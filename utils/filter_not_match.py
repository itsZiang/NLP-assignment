import json

# Đọc file JSON chứa dữ liệu
input_files = [
    ("data_slot_filling_dev.json", "data_slot_filling_dev.json"),
    ("data_slot_filling_test.json", "data_slot_filling_test.json"),
    ("data_slot_filling_train.json", "data_slot_filling_train.json")
]

# Hàm kiểm tra tính hợp lệ của span_info
def is_valid_span(utterance, value, start, end):
    # Chuyển câu và giá trị về chữ thường để so sánh
    utterance_lower = utterance.lower()
    value_lower = value.lower()
    # Kiểm tra value có xuất hiện trong đoạn substring từ start đến end
    return utterance_lower[start:end] == value_lower

# Lặp qua từng file đầu vào
for input_file, output_file in input_files:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    filtered_data = []

    for entry in data:
        utterance = entry["utterance"]
        valid_span_info = []

        for span in entry["span_info"]:
            intent, slot_name, value, start, end = span

            if is_valid_span(utterance, value, start, end):
                valid_span_info.append(span)

        # Chỉ thêm vào danh sách kết quả nếu span_info còn dữ liệu
        if valid_span_info:
            filtered_data.append({
                "utterance": utterance,
                "span_info": valid_span_info
            })

    # Lưu kết quả đã lọc vào file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

    print(f"Filtered data saved to {output_file}")
