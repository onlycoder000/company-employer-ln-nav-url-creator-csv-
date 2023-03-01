import csv
import urllib.parse
# https://www.linkedin.com/sales/search/people?query=(recentSearchParam:(id:1617272009,doLogHistory:true),filters:List((type:CURRENT_COMPANY,values:List((text:first,selectionType:INCLUDED),(text:middle,selectionType:INCLUDED),(text:last,selectionType:INCLUDED)))))&sessionId=ZAJd3TUFR+mUK7BjGnBr+Q==&viewAllFilters=true
f = open("export.txt", "w")
f.write("")
f.close()

file = open('import.csv')
csvreader = csv.reader(file)

c=0

lp_prefix='(text%3A'
lp_suffix='%2CselectionType%3AINCLUDED)'

link_prefix='https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList('
link_suffix='))))&sessionId=HlIWahktREiHR2BLNRhxaA%3D%3D&viewAllFilters=true'

ln_text=''
for row in csvreader:
    if c==0:
        c=c+1
        continue
    if c%5 == 0:
        f = open("export.txt", "a")
        f.write(link_prefix+ln_text+link_suffix+'''
''')
        f.close()
        ln_text=''
        r=''
    else:
        r='%2C'
    tem=urllib.parse.quote(row[0])
    # tem=row[0]
    ln_text=ln_text+(lp_prefix+tem+lp_suffix)+r
    c=c+1
    


