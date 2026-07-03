intial = open("vaspin.txt","r")
post=open("out.txt","w")

cont=intial.read()
cont=cont.split("\n")

pos=cont.index("Ag Zn Te")
Ag, Zn, Te = cont[pos+1].split()


pos=cont.index("Cartesian")
print(type(cont))

dict = {"Ag":Ag,"Zn":Zn,"Te":Te}
for X in dict:
    for i in range(int(dict[X])):
        
        post.write(X+"      "+cont[pos+1]+"\n")
        pos+=1

