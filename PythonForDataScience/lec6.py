import pandas as pd
print(not True)
print(not False)
print(True or False)
print(True and False)

z = 5
if z % 2 == 0 :
 print("z is even")
else :
 print("z is odd")

brics = pd.read_csv("brics.csv",index_col=0)
brics["on_earth"] = [True, True, True, True, True]
brics["density"] = brics["population"] / brics["area"] * 1000000
print(brics)
print(brics["country"])
print(brics.country)
print(brics.loc["BR"])
print(brics.loc["CH","capital"] )
print(brics["capital"].loc["CH"] )
