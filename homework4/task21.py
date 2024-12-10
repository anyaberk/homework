# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>

 </body>
</html>
"""
f_template =f""" 
<!DOCTYPE HTML>
<html>
<head>
<title> {page['title']} </title>
<meta charset="{page['charset']}">
</head>
<body onload="alert('{page['alert']}')">

<p>{page['p']}</p>

</body>
</html>
"""
print(f_template)


f=open("index.html","w", encoding='utf-8')
f.write(f_template)
f.close()
