#!C:/Users/julia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python3/python
print("Content-Type: text/html; charset=euc-kr/n")
print()

import cgi, view
form=cgi.FieldStorage()

if "id" in form:
    pageId = form["id"].value
    description=open("data/"+pageId, 'r').read()
    update="<a href='update.py?id={}'>update</a>".format(pageId)
    delete_action="""
        <form action="process_delete.py" method="post">
            <p><input type="hidden" name="pageId" value={title}></p>
            <p><input type="submit" value="delete">
        </form>"""   
else:
    pageId = "Welcome!"  
    description ="Hello Web!"
    update=""
    delete_action=""

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
    <a href="create.py>create</a><br>
    {update}
    {delete} 
    <H2>{title}</h2>
        <p>
            {text}
        </p>
</body>

</html>
""".format(title=pageId, text=description, list=view.listing(), update=update, delete=delete_action)
)

#7. URL query로 id값갖고와서 소제목 바꾸기. URL query 갖고오기
#8. id가 없는 경우는 Hello web으로 if구문 사용하기
#13. description 만들기 파일 열어서 만들기
#18. for 구문 이용해서 list를 하위디렉토리에서 생성하기. 하위 디렉토리 파일만 관리하면 자동으로 되게 만들기. 
#이제부터 사용자를 도입
#19. create 만들기. write 기능을 이용.file.write(text) 그리고 form action="" method=post 
#20. update 만들기. write와 read를 잘 버무림. <input type=hidden을 통해 은밀하게 전송하는 법. os rename(,)
#21. 삭제, delete기능, os.remove()
#25. 함수를 통해 중복을 제거. 
#27. 모듈 사용해보기
#29. 보안 관련해서 HTML sanitizer까지. PiPY PiP까지 해보기. 