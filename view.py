#!C:/Users/julia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python3/python
print("Content-Type: text/html; charset=euc-kr/n")
print()

import os

def listing():
    liststr=""
    items=os.listdir("data")
    for i in items:
        liststr=liststr+"<li><a href='index.py?id={x}'>{x}</a></li>".format(i)
    return liststr 

