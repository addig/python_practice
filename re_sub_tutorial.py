# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

#Replacing " && " and " || " by "and" and "or"
def replace_op(match):
    match =re.sub(" && "," and ",match)
    match =re.sub(" \|\| "," or ",match)
    return str(match)
num = int(raw_input())
lines = ""
for n in xrange(num):
    lines+=raw_input()+"\n"
output_string = replace_op(lines)
print(output_string)