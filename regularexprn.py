#search method
import re
str = "Take one on map.only one on man"
result = re.search(r'o\w\w',str)  #\w is a alphanumeric
print(result)     #prints all info

print(result.group())  #print exact match

#findall Method
result = re.findall(r'm\w\w',str)  #findall method checks all similars
print(result)

#match method
result = re.match(r'T\w\w',str) #searches only beggining of string
print(result.group())

#split method
str1= "Take one 23 on map.6only one on 58man"
result=re.split(r'\d+',str1)  #splits the string wherever digits are there
print(result)