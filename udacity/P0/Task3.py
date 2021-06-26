import csv
import re
import pprint

pretty = pprint.PrettyPrinter(indent=4).pprint

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


                    ~ Part A ~ 
Find all of the area codes and mobile prefixes called by people
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


                    ~ Part B ~ 
What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

i_calling_num = 0
i_receiving_num = 1
i_start_time = 2
i_duration = 3
list_of_codes = {
    'fixed': {'count': 0, 'code': set()},
    'mobile': {'count': 0, 'code': set()},
    'telemarketer': {'count': 0, 'code': set()}
}
bangalore_stat = {
    'bangalore_count': 0,
    'all_codes_total': 0
}
for i in calls:
    call_num = i[i_calling_num]
    receiving_num = i[i_receiving_num]
    if call_num[:5] == '(080)':
        fixed = re.search(r'\(\d+\)', receiving_num)
        mobile = re.search(r'[789]\d+\s', receiving_num)
        telemarketer = receiving_num[:3]
        if fixed:
            fixed = fixed.group()
            list_of_codes['fixed']['code'].add(fixed)
            list_of_codes['fixed']['count'] += 1
            if fixed == '(080)':
                bangalore_stat['bangalore_count'] += 1
        elif mobile:
            list_of_codes['mobile']['code'].add(mobile.group().strip())
            list_of_codes['mobile']['count'] += 1
        elif telemarketer == '140':
            list_of_codes['telemarketer']['code'].add(telemarketer)
            list_of_codes['telemarketer']['count'] += 1

codes = []
for k in list_of_codes:
    code_type_list = [i for i in list_of_codes[k]['code']]
    bangalore_stat['all_codes_total'] += list_of_codes[k]['count']
    codes.extend(code_type_list)

codes = sorted(codes)
percentage = round(bangalore_stat['bangalore_count'] / bangalore_stat['all_codes_total'], 2)

print(f'The numbers called by people in Bangalore have codes:\n', codes)
print(f'\n\n{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
