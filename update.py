#!C:/Users/julia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python3/python
print("Content-Type: text/html; charset=euc-kr/n")
print()

import cgi, view
form=cgi.FieldStorage()

if "id" in form:
    pageId = form["id"].value
    description=open("data/"+pageId, 'r').read()
    
else:
    pageId = "Welcome!"  
    description ="Hello Web!"


print("""
<!doctype html>
<html>
<head>
    <title>Web1-welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <H1><a href="index.py">WEB</a></H1>
    <ol>
        {list}
    </ol>
    
    <form action="process_update.py" method="post"></p>
        <p><input type="hidden" name="pageId" value={title}></p>
        <p><input type="text" name="title" value={title}></p>
        <p>textarea name="description">{text} 
          
        </textarea></p>
        <p><input type="submit"></p>
    </form>
    
</body>

</html>
""".format(title=pageId, text=description, list=view.listing())
)

#7. URL query로 id값갖고와서 소제목 바꾸기. URL query 갖고오기
#8. id가 없는 경우는 Hello web으로 if구문 사용하기
#13. description 만들기 파일 열어서 만들기
#18. for 구문 이용해서 list를 하위디렉토리에서 생성하기. 하위 디렉토리 파일만 관리하면 자동으로 되게 만들기. 
#이제부터 사용자를 도입
#19. create 만들기. 
