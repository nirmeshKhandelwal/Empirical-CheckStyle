"""
One needs to provide the python file or package as input. If you are providing a directory, it must contain __init__.py file.
Reference: I got motivation for this script from https://gist.github.com/gregorynicholas/3152237. I have used some part of the mentioned code.
"""
import os
import re
import sys
import basic_style_check_on_project

def main():  
    if(len(sys.argv) < 2):
        print("Please provide python file or package path as command line argument")
        exit()
    target = sys.argv[1]
    if not os.path.exists(target):
        print("File or directory does not exists")
        exit()
    elif ((os.path.isfile and target[-3:] == ".py") or 
          (os.path.isdir(target) and '__init__.py' in os.listdir(target)) ): 
        check(target)
    else:
        print("Provided input is neither python file nor a python package."
              " Please Provide a valid python file path or python package path")
        exit()        

def check(module):
    global total, count
    print("CHECKING ", module)
    messages = {}
    pout = os.popen('pylint -r y %s'% module, 'r')
    for line in pout:
        if  "statements analysed" in line:
            number_of_statements = int(line.split(' ')[0])
            print(line)
        if "Your code has been rated at" in line:
            score = float(re.findall("\d.\d\d", line)[0])
            print(line)
        x = line.split('|')
        if len(x) == 4 and "message id" not in x[1]:   
            key = x[1].strip()
            value = int(x[2].strip())
            messages[key] = value
            print(line)

    print("=="*50)
    print(messages)
    print("=="*50)
    print("number_of_statements: " + str(number_of_statements) ) 
    print("score: " + str(score) )
  
if __name__ == "__main__":
    main()    
    #print "==" * 50
    #print "%d modules found"% count
    #print "AVERAGE SCORE = %.02f"% (total / count)