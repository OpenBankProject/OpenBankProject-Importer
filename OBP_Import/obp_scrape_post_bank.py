__author__ = 'simonredfern'

from BeautifulSoup import BeautifulSoup


import urllib

#f = urllib.urlopen("http://Volumes/not_on_your_nelly/Bank_statements/Postbank-Online-Banking_100_days.html")

f = open('/Volumes/not_on_your_nelly/Bank_statements/Postbank-Online-Banking_100_days.html', 'r')

# Read from the object, storing the page's contents in 's'.
s = f.read()
f.close()


html = s



soup = BeautifulSoup(html)


#print soup.prettify()


print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

balance = soup.find("span", { "class" : "balance-amount" })

print 'balance is %s' % balance.contents[0]

"""

entry = soup.find("td", { "class" : "headers-entry-note" })

print 'entry is %s' % entry

print 'entry.next is %s' % entry.next


print 'entry.parent is %s' % entry.parent


entries = soup.findAll("td", { "class" : "headers-entry-note" })

print 'entries is %s' % entries

for e in entries:
    print e
    print "\n"

"""




# Grab the <table id="mini_player"> element
scores = soup.find('table', {'id':'mini_player'})

# Get a list of all the <tr>s in the table, skip the header row
rows = scores.findAll('tr')[1:]








# note: this id seems to change!

my_id = "idc7c"
tbody = soup.findAll("tbody", { "id" : my_id })
print 'tbody is %s' % tbody


print 'yyyyyyyyyyyyyyyyyyyyyyyyyyy'

rows = tbody.findAll('tr')[0:]
















#for i in tbody.tr:
#    print i

#print tbody.children

#data = soup.findAll("table", { "id" : "ida9" })
#print 'data is %s' % data




#soup.find("div", {"id": "articlebody"})




#for tr in tbody.findAll('tr'):
#    print 'this is a row'



