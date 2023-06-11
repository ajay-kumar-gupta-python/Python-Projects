import pyshorteners

url="https://www.google.com"
s=pyshorteners.Shortener()
output=s.tinyurl.short(url)
print(output)
