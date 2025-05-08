import json
import matplotlib.pyplot as plt
from datetime import datetime

# Save the mood data to a JSON file
def save_mood(mood, note, timestamp):
    data = load_mood_data()
    data.append({"mood": mood, "note": note, "timestamp": timestamp})
    with open('mood_data.json', 'w') as f:
        json.dump(data, f)

# Load mood data from the JSON file
def load_mood_data():
    try:
        with open('mood_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Plot the mood trends using Matplotlib
def plot_mood_trends(mood_data):
    moods = [entry['mood'] for entry in mood_data]
    timestamps = [entry['timestamp'] for entry in mood_data]

    # Count occurrences of each mood
    mood_counts = {mood: moods.count(mood) for mood in set(moods)}

    # Plot a bar chart for mood trends
    plt.figure(figsize=(10, 5))
    plt.bar(mood_counts.keys(), mood_counts.values())
    plt.xlabel('Mood')
    plt.ylabel('Frequency')
    plt.title('Mood Trends')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

