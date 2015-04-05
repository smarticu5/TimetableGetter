import xml.etree.ElementTree as ET
import requests
import sys
# Andy: p122744
# Me: p121329

with open('finder2.html', 'r') as f:
	for line in f:
		if '1302651' in line:
			split = (line.split('Student: ', 1)[1]).split(',')
			name = split[1] + split[0]
			name = name.lstrip(' ')
			print 'Student\'s Name: {0}'.format(name)
			studentNumber = split[2][1:8]
			print 'Student Number: {0}'.format(studentNumber)
			url = (line.split('href="', 1)[1]).split('.')[0]
			url = url + '.xml'
			print url
sys.exit()

r = requests.get('https://timetables.abertay.ac.uk/Term2/' + url)
# print r.text

timetableFile = open('timetable.xml', 'w')
timetableFile.write((r.text[3::]).encode('utf8'))
timetableFile.close()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
getThese = ['day', 'starttime', 'endtime', 'category', 'prettyweeks', 'item']
events = []
tree = ET.parse('timetable.xml')
root = tree.getroot()

for event in root.iter('event'):
	tmpList = []
	for subtag in event:
		if subtag.tag in getThese:
			if subtag.tag == 'day': subtag.text = days[int(subtag.text)]
			# print '{0}:{1}'.format(subtag.tag.ljust(15), subtag.text)
			tmpList.append(subtag.text)
		if subtag.tag == 'resources':
			for subsubtag in subtag:
				if subsubtag.tag in ['module', 'staff', 'room']:
 					tmp = '{0}:'.format(subsubtag.tag.ljust(15))
 					tmp2 = ''
 					for subitem in subsubtag:
 						tmp2 = tmp2 + '{0}'.format(subitem.text)
 				tmp = tmp + ' ' + tmp2
 				# print tmp
 				tmpList.append(tmp2)
 	# print tmpList
 	events.append(tmpList)
 	# print '\n'

 # print events

for event in events:
 	print '{0} {1} from {2} to {3} on {4}s'.format(event[5], event[3].ljust(10), event[1], event[2], event[0])