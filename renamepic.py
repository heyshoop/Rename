# -*-coding:utf8-*-
import os

f = open('ID.txt','r')
ids = dict()
i=0
for id in f:
    ids[i] = id
    i = i+1
path = "D:\workspace\python\Rename\image"
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        num = int(file.split(".")[0].split("e")[1])-1
        newname = ids[num].replace("\n","") + '.jpeg'
        os.rename(os.path.join(path, file), os.path.join(path, newname))
        print(file+"-------->"+newname)