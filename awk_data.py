from random import randint, choice
from calendar import month_name

fname = [
    'Ayush', 'Ashutosh', 'Shubham', "Vibhor", "Amrit", "Pankaj", 'Vatsal',
    'Siddharth', 'Sahil'
]
lname = ['Rawat', 'Bisht', 'Negi', 'Joshi', 'Mehra', 'Bhandari', 'Thapliyal']

city = ['Pune', 'Delhi', 'Goa', 'Dehradun', 'Kanpur']
pos = ['Manager', 'Analyst', 'CTO', 'CEO', 'Developer', 'Programmer']
spec = ['c', 'c++', 'R', 'js', 'java', 'rust', 'go']

file_names = ['vibhor.txt', 'pankaj.txt', 'sahil.txt', 'vatsal.txt', 'ayush.txt']

for file in file_names:
    with open(f'S:/{file}', 'w') as fl:
        names = set()
        ID = set()

        for i in range(1, 31):
            while True:
                eid = randint(100, 1000)
                if eid not in ID:
                    ID.add(eid)
                    break

            while True:
                f = choice(fname)
                l = choice(lname)
                if f + l not in names:
                    names.add(f + l)
                    break
            c = choice(city)
            p = choice(pos)
            s = choice(spec)

            print(eid,
                  f,
                  l,
                  c,
                  p,
                  randint(30000, 100000),
                  s,
                  "Project_" + p + "_" + s,
                  month_name[randint(1, 12)],
                  randint(2000, 2022),
                  file=fl)
