#substitute method
import re
str="take up one idea.one at a time on onlyee"

result=re.sub(r'one','two',str)  #replaces or substitutes the elements
print(result)

result=re.sub(r'idea','ideas',str)
print(result)

#Quantifiers
result=re.findall(r'o\w+',str) #one are more starts with 'o'
print("+ --",result)

result=re.findall(r'o\w*',str)  #0 or more strats with o
print("* --",result)

result=re.findall(r'o\w?',str)  # 0 or one
print("? --",result)

result=re.findall(r'o\w{5}',str) #exact numbers of occurences
print("{} --",result)

result= re.findall(r't\w{1,3}',str)  #min  and max length of occurences
print("max min --",result)