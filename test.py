import pyperclip

name=""

pyperclip.copy('''Hi '''+ name +'''

I came across your profile and was impressed by your work in [industry/field]. I'm currently [mention your role/area of interest, e.g., "a Data Science student at Arizona State University" or "exploring opportunities in data engineering"], and I would love to connect and learn from your expertise. Looking forward to connecting with you here on LinkedIn!''' + name)

text = pyperclip.paste() 
print(text) 


#logic
