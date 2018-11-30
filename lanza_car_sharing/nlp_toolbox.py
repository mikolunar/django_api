import re
import io
import sys


# Function to find occurence of substrin in string with overlaping charactres:
# e.g. abcdcdc (cdc) ==> 2 

def subString(string, sub_string):
    string1=input().strip()
    sub_str=input().strip()

    counter=0
    for index in range(0,len(string1)-len(sub_str)+1):
        substr=string1[index:index+len(sub_str)]
        print(substr)
        if substr==sub_str:
            counter+=1
        
    return counter

def validEmail(email_string):

    match=re.search(r"(?:\b)([^\s]*\@[^\s]*\.[a-zA-Z]{2,4})(?:\b)",email_string)

    return True

def validPhoneNumber(phone_number):

    line=sys.stdin.readline()
    test_str=str(line).strip()
    
    match = re.search(r'^[7-9]\d{9}$',test_str)
    if match:
        return True
    else:
        return False
    


    return True



def validateString(string):

    s=str(input()).strip()

    # 1 print True if  has any alphanumeric characters. Otherwise, print False. 

    if any(c.isalnum() for c in s):
        print('True')
    else:
        print('False')



    # 2 In the second line, print True if  has any alphabetical characters. Otherwise, print False. 

    if any(c.isalpha() for c in s):
        print('True')
    else:
        print('False')

    # 3 In the third line, print True if  has any digits. Otherwise, print False. 
    
    if any(c.isdigit() for c in s):
        print('True')
    else:
        print('False')

    # 4 In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
    
    if any(c.islower() for c in s):
        print('True')
    else:
        print('False')

    # 5 In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

    if any(c.isupper() for c in s):
        print('True')
    else:
        print('False')




validateString('')