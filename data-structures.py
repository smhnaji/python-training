list (linked list in c, c++): [10, 20, True, 3.14, "my string here"]

myList = [10, 20, True, 3.14, "my string here"]
len(myList) => 5
print(myList[3]) => 3.14
myList[3] = "nnnnnnnnn"
print(myList[3]) => "nnnnnnnnn"
print(myList[-2]) => "nnnnnnnnn"

tuple: (10, 20, True, 3.14, "my string here")
mytupple = (10, 20, True, 3.14, "my string here")
immutable: this will error:
mytupple[0] = 8 => error

string
mystr = "salam"
immutable: this will error:
mystr[0] = 'S' => error

dict
mydict = {10: 'hiii', 'name': 'mohammad'}
mutable is OK:
mydict['name'] = 5554.77777

set
is not a sequence (yani tartib toosh mohem nist)
doesn't have index
>>> s = {10, 11, 10, 11, 15}
>>> print(s)
{10, 11, 15}

>>> existance = 10 in s
>>> existance
True