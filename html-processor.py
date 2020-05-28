import re


text = open('testpage.txt','r',encoding='utf-8').read()
# print(text)

# ΕΡΩΤΗΜΑ 1

rexp = re.compile('<title>(.*?)</title>')

m = rexp.search(text)

print(m.group(1))

# ΕΡΩΤΗΜΑ 2

rexp = re.compile('<!--(.*?)-->', re.DOTALL) 

m = rexp.sub('<!-- --> ', text) 

#print(m)

# ΕΡΩΤΗΜΑ 3

rexp = re.compile('<script>(.*?)</script>', re.DOTALL)

m = rexp.sub(' ', m) 

rexp = re.compile('<style>(.*?)</style>', re.DOTALL)

m = rexp.sub(' ', m) 

# print(m)

# ΕΡΩΤΗΜΑ 4

rexp = re.compile('<a(.*?)</a>')


for x in rexp.finditer(m):
    print(x.group(0))
    
# ΕΡΩΤΗΜΑ 5

rexp = re.compile(r'<.*?>')
m = rexp.sub(' ', m)
# print(m)


# ΕΡΩΤΗΜΑ 6
def cp(m):
    if (m.group(0)=='&amp'):
        #print(m.group(0))
        return '&'
    elif (m.group(0)=='&lt'):
        #print(m.group(0))
        return '<'
    elif (m.group(0)=='&gt'):
        return '>'
    elif (m.group(0)=='&nbsp'):
        return ' '
rexp = re.compile('&amp|&lt|&gt|&nbsp')
m = rexp.sub(cp, m)
#print(m)

# ΕΡΩΤΗΜΑ 7
def cp2(m):
    return ' '
rexp = re.compile(r'\s+')
m = rexp.sub(cp2, m)
print(m)
# ΕΡΩΤΗΜΑ 8
text_file = open("output.txt", "w", encoding='utf-8')
n = text_file.write(m)
text_file.close()












