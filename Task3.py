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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# ===== Constants =====
BANGLORE_AREA_CODE = "(080)"
TELEMARKETER_CODE = "140"
MOBILE_PHONE_CODE_LENGTH = 4
# =====================

# ===== Part A ======
banglore_call_receivers_code = set()

for call in calls:
    # If call is not from a Banglore continue
    if not call[0].startswith(BANGLORE_AREA_CODE):
        continue

    # Access to number only once
    receiver_number = call[1]

    # This means receiver is a mobile phone
    if " " in receiver_number:
        banglore_call_receivers_code.add(receiver_number.split(" ")[
                                         0][:MOBILE_PHONE_CODE_LENGTH])
    # If receiver is a fixed line
    elif receiver_number.startswith("("):
        area_code = receiver_number.split(")")[0] + ")"
        banglore_call_receivers_code.add(area_code)

    # If receiver is a telemarketer
    elif receiver_number.startswith(TELEMARKETER_CODE):
        banglore_call_receivers_code.add(TELEMARKETER_CODE)


sorted_code_list = sorted(list(banglore_call_receivers_code))

print("The numbers called by people in Bangalore have codes:")
for code in sorted_code_list:
    print(code)

# ===================

# ===== Part B ======
call_to_any = 0
call_to_banglore = 0

for call in calls:
    if not call[0].startswith(BANGLORE_AREA_CODE):
        continue

    # Increment call to banglore if only receiver is from Banglore
    if call[1].startswith(BANGLORE_AREA_CODE):
        call_to_banglore += 1

    # Increment call to any at all cases
    call_to_any += 1


# Calculating the percentage
percentage = (call_to_banglore / call_to_any) * 100


print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    "%.2f" % percentage))
# ===================
