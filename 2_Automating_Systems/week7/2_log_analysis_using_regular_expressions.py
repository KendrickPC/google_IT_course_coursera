# https://www.coursera.org/learn/python-operating-system/discussions/weeks/7/threads/8BzoZ74LQvGc6Ge-C2Lxcw

#!/usr/bin/env python3

import re
import operator
import csv

def users_list(dic1,dic2):
  usuarios = []
  for item2 in dic2.keys():
    if item2 not in usuarios:
      usuarios.append(item2)
  for item1 in dic1.keys():
    if item1 not in usuarios:
      usuarios.append(item1)
  return usuarios
per_user = {'user1':{'INFO':0, 'ERROR':0}, 'user2': {'INFO': 0, 'ERROR': 0}}

error={}
info={}
per_user={}
us=""
err_pattern=r"ERROR\s[\w\s].* "
user_pattern=r"\((\w+)\)"
f=open("syslog.log")
for line in f.readlines():
  inf=re.search(r"ticky: INFO",line)
  if inf!=None:
   us=re.search(user_pattern,line)
   if us!=None:
     user_name=us.group()[1:-1]
     if user_name not in info.values():
       info[user_name]=1
     else:
       info[user_name]+=1
  elif re.search(r"ticky: ERROR",line)!=None:

    us = re.search(user_pattern, line)
    if us != None:
      user_name=us.group()[1:-1]
      if user_name not in error.values():
        error[user_name] = 1
      else:
        error[user_name] += 1

lista=users_list(info,error)
lista.sort()
sorted(lista)

for element in  sorted(lista, reverse=False):
  if element in info.keys():
    if element not in per_user.keys():
      per_user[element]=[1,0]
    else:
      num1=per_user[element][0]
      num2=per_user[element][1]
      per_user[element]=[num1+1,num2]
  elif element in error.keys():
      if element not in per_user.keys():
          per_user[element] = [0, 1]
      else:
          num1 = per_user[element][0]
          num2 = per_user[element][1]
          per_user[element] = [num1 , num2+1]

print(per_user)




f.close()

######################Error Message csv
err_types={}

fi=open("syslog.log")
for line in fi.readlines():
  e = re.search(err_pattern, line)
  if e!=None:
    tipo=e.group().strip("ERROR ")
    if tipo not in err_types:
      err_types[tipo]=0
    else:
      err_types[tipo]+=1
fi.close()

error_types=sorted(err_types.items(), key = operator.itemgetter(1), reverse=True)
error_types_sorted={}

for key,value in error_types:
  error_types_sorted[key]=value

err_file=open("error_message.csv","w")
err_file.write("Error, Count\n")

for key,value in error_types_sorted.items():
  err_file.write(key+", "+str(value)+"\n")


users_sta=open("user_statistics.csv","w")
users_sta.write("Username, INFO, ERROR\n")

for key,value in per_user.items():
  users_sta.write(key+", "+str(value[0])+", "+str(value[1])+"\n")
users_sta.close()
  