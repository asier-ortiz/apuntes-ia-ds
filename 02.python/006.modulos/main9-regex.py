"""
https://regexr.com/
https://docs.python.org/3/library/re.html
"""
import re

text1 = "Hola y Adiós."
text2 = "Hola y hasta luego."

result = re.search("^Hola.*Adiós.$", text2)
print(result)