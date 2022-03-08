print ('Lets begin IF')

for i in [1, 2, 3]:
    if i == 2:
        print ('The below break is going to happen')
        break
else:
    print ('You cannot reach me, because break will be happened!')

# ----------

print ('======')
print ('======')
print ('======')

print ('Lets begin WHILE')

while 1 == 2:
    print ('This will never happen')
    break
else:
    print ('This WILL happen , because break is not happened.')