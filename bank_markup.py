import re
import sys

# Gather user define pieces
input_file = input("Enter the log name: ")
output_file = input("Enter the log markup name (%s.yuku)"% input_file)
if output_file == '':
	output_file = "%s.yuku"% input_file
input_file_handle = open(input_file)

# Vanguard's /bankdisplay command reports a well formatted bank dump:
#
# [HH:MM:SS] ---- Bank Items ----
# [HH:MM:SS] Item1, Item2, ..., Item YY
# Attached Enchantments:

# Parse off The head of the log by looking for the "Bank Items" line.
start_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\] ---- Bank Items ----")
start_found = False
while not start_found:
	line = input_file_handle.readline()
	start_found =  start_pattern.match(line) != None

items = input_file_handle.readline()[10:]

# Split into a list of just item names.
item_list = items.split(',')

print("Logging to: %s"% output_file)
with open(output_file, 'w') as output_file_handle:
	for item in item_list:
		item = item.strip()
		# Sometimes we have multples.  Strip off the count.
		item_count = item
		while '(' in item:
			item = item[:-1]
		output_file_handle.write("([link=http://vanguard.wikia.com/wiki/%s]wikia[/link] - [link=http://wiki.silkyvenom.com/index.php/%s]silky[/link]) %s\n"% (item.replace(" ", "_"), item.replace(" ", "_"), item_count))
		
