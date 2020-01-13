"""
Regular Expression. Represented by a special syntax that helps you find and match a pattern inside a string
"""
myStr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, Javascript or PHP."
print(f"Find the programming language in the string below")
print(f"{myStr}")
# find the programming language in myStr that starts with capital 'P' and have 4 letters or the programming languages
# starting with the substring 'Java' regardless of 'j' being upper or lower case or the last 4 charaters preceeding the
# digit 3 (thon)
# all methods for regular expressions are provided by the re built-in module
import re 
# the match method, searches for the pattern provided (first arg) for the string (second arg) but only at the beginning 
# of the string 'a = re.match(pattern, string, optional flags)'
print(f"Look for 'you' at the beginning of the string") 
a = re.match("You", myStr)
print(f"{a}")
print(f"Look for 'abc' at the beginning of the string")
a = re.match("abc", myStr)
print(f"{a}")
print(f"{type(a)}")
# using group method to return the match returned
a = re.match("You", myStr)
print(f"A match has been found and it is {a.group()}")
# optional flag (ignore the case of the match) I/IGNORECASE
a = re.match("you", myStr, re.I)
print(f"Looking for 'you' and ignore the case in the string")
print(f"{a}")
print(f"Found {a.group()}")
# the you is now somewhere in the middle of the string
myStr = "Now I am moving the you to the middle of the string"
print(f"The string is now")
print(f"{myStr}")
print(f"Using the match method to find 'you'")
a = re.match("you", myStr, re.I)
print(f"{a}")
print(f"{type(a)}")
# this returns none as the pattern is not at the beginning of the string
# to search for a pattern across the entire string use the search method
# 'a = re.search(pattern, string, optional flags)'
a = re.search("you", myStr, re.I)
print(f"Using the search method to find 'you'")
print(f"{a}")
print(f"Found {a.group()}")
print(f"COMPLEX PATTERN MATCHING")
# define a more complex string
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222     L"
print(f"String to search is below with")
print(f"{arp}")
"""
syntax of regular expressions
lower case r before the pattern inside the "" means it should be treated as a raw string
() match the regular expresion in between them. Start and end of a group 
'.' any character except a newline character
'+' means 1 or more repetitions of the expression before it
'*' means 0 or more repetitions of the expression before it
'?' means matching as few characters as possible   
the space after (.+?) means match a group until a space is encountered
the '+' after the space means that there could be more than one space after the initial match
(\d) means any decimal digit 0-9 for the second group however this will be a single digit
the space after is to limit the group (boundary)
(.+?) with the addition of the other pattern 
'\s' match any whitespace character (space, tab or newline)
{2,} match means expect 2 or patterns preceeding the {} in this case '\s'. Without the comma it would expect exactly 2 repetitions
'\w' followed by the * matches 2 or more occurances of any word character (a-z, A-Z, 0-9 and _)
"""
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
# the below will return the match based on (.+?)
print(f"The first group match using (.+?): {a.group(1)}")
print(f"The second group match using +(\d): {a.group(2)}")
group3 = "+(.+?)\s{2,}"
print(f"The third group match using {group3}: {a.group(3)}")
print(f"The fourth group match using (\w)*: {a.group(4)}")
# returning the entire string can be done by a.group() and a.group(0)
# groups method will return a tuple where each element is a regex group 
print(f"Compete match returned as a tuple: {a.groups()}")
# the findall() method is, by far, the most used method because of returning a match object like match() and search() does
# it returns a list where each element was a pattern that was matched within the target string. It returns all the patterns
# that were matched. 
print(f"The find() method")
"""
using the findall() method to match the IP address in the arp variable using regular expression syntax. The IP address
for the match consists of 2 digits in the first octet, then a '.', another 2 digits, then another '.' etc until the last
octet which is a single digit
\d\d means two consequetive digits
\. this is character escaping as dot in regular expressions means any character except the new line character, so match
an actual '.' it needs to be escaped using a backslash. This is also valid for ?, +, () or any other characters that have
any other meaning in regular expressions
\d{2} means any preceeding digit (0-9) should occur only two times
\. another escaped '.' to represent the actual . in the IP address
[0-9][0-9] for the third octet a set of characters was used (regular expression) which defines a range of characters or a
character class that should be expected at that particular location in the pattern. In this case the character class is 
doubled as there is expectation that there will be 2 digits
\. another escaped '.' to represent the actual . in the IP address
[0-9]{1,3} for the fourth octet which uses a character set (0-9) which is expected to occur 1 to 3 times (1, 2, or 3 times)
One of these could have been used to represent the digit pattern that is being looked for
""" 
# the below will yield a single list which has the IP address as the element
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
print(f"The result of the pattern is {a} and its type is {type(a)}")
# group each octet which will yield a tuple within the list. Each tuple element is a group within the pattern 
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(f"The result of the pattern when it is grouped is {a}")
# add another IP address to the string
print(f"Adding another IP address to the string")
arp2 = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222    10.0.10.1   L"
b = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp2)
print(f"The string is {arp2}")
print(f"The result of the pattern when it is grouped is {b}")
"""
The sub() method replaces the occurances of the specified pattern in the target string with another string provided as an
argument
"""
print(f"The sub() method")
# replace all digits in string with 7
c = re.sub(r"\d", "7", arp)
print(f"The original string is {arp}")
print(f"The result of changing all digits to 7 is {c}")