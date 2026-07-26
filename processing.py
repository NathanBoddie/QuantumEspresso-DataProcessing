intial = open("in.txt","r")
post=open("out.txt","w")


cont=intial.read()
cont=cont.split("\n")

cont.index("   JOB DONE.")

pos =  cont.index("     The maximum number of steps has been reached.")


iterations = cont[pos-109]
time = cont[pos-108]

iterations = iterations.split()[-1]
time = time.split()[-2]
print("Iteration: "+iterations+ " | " + time +" pico-seconds")

temp_cont = []
#pos-102 to pos-12
for i in range(90):
    temp_cont.append(cont[pos-102+i])
cont=temp_cont

for i in range(len(cont)):
    x=cont[i].split()
    if len(x) == 4:
        cont[i]+=("    1   1   1")
    post.write(cont[i]+"\n")

print("completed")

#expend in order to take .out file and plug into .in than modify to add it into sbatch
