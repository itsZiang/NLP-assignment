import json
import matplotlib.pyplot as plt
from collections import Counter

# Load the training data
with open("out/data_act_detection_train.json", "r") as file:
    data = json.load(file)

# Extract all acts from the data
all_acts = []
for entry in data:
    all_acts.extend(entry["acts"])

# Count the frequency of each act
act_counts = Counter(all_acts)

# Separate the acts and their counts for plotting
acts = list(act_counts.keys())
counts = list(act_counts.values())

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.bar(acts, counts, color='skyblue')
plt.xlabel("Dialogue Acts")
plt.ylabel("Frequency")
plt.title("Histogram of Dialogue Act Frequencies")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the histogram image
output_image_path = "dialogue_act_histogram.png"
plt.savefig(output_image_path)
plt.show()

print(f"Histogram saved to {output_image_path}")