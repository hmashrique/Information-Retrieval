'''
Problem 1 [20 points]. 
Write a Python/Perl script that copies, line by line, a text 
file into a destination file. The source and destination file paths are given
as input parameters. You should handle all cases.
'''


'''
The program takes a file location as source and a file location as destination and passes it into a function.
The function reads the input source file and writes it into the destination source file.

VERSION HISTORY:

Modified by Hasan Mashrique, 9/8/2022
'''

def FileCopy(source, dest):

# precondition: source file , destination file (empty)

# postcondition: reads source file content and writes to destination file


    f = open(source,'r',encoding = 'utf-8')  # opens the source file in read mode
    readFile= f.read()                      # reads the file line by line
    f.close()                               # close the file after reading
    #print(readfile)

    with open(dest, 'w') as f:              # open the destination file in write mode
        for line in readFile:
            f.write(line)                   # write the file line by line
        f.close()

#main                                       # main method
source="/Users/hmashrique/Coding/hello.txt" # source file location
dest="/Users/hmashrique/Coding/readme.txt"  # destination file location 

FileCopy(source,dest)                       # call the function with source and destination files as parameters
