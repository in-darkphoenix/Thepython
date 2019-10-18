"""this script conrains the creation od empty files. """
filename="sample.txt"

#create empty file
def createfile() :
    """This function creates an empty file"""
    with open(filename,"w") as file:
       file.write("") #writing empty string
