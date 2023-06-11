import pyshorteners

iinput=input("Enter the Link: ")
s=pyshorteners.Shortener()
output=s.tinyurl.short(iinput)
print(output)
