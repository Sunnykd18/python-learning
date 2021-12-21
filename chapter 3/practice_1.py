name = input("enter your name:")
Date = input("enter your date:")
su
template = '''
Dear <|name|>,
you are selected
<|date|>'''

print(template.replace('<|name|>', name).replace('<|date|>', Date))