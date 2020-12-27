import threading 
from threading import*
import time

data={} #'data' is the dictionary in which we will store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional 

def create(key,value,timeout=0):
    if key in data:
        print("Error: The key entered already exists") #error message
    else:
        if(key.isalpha()):
            if len(data)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and jsonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    data[key]=l
            else:
                print("Error: Memory limit exceeded! ")#error message
        else:
            print("Error: Invalind key_name! special characters and numbers are not allowed key_name must contain only alphabets ")#error message

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in data:
        print("Error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=data[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                val=str(key)+":"+str(b[0]) #to return the value in the format of jsonobject i.e.,"key_name:value"
                return val
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            val=str(key)+":"+str(b[0])
            return val

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in data:
        print("Error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=data[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del data[key]
                print("Key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #error message
        else:
            del data[key]
            print("key is successfully deleted")

# Additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=data[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in data:
                print("Error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                data[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in data:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            data[key]=l