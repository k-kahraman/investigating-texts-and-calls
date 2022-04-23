"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_per_number_dict = {}

# For each call in calls O(N) where N is length of the calls
for call in calls:
    # If caller number doesn't exists O(1)
    if call[0] not in time_per_number_dict:
        time_per_number_dict[call[0]] = 0

    # If receiver number doesn't exists O(1)
    if call[1] not in time_per_number_dict:
        time_per_number_dict[call[1]] = 0

    # Update the number time spents
    time_per_number_dict[call[0]] += int(call[3])
    time_per_number_dict[call[1]] += int(call[3])


# Get the longest time spent number from map using values
longest_time_spent_number = max(
    time_per_number_dict, key=time_per_number_dict.get)

print(
    f"{longest_time_spent_number} spent longest time, {time_per_number_dict[longest_time_spent_number]} seconds, on the phone during September 2016.")
