"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Tulabut Adrian A]
Date: [9-27-26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[

--------- condition ----------
the condition syntax is used when you want to verify something first before it run he code
for example, you only want to let someone pass if they are above 18yo, in this case you are gonna use the if elif and else 
conditions, so in human language, 

--------- if / elif / else:----------
if (you are 18 yo) [you can pass the gate]
else (you are below 18) [you can't pass the gate]
and if were gonna code that its gonna be
if age >= 18:
  print("you can pass the game")
else:
  print("stay inside")

  
--------- comparison operator ----------
the comparison operator by word itself compares two datas and gives back either true or false
good example here is the one we use earlier (>=) this means greater than or equal to,
so then if the value is greater than or equal to (another value) then it will show TRUE
if not, then it will show false
]


--------- boolean expression ----------
the boolena expression is basically a data type which has only 2 outputs, true and false
one thing i always forget here is to capitalize the first letter (True and False) 
because i came from java and java script, on that language we can use uncapitalized letters


============================================
KEY VOCABULARY
============================================
- condition:
- if / elif / else:
- comparison operator:
- boolean expression:
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

money = 10
if money >= 7:
  print("you can have siomai and water")
elif money >= 5:
  print("you can buy siomai ")
else:
  print("buy candy instead")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

[
the mistakes i always made is forgetting the syntax, like using => instead of >=
i also always forgot the colon the after the if else statement
for example (else:) which i forgot all the time, because on java we used
else () {} which is the condition and the action, but on python it is much simplier (they say)
and one more thing i mentioned earlier which is forgetting to capitalize the first letter of True and False
]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
this is important to learn specially when working with oop (object oriented programming) and looping!!
which was our midterms last saturday, and i didnt review that well about while loop (or general looping) 
so i didnt know how to end the loop
if i should use "break" "end" or even "pass"
learning this and memorizing syntaxes will help alot in future developing

"""
