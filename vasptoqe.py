#changes form a .vasp to the proper format needed in qe input coordnates
intial = open("in.txt","r")
post=open("out.txt","w")

cont=intial.read()
cont=cont.split("\n")

pos=cont.index("Ag Zn Te")
Ag, Zn, Te = cont[pos+1].split()


pos=cont.index("Cartesian")
print(type(cont))

cont = list(map(lambda x: x.replace("T T T", "1 1 1").replace("F F F", "0 0 0"), cont))

dict = {"Ag":Ag,"Zn":Zn,"Te":Te}
for X in dict:
    for i in range(int(dict[X])):
        
        post.write(X+"      "+cont[pos+1]+"\n")
        pos+=1

print("completed")
