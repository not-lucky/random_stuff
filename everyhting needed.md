Counter, defaultdict,
string,tuple, basically all ds methods... V.IMP.
dict.fromkeys(any_sequence)  usefull for in like ordered set
filter
reduce
cmath module
round()  to round float

itertools
product, permutations, 
groupby

Use
enumerate  
for _not in_ do this  

command, *args = input().split()

eval(f"arr.{command}({','.join(args)})")  
OR  
exec

join,split

string.startswith(substring)

string.ljust(total_width, "what to fill with')
center
rjust

NOTE:
a, *b = input().split()
a is single element
while b will be a list
ex:
a, *b = input(), Counter(map(int, input().split()))

a will be sinlge input
b will be list containing a single counter object
