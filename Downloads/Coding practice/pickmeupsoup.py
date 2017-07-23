import sys
import requests 
from bs4 import BeautifulSoup

pickUpLine = 'https://pickupline.net'

# gets the raw html from the pickUpLine
req = requests.get(pickUpLine)
data = req.text
soup = BeautifulSoup(data)

#makes it pretty 
soup.prettify()
pickUpTable = soup.find('tbody', {'class': 'row-hover'})
pickUpRow = pickUpTable.findChildren()	

i = 0 
list = []
for child in pickUpRow:
	for pickUpTwo in child:
		i = i + 1
		#if i % 9 == 0:
			#print("line",i, pickUpTwo)
		# Stores the children of the table in a list 	
		list.append(pickUpTwo)
		
		#if any("https://pickupline.net" in s for s in list):
			#print(p)
	

#Storing links in a link list 
link = []
i = 0
for item in list:
	if i < 5:
		i = 5 
		link.append(list[i])
	elif i + 8 < len(list):
		i = i + 8
		link.append(list[i])
	else:
		break
		
print(link)

# Parse out links 