#date
import re
str = "2-1-1998 2-04-1999"

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)

print(result)

#special characters
str="take up one idea.one at a time on onlyee"

result = re.findall(r'^t\w*',str)
print(result)