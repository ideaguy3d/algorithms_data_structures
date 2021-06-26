"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import pprint

pretty = pprint.PrettyPrinter(indent=4).pprint

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
these are numbers that make outgoing calls but 
        - never send texts,
        - receive texts or 
        - receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# call indexes
c_calling_num = 0
c_receiving_num = 1
c_start_time = 2
c_duration = 3
# text indexes
t_sending_num = 0
t_receiving_num = 1
t_timestamp = 2
telemarketer_ds = {
    'sent_text': set(),
    'received_text': set(),
    'made_call': set(),
    'received_call': set()
}

for c in calls:
    telemarketer_ds['received_call'].add(c[c_receiving_num])
    telemarketer_ds['made_call'].add(c[c_calling_num])

for t in texts:
    telemarketer_ds['sent_text'].add(t[t_sending_num])
    telemarketer_ds['received_text'].add(t[t_receiving_num])

"""
- never send texts
- never receive texts  
- never receive incoming calls.
"""
made_call = telemarketer_ds['made_call']

never_sent_texts = made_call.difference(telemarketer_ds['sent_text'])
never_received_texts = made_call.difference(telemarketer_ds['received_text'])
never_received_calls = made_call.difference(telemarketer_ds['received_call'])

possible_telemarketers = made_call.intersection(never_sent_texts, never_received_texts, never_received_calls)
possible_telemarketers = list(reversed(sorted(possible_telemarketers)))

print(f'These numbers could be telemarketers: ', pretty(possible_telemarketers))


# end of file
