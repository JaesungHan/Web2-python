#!C:/Users/julia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python3/python


import cgi,os
form=cgi.FieldStorage()
pageId=form["pageId"].value
os.remove("data/"+pageId)


print("Location=index.py")
print()