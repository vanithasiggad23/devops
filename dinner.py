dinner=['vani','aru','smith']
message="hello"+" "+dinner[0]+" i am glad to invite you to dinner"
print(message)
message="hello"+" "+dinner[1]+" i am glad to invite you to dinner"
print(message)
message="hello"+" "+dinner[2]+" i am glad to invite you to dinner"
print(message)
print("oh aru could not make it")
dinner.append('vaishu')
print(dinner)
del dinner[1]
print(dinner)
message="hello"+" "+dinner[0]+" i am glad to invite you to dinner"
print(message)
message="hello"+" "+dinner[1]+" i am glad to invite you to dinner"
print(message)
message="hello"+" "+dinner[2]+" i am glad to invite you to dinner"
print(message)
print("it seems i have found a bigger tabel")
dinner.insert(0,'sana')
print(dinner)
dinner.insert(2,'ravi')
print(dinner)
dinner.append('raj')
print(dinner)
for guest in dinner:
    message=f"hello {guest} i am glad to invite you to dinner"
    print(message)
print("oh sorry  table is late so only two can be picked randomly")
me=dinner.pop()
print("sorry buddy  "+  me)
me=dinner.pop()
print("sorry buddy  "+  me)
me=dinner.pop()
print("sorry buddy  "+  me)
me=dinner.pop()
print("sorry buddy  "+  me)
print(dinner)
for guys in dinner:
    print(f"hello {guys} you must attend the dinner!!")
count=len(dinner)
print(count)
