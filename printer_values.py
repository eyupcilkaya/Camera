import pandas as pd

f = open("log.txt")
lines=f.readlines()

for line in lines:
    line=line.split(" ")
    v=pd.Series(line)
    if v[0]=="ok":
        for i in v:
            if i[0:2] in "T:":
                print(i[2:])

            elif i[0:2] in "B:":
                print(i[2:])
            else:
                continue
