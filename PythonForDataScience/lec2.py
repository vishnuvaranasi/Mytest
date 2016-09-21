fam1 = [1.73,1.68,1.71,1.89]
fam2 = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam3 = [["liz", 1.73],
	["emma", 1.68],
 	["mom", 1.71],
 	["dad", 1.89]
       ]
print(fam1)
print(fam2)
print(fam3)
print(type(fam1),type(fam2),type(fam3))
print("\n")
print(fam1[3])
print(fam2[3])
print(fam3[3])
print("\n")
print(fam1[-1])
print(fam2[-1])
print(fam3[-1])
print("\n")
print(fam1[-3:-1])
print(fam2[-3:-1])
print(fam3[-3:-1])
print("\n")
print(fam1[3:])
print(fam2[3:])
print(fam3[3:])
print("\n")
fam2[7] = 1.86
fam2[0:2] = ["lisa", 1.74]
print(fam1)
print(fam2)
print(fam3)
print("\n")
fam1 = fam1 + ["me", 1.79]
del(fam2[2])
print(fam1)
print(fam2)
print(fam3)
print("\n")
