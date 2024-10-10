import asyncio
import json
import argparse
import os
import time
from datetime import datetime
from frame_sdk import Frame
from frame_sdk.display import Alignment

async def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Battery Life Test with Variable Rectangle Size')
    parser.add_argument('--size', type=int, required=True, help='Size of the rectangles (width and height, equal)')
    args = parser.parse_args()
    rectangle_size = args.size

    # Prepare output folder
    output_folder = 'battery_data'
    os.makedirs(output_folder, exist_ok=True)

    # Generate a unique filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    json_filename = f'battery_data_{rectangle_size}px_{timestamp}.json'
    json_filepath = os.path.join(output_folder, json_filename)

    # Connect to the Frame device
    async with Frame() as f:
        print(f"Connected: {f.bluetooth.is_connected()}")
        width = rectangle_size/4  # Width of each rectangle
        height = rectangle_size/4  # Height of each rectangle
        offset = 0  # Starting offset

        battery_data = {
            "rectangle_size": rectangle_size,
            "data": []
        }  # Dictionary to store battery levels and timestamps along with rectangle size
        iteration = 0  # Initialize iteration count

        while True:
            loop_start_time = time.perf_counter()  # Start time of loop

            # Calculate elapsed time based on iteration count
            elapsed_time = iteration * 5

            # Get battery level
            battery_level = await f.get_battery_level()
            print(f"Time: {elapsed_time}s, Frame battery: {battery_level}%")

            # Append data to the list
            battery_data["data"].append({
                "time": elapsed_time,
                "battery_level": battery_level
            })

            # Write the battery data to a JSON file
            with open(json_filepath, 'w') as json_file:
                json.dump(battery_data, json_file, indent=4)

            # Loop through all 16 colors
            for color in range(0, 16):
                tile_x = (color % 4)  # Column position
                tile_y = (color // 4)  # Row position
                # Draw the rectangle with current offset
                await f.display.draw_rect(
                    tile_x * width + 1 + offset,
                    tile_y * height + 1,
                    width,
                    height,
                    color
                )
            await f.display.show()  # Update the display

            # Measure execution time
            loop_end_time = time.perf_counter()
            execution_time = loop_end_time - loop_start_time

            # Calculate sleep time to maintain exact 5-second intervals
            sleep_time = 5 - execution_time
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)
            else:
                print(f"Warning: Loop execution exceeded 5 seconds by {-sleep_time:.2f} seconds.")

            # Switch the offset for the next iteration
            offset = 100 if offset == 0 else 0

            # Increment iteration count
            iteration += 1

            # Optionally, stop when battery reaches a certain level
            if battery_level <= 0:
                print("Battery depleted. Exiting.")
                break

if __name__ == '__main__':
    asyncio.run(main())
