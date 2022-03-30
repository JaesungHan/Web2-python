#!C:/Users/julia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python3/python

import cgi,os
form=cgi.FieldStorage()


pageId=form["pageId"].value
title=form['title'].value
description=form['description'].value
os.rename("data/"+pageId, "data/"+title)
opened_file=open("data/"+title,'w')
opened_file.write(description) 

print("Location=index.py?id="+title)
print()