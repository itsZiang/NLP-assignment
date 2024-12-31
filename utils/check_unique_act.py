import json

# Function to read the JSON file and extract unique dialog acts
def get_unique_dialog_acts_from_file(file_path):
    # Load the data from the JSON file
    with open(file_path, 'r') as file:
        dialogue_act_data = json.load(file)
    
    unique_dialog_acts = set()
    
    # Iterate through the nested dictionary to extract dialog acts
    for dialogue_id, turns in dialogue_act_data.items():
        for turn_id, data in turns.items():
            # Retrieve dialog act keys for each turn
            dialog_acts = data.get("dialog_act", {}).keys()
            unique_dialog_acts.update(dialog_acts)
    
    return unique_dialog_acts

# Specify the path to the dialogue act data file
file_path = "dialog_acts.json"  # Replace with the actual file path

# Get unique dialog acts from the file
unique_acts = get_unique_dialog_acts_from_file(file_path)

# Write the unique dialog acts to a text file
output_file_path = "acts_name.txt"  # Output text file path
with open(output_file_path, 'w') as output_file:
    # Write each dialog act on a new line
    for act in unique_acts:
        output_file.write(f"{act}\n")

print(f"Unique dialog acts have been written to {output_file_path}")
