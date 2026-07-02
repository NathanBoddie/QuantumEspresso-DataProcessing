intial = open("in.txt","r")
post=open("out.txt","w")


cont=intial.read()
cont=cont.split("\n")


for i in range(len(cont)):
    x=cont[i].split()
    if len(x) == 4:
        cont[i]+=("    1   1   1")
    post.write(cont[i]+"\n")

print("completed")

#expend in order to take .out file and plug into .in than modify to add it into sbatch