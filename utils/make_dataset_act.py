import json
import os

# Initialize datasets for dialogue act detection
data_act_detection_train = []
data_act_detection_dev = []
data_act_detection_test = []

# Define the directory paths for train, dev, and test
directories = {
    "train": "./train",  # Replace with your actual directory path
    "dev": "./dev",      # Replace with your actual directory path
    "test": "./test"     # Replace with your actual directory path
}

# Function to process JSON files and extract data
def process_data(directory, dataset):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            with open(file_path, "r") as utter_file:
                utterance_data = json.load(utter_file)

            # Assuming dialog acts data is consistent and already loaded or available globally
            with open("dialog_acts.json", "r") as act_file:
                dialogue_act_data = json.load(act_file)

            # Process each dialogue
            for dialogue in utterance_data:
                dialogue_id = dialogue["dialogue_id"]
                turns = dialogue["turns"]

                for turn in turns:
                    turn_id = turn["turn_id"]
                    utterance = turn["utterance"]

                    # Retrieve the dialogue acts for this turn
                    dialogue_acts = dialogue_act_data.get(dialogue_id, {}).get(turn_id, {}).get("dialog_act", {})
                    # Prepare data for Dialogue Act Detection
                    acts = list(dialogue_acts.keys())
                    dataset.append({
                        "utterance": utterance,
                        "acts": acts
                    })

# Process data for each set (train, dev, test)
process_data(directories["train"], data_act_detection_train)
process_data(directories["dev"], data_act_detection_dev)
process_data(directories["test"], data_act_detection_test)

# Save the processed data to respective JSON files
with open("data_act_detection_train.json", "w") as train_file:
    json.dump(data_act_detection_train, train_file, indent=4)

with open("data_act_detection_dev.json", "w") as dev_file:
    json.dump(data_act_detection_dev, dev_file, indent=4)

with open("data_act_detection_test.json", "w") as test_file:
    json.dump(data_act_detection_test, test_file, indent=4)

print("Datasets created:")
print("- data_act_detection_train.json")
print("- data_act_detection_dev.json")
print("- data_act_detection_test.json")
