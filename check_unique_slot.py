import json

def extract_unique_slots(data_files):
    """
    Extract unique slots from multiple JSON files and count their occurrences
    """
    unique_slots = set()
    slot_counts = {}
    
    # Process each data file
    for file_path in data_files:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        # Process each entry
        for entry in data:
            acts = entry['acts']
            # Go through each dialog act
            for act_slots in acts.values():
                # Add each slot to our set and count occurrences
                for slot in act_slots.keys():
                    unique_slots.add(slot)
                    slot_counts[slot] = slot_counts.get(slot, 0) + 1
    
    return unique_slots, slot_counts

def main():
    # Define input files
    data_files = [
        "out/data_slot_filling_train.json",
        "out/data_slot_filling_dev.json",
        "out/data_slot_filling_test.json"
    ]
    
    # Extract unique slots and their counts
    unique_slots, slot_counts = extract_unique_slots(data_files)
    
    # Sort slots by frequency (most common first)
    sorted_slots = sorted(slot_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Write results to output file
    with open("slots_name.txt", "w") as f:
        f.write(f"Total unique slots found: {len(unique_slots)}\n\n")
        f.write("Slots and their frequencies:\n")
        f.write("-" * 40 + "\n")
        for slot, count in sorted_slots:
            f.write(f"{slot}: {count}\n")
        
        f.write("\n\nAlphabetical list of unique slots:\n")
        f.write("-" * 40 + "\n")
        for slot in sorted(unique_slots):
            f.write(f"{slot}\n")

if __name__ == "__main__":
    main()