import os,shutil
f=open("icd_collected.dat","a")

for files in os.listdir("./"):
    if files.endswith(".txt"):
        g=open(files,"rt")
        for line in g:
            f.writelines(line+'\n')
        #shutil.copyfileobj(g,f)
        g.close()
f.close()
