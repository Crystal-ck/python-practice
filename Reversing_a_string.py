#String to be reversed
string="Hello World!"
#Stores the reverse of the string string
reverse=" "
#for loop adds each character to reverse hence reversing the string
for ch in string:
    reverse = ch +reverse
print(reverse)