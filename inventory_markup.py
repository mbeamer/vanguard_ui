import re
import sys

# Gather user define pieces
input_file = input("Enter the log name: ")
output_file = input("Enter the log markup name (%s.yuku)"% input_file)
if output_file == '':
	output_file = "%s.yuku"% input_file
input_file_handle = open(input_file)

# Vanguard's /inventory command reports a well formatted inventory dump:
#
# [HH:MM:SS] Inventory: 
# [HH:MM:SS] Capacity: XX Space used: YY
# [HH:MM:SS] Items: Item1, Item2, ..., Item YY
# Attached Enchantments:

# Parse off The head of the log by looking for the "Inventory" line.
start_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\] Inventory: ")
start_found = False
while not start_found:
	line = input_file_handle.readline()
	start_found =  start_pattern.match(line) != None

capacity = input_file_handle.readline()
items = input_file_handle.readline()[18:]

# Split into a list of just item names.
item_list = items.split(',')

print("Logging to: %s"% output_file)
with open(output_file, 'w') as output_file_handle:
	for item in item_list:
		item = item.strip()
		while '(' in item:
			item = item[:-1]
		output_file_handle.write("[link=http://vanguard.wikia.com/wiki/%s]%s[/link]\n"% (item.replace(" ", "_"), item))
