import os
import time
import datetime
import numpy as np
import nidaqmx


def main():
    a = np.array([], dtype=np.float64)
    interval = 0.01  # [ms]
    device = "Dev2"
    channel = "ai0"
    save_path = "src"
    sampling_data = np.array([], dtype=np.float64)
    sampling_channel = "{0:s}/{1:s}".format(device, channel)
    print("analog voltage input from" + sampling_channel)
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(sampling_channel)
        while True:
            try:
                sampling_value = task.read()
                print("\r{0:15.10f}".format(sampling_value), end="")
                sampling_data = np.append(sampling_data, sampling_value)
                time.sleep(interval)
            except KeyboardInterrupt:
                file_name = os.path.join(
                    save_path,
                    "sampling_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),
                )
                print(
                    "\nSave as {0:s} length{1:d}".format(file_name, sampling_data.size)
                )
                np.save(file_name, sampling_data)
                break


if __name__ == "__main__":
    main()
