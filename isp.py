#Inter-Simulation Processing between the output file of QE to QE input

import sys

intial = open(sys.argv[1],"r")

cont=intial.read()
cont=cont.split("\n")

cont.index("   JOB DONE.")

#preparing output file

path=sys.argv[1].split("/")[0:-1]
path="/".join(path)+"/"

pos = cont.index("     Current dimensions of program PWSCF are:")
current_md="".join(filter(str.isdigit, cont[pos-2].split()[-1]))
if current_md=="": current_md = "0"

next_md=int(current_md)+1

post=open(path+"md"+str(next_md)+".in","w")

config=open("md-config.txt","r")
post.write(config.read())

#processing last coords. 
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

post.write("K_POINTS gamma")

print("completed")
