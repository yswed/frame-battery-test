# Brilliantlabs Frame AR Glasses Battery Life Testing

This project contains scripts to test and visualize battery life performance for the Brilliantlabs Frame AR glasses. It includes a script for collecting battery data and another for visualizing the results.

## Project Overview

The goal of this project is to measure and analyze the battery performance of the Brilliantlabs Frame AR glasses under different conditions. The provided scripts allow users to:

1. **Collect Battery Life Data:** `battery-test.py` collects battery performance data from the glasses.
2. **Visualize Battery Life Data:** `visualize.py` generates visualizations of the collected data for analysis.

## Environment Setup

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## How to Use

1. **Collect Battery Data**
   - Connect the Brilliantlabs Frame AR glasses to your computer.
   - Run the `battery-test.py` script to begin collecting data.
   - Data will be saved to a log file for later use.

2. **Visualize the Data**
   - Use the `visualize.py` script to generate visualizations of the collected data.
   - Make sure the path to the log file is correctly specified in the script.

## Example

Here is an example workflow for using these scripts:

1. Start by running `battery-test.py` to collect battery data:
   ```bash
   python battery-test.py --size 100
   ```

2. After data collection is complete, run `visualize.py` to generate a visualization:
   ```bash
   python visualize.py
   ```
