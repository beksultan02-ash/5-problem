import re
def find(s):
     charRe  = 'ab{3}'
     if re.search(charRe, s):
         return "found a match"
     else :
         return "not matched"    


s= input()
print (find(s) )