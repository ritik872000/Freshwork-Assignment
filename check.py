#here are the commands to demonstrate how to access and perform operations on a main file
#run the code file first in order to perform the operations

import datastore as data 
#importing the main file("datastore" is the name of the file I have used) as a library 

data.create("Ritik",216)

#to create a key with key_name,value given and with no time-to-live property
data.create("Shubhankar",217,60) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)

#it returns the value of the respective key in jsonobject format 'key_name:value'
data.read("Ritik")

#it returns the value of the respective key in jsonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR
data.read("Shubhankar")

#it returns an ERROR since the key_name already exists in the database
data.create("Ritik",216)

#it replaces the initial value of the respective key with new value (to avoid the error due to above command)
data.modify("Ritik",220)

 #it deletes the respective key and its value
data.delete("Shubhankar")

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
