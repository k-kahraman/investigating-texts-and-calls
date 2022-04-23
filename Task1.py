"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Sets can't have duplicates
numbers_set = set()

# For each text in texts, runtime here is O(N) where N is length of the texts
for text in texts:
    # Add to set, adding element to set is O(1) in averate (https://wiki.python.org/moin/TimeComplexity)
    numbers_set.add(text[0])
    numbers_set.add(text[1])


# For each call in calls, runtime here is O(M) where M is length of the calls
for call in calls:
    numbers_set.add(call[0])
    numbers_set.add(call[1])


# Overall runtime is O(N + M)
print(
    f"There are {len(numbers_set)} different telephone numbers in the records.")
