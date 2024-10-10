import json
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def load_battery_data(folder):
    data_list = []
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r') as json_file:
                data = json.load(json_file)
                data_list.append(data)
    return data_list  # Corrected indentation

def plot_battery_data(data_list):
    plt.figure(figsize=(12, 8))
    max_time_minutes = 0  # To determine the range of x-axis
    for data in data_list:
        times_seconds = [entry['time'] for entry in data['data']]
        times_minutes = [t / 60 for t in times_seconds]  # Convert seconds to minutes
        battery_levels = [entry['battery_level'] for entry in data['data']]
        rectangle_size = data['rectangle_size']
        plt.plot(times_minutes, battery_levels, label=f'Size: {rectangle_size}px', marker='o')
        if times_minutes:
            max_time_minutes = max(max_time_minutes, max(times_minutes))

    plt.title('Battery Level Over Time for Different Rectangle Sizes')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Battery Level (%)')
    plt.legend(loc='best')
    plt.grid(True)

    # Set x-axis ticks at every whole minute
    x_ticks = np.arange(0, max_time_minutes + 1, 1)  # Adjust the step as needed
    plt.xticks(x_ticks)

    # Save the plot as a PNG file with higher resolution
    output_folder = 'plots'
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = os.path.join(output_folder, f'battery_plot_{timestamp}.png')
    plt.savefig(output_filename, dpi=300)
    print(f"Plot saved as {output_filename}")
    plt.close()

if __name__ == '__main__':
    battery_data_folder = 'battery_data'
    battery_data_list = load_battery_data(battery_data_folder)
    plot_battery_data(battery_data_list)
