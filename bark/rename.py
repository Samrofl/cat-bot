import os, os.path, re, glob
file_count = 0
unused=[]

#Search for gaps in filenames
for f in os.listdir("."):
    file_count+=1
    if not glob.glob(str(file_count)+'.*'):
        print("not found: " + str(file_count))
        unused.append(file_count) #build list of gaps
    else:
        print("file found: "+glob.glob(str(file_count)+'.*')[0])
print(unused)

#Search for files not conforming to standard
#Rename them using gaps
for f in os.listdir("."):
    if not re.match(r"[0-9]+.(jpg|png|jpeg)",f):
        ext = f.split(".")[1]
        if ext in ("jpg","png","jpeg"):
            print(f+" renamed to " + str(unused[0])+"."+ext)
            os.rename(f,str(unused[0])+"."+ext)
            del unused[0]
        else:
            print("Cannot rename "+f)
