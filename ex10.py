tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
Ill do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

sad_cat = """
Ill do another list:
\t* Cat f\aood
\t* Cat f\bood
\t* Cat f\food
\t* Cat f\nood
\t* Cat f\rood
\t* Cat f\tood
\t* Cat f\vood
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print sad_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i

# Note: made a mistake on line 7 and typed the wrong word
# come back and do SD 3,4
