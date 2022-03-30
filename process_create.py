#!C:/Users/julia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python3/python


import cgi
form=cgi.FieldStorage()

title=form['title'].value
description=form['description'].value
opened_file=open("data/"+title,'w')
opened_file.write(description) 

print("Location=index.py?id="+title)
print()