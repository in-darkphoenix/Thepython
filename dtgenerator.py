import datetime
"""this script contains the creation od empty files. """
filename=datetime.datetime.now()

#create empty file
def createfile() :
    """This function creates an empty file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
       file.write("") #writing empty string

createfile()
