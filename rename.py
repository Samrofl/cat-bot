import os, os.path
file_count = 0
for f in os.listdir("."):
    if f.endswith('.jpg'):
        file_count+=1
        if os.path.isfile(str(file_count)+".jpg"):
            print("File exists: "+str(file_count)+".jpg")
        else
            print("Renaming "+f+" to "+str(file_count)+".jpeg")
            os.rename(f,str(file_count)+".jpg")
    elif f.endswith('.jpeg'):
        file_count+=1
        if os.path.isfile(str(file_count)+".jpeg"):
            print("File exists: "+str(file_count)+".jpeg")
        else:
            print("Renaming "+f+" to "+str(file_count)+".jpeg")
            os.rename(f,str(file_count)+".jpeg")
print(file_count)
