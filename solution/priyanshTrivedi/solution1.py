problem = """ Given two strings, reverse all the occurrences of second string in the first string.

    					Input: Two strings
					    Output: First string with every occurrence of second string reversed.

							Eg.

    					Input: betty_thguob_rettob_a_bit_of_butterty_botter_bought_a_bit_of_butter._the_butter_betty_botter_bought_was_a_bit_bitter, botter_bought
    					Output: betty_thguob_rettob_a_bit_of_butter._the_butter_betty_thguob_rettob_was_a_bit_bitter"""


#Input the two string
string1 = raw_input("Please enter the first string")
string2 = raw_input("Please enter the second string")

#If the string2 is in string1
if string2 in string1:
	
	string2_rev = string2[-1:0:-1] + string2[0]		#Reverse a string by slicing it, iterating backwards starting from the last char.
	print string1.replace(string2, string2_rev)		#Print a replaced version of it.

else:
	print string1
	





