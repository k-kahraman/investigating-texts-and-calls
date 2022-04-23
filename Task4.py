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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

caller_numbers = set()         # Caller numbers
call_receiver_number = set()   # Call receiver number
texter_number = set()          # Texter number
text_receiver_numbers = set()  # Text receiver numbers


# For each call in calls, runtime here is O(N) where N is number of calls
for call in calls:
    # Get caller number O(1)
    caller_numbers.add(call[0])
    # Get call receiver number O(1)
    call_receiver_number.add(call[1])


# For each text in texts, runtime here is O(M) where M is number of calls
for text in texts:
    # Get texter number
    texter_number.add(text[0])
    # Get text receiver number
    text_receiver_numbers.add(text[1])


# To filter out telemarketers we are extracting common members of;
# Call receiver cause telemarketers won't receive calls,
# Texters we know that telemarketers only call,
# Text receivers because telemarketers wont receive any text message,
telemarketer_numbers = sorted(list(caller_numbers -
                       (call_receiver_number | texter_number | text_receiver_numbers)))
print("These numbers could be telemarketers: ")
for telemarketer in telemarketer_numbers:
    print(telemarketer)
