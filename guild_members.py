import re
import sys
import os
from bs4 import BeautifulSoup

def parse_log(members, input_file):
	''' Parse the input_log and output an updated member_list '''

	def update_members(members, re_sults):
		''' use a match from re to update members dictionary.  Some items are optional, so handle cases where they are missing. '''

		# If we've come across this name before, update the record (newer is better).  Otherwise initialize the member structure
		if re_sults.group('name') in members:		
			a_member = members[re_sults.group('name')]
		else:
			a_member = dict()
			members[re_sults.group('name')] = a_member
			
		a_member['character_level'] = re_sults.group('character_level')
		a_member['class'] = re_sults.group('class')
		a_member['diplomacy_level'] = re_sults.group('diplomacy_level')
		try:
			a_member['trade_level'] = re_sults.group('trade_level')
			a_member['trade_skill'] = re_sults.group('trade_skill')
		except:
			a_member['trade_level'] = '0'
			a_member['trade_skill'] = 'Undecided'
	
	# Vanguard's /who command reports a well semi-formatted dump.  Two formats are possible, those with Trade skills, and those without.
	# For example:
	#
	# [09:21:50] Khazull: Level 26 Rogue, 1 Diplomat (Stone & Steel) - Tursh Village
	# [09:21:50] Warfeild: Level 24 Paladin, 11 Blacksmith, 13 Diplomat (Stone & Steel) - Three Rivers Village

	# Parse the log looking for /who results.  Store in a tuple of tuples
	# members_list = [<member name>: [character_level: <level>, class: <class>, trade_level: <trade_level>, trade_skill: <trade_skill>, diplomacy_level: <diplomacy_level>], ... ]
	full_who_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*(?P<name>\w*):\s*Level\s*(?P<character_level>[0-9]+)\s*(?P<class>\w+),\s*(?P<trade_level>[0-9]+)\s*(?P<trade_skill>\w+),\s*(?P<diplomacy_level>[0-9]+)\s*Diplomat\s*\(Stone\s*\&\s*Steel\)")
	part_who_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*(?P<name>\w*):\s*Level\s*(?P<character_level>[0-9]+)\s*(?P<class>\w+),\s*(?P<diplomacy_level>[0-9]+)\s*Diplomat\s*\(Stone\s*\&\s*Steel\)")

	print("\n")
	for	line in open(input_file):
		who_match =  full_who_pattern.match(line)
		if who_match != None:
			update_members(members, who_match)
		else:
			part_who_match = part_who_pattern.match(line)
			if part_who_match != None:
				update_members(members, part_who_match)

def update_html(members, web_file):
	''' Process the html.  Update fields as available. '''

	def get_match_name(col, r_index, members):
		''' Get the character name from the current row if possible.  Return empty otherwise'''
		try:
			if r_index == 0:
				web_name = col.a.string
			else:
				web_name = col.b.font.find(text=True).string
			result = None
			for name in members:
				if web_name.startswith(name):
					result = name
		except Exception as ex:
			result = None
		return result
		
	source = BeautifulSoup(open(os.path.join(web_file, "members.html")))

	# We care about the 4th table in the page
	table = source.findAll('table')[3] 

	# We don't care for the first 2 or last 4 rows
	rows = table.findAll('tr')[2:-4]
	for r_index in range(len(rows)):
		row = rows[r_index]
		cols = row.findAll('td')

		name = get_match_name(cols[0], r_index, members)
		#name = get_name(cols[0], r_index)
		
		# If the current name is in our update list, do an inplace update.
		if name != None:
			try:
				for c_index in range(8):
					col = cols[c_index]
					if c_index == 3:
						col.b.font.string = members[name]['character_level']
					if (c_index == 5) and (col.b != None):
							col.b.font.string = members[name]['trade_level']
					if (c_index == 6) and (col.b != None):
						col.b.font.string = members[name]['trade_skill']
					if c_index == 7:
						col.b.font.string = members[name]['diplomacy_level']
				print("Updating: %s [level:%s, dipl:%s, tradeLevel:%s, Skill:%s]"% (name, members[name]['character_level'], members[name]['diplomacy_level'], members[name]['trade_level'], members[name]['trade_skill']))
			except Exception as ex:
				print('%s - [%s, %s]: %s'% (name, r_index, c_index, ex))
	
	# Write back the updated page.
	with open(os.path.join(web_file, "membersUpdated.html"), 'w') as outfile:
		outfile.write(source.prettify())

def main():
	# Gather user define pieces
	input_file = input("Enter the log name: (./data/vanguard.log): ")
	if input_file == '':
		input_file = "./data/vanguard.log"
	output_file = input("Enter the log markup name (%s.yuku): "% input_file)
	web_file = input("web content location (members.html, member_template.txt, etc) (./data/): ")
	if web_file == '':
		web_file = "./data/"
	if output_file == '':
		output_file = "%s.yuku"% input_file

	members = dict()
	parse_log(members, input_file)
	update_html(members, web_file)

	print("Done parsing\n")
		
if __name__ == '__main__':
	main()
