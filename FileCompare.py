import difflib

text1 = '''  1. Beautiful is better than ugly.
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
            '''.splitlines(keepends=False)


text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
    '''.splitlines(keepends=True)

d = difflib.HtmlDiff()
htmlContent = d.make_file(text1,text2)
# print(htmlContent)
with open('diff.html','w') as f:
    f.write(htmlContent)
