import time

with open('finder2.html', 'r') as f:
	for line in f:
		if 'staff:' in line.lower() or 'student:' in line.lower():
			if 'staff' in line.lower():
				role = 'Staff'
			else: role = 'Student'
			# print line
			splits = line.split(':')[1].split(',')
			if len(splits) > 2:
				forename = splits[1].lstrip( )
				surname = splits[0].lstrip( )
				idnumber = splits[2].lstrip( ).split('<')[0]
			else:
				forename = splits[0].split(' ')[0]
				surname = splits[0].split(' ')[1]
				idnumber = splits[1].split('<')[0]
			for splitEnum in splits:
				if len(splitEnum) < 3:
					print 'Sleeping for', splitEnum
					time.sleep(3)
			print 'Role:\t\t{0}\nForename:\t{1}\nSurname:\t{2}\nIDNumber:\t{3}\n'.format(role, forename, surname, idnumber)