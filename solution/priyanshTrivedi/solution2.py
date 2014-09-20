problem = """

Given two strings reverse, consider the second string as sequence of characters/deleimeters (partition points) and reverse each partition of the first string.

Eg.

    Input: A small man can cast a very big shadow., mtd
    Output : s Am llamsac nac natahs gib yrev a d.wo
    Highlighted delimeters:
        Before reversal: A small man can cast a very big shadow.
        After reversal: s Am llamsac nac natahs gib yrev a d.wo			"""
#ASSUMING CASE SENSITIVE

substrings = []			#Used to store all substrings and the delimiting char.
i = 0								#
j = 0

#Input the two string
string = raw_input("Please enter the first string")
string2 = raw_input("Please enter the second string")

#Refine string2 to not contain any dependency.
delimiters = list(set(string2))

#Loop identifies the strings to revert
for i in range(len(string)):
	if string[i] in delimiters:
		substrings.append((string[j:i],string[i]))	
		j = i+1

if j < len(string): 	substrings.append((string[j:],''))

#
# Assuming string = "You shall not pass" and delimiting char 'o' and 'a'
#	substrings will store the values as:
# [("Y",'o'),("u sh",'a'),("ll n",'o'),("t p",'a')]
#

result = []
for tuple in substrings:
	result.append(tuple[0][::-1]+tuple[1])

string = ''.join(result)
print string