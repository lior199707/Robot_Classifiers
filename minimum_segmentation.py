def times(time_increment):
    # Define the initial time
    current_time = 0

    # Define the time to stop at (20:00)
    end_time = 20 * 60  # 20 minutes * 60 seconds per minute

    # Define the time increment (19 seconds)
    time_increment = time_increment
    arr = []
    # Loop to simulate jumps
    while current_time < end_time:
        # Convert the current time to mm:ss format for the start and end of the range
        start_minutes = current_time // 60
        start_seconds = current_time % 60
        end_minutes = (current_time + time_increment) // 60
        end_seconds = (current_time + time_increment) % 60

        # Format and print the time range
        time_range_str = f"{start_minutes:02}:{start_seconds:02}-{end_minutes:02}:{end_seconds:02}"
        arr.append(time_range_str)
        current_time += 1

        # Increment the current time by 19 seconds
        current_time += time_increment
    return arr

eda_time_intervals = [
    "13:20-13:23",
    "07:27-07:36",
    "14:07-14:13",
    "05:40-05:58",
    "06:09-06:15",
    "14:30-14:39",
    "04:40-04:49",
    "07:29-07:37",
    "11:24-11:30",
]
ecg_time_intervals = [
    "08:58-09:02",
    "10:57-11:06",
    "17:37-17:43",
    "05:20-05:39",
    "05:50-05:56",
    "14:11-14:20",
    "04:21-04:30",
    "07:10-07:18",
    "11:04-11:10"
]

cropped_ecg_time_intervals = [
    "08:58-09:02",
    "10:57-11:06",
    "17:37-17:43",
    "05:25-05:39",
    "05:50-05:56",
    "14:11-14:20",
    "04:21-04:30",
    "07:10-07:18",
    "11:04-11:10"
]


arr = times(21)


def in_interval(arr, time_intervals):
    # Initialize a flag to check if all times are in the intervals
    all_times_in_intervals = True

    # Loop through each time in the time_intervals list
    for time in time_intervals:
        start_time, end_time = time.split("-")
        found = False

        # Check if the time is within any of the intervals
        for interval in arr:
            start_interval, end_interval = interval.split("-")
            if start_time >= start_interval and end_time <= end_interval:
                found = True
                break

        # If the time is not found in any interval, set the flag to False and break
        if not found:
            all_times_in_intervals = False
            break

    return all_times_in_intervals

def find_intervals(time_intervals):
    flag = False
    i = 1
    while not flag:
        arr = times(i)
        flag = in_interval(arr, time_intervals)
        i += 1

    return i

print("ECG:",find_intervals(ecg_time_intervals), "EDA:",find_intervals(eda_time_intervals), "Cropped ECG:",find_intervals(cropped_ecg_time_intervals))
