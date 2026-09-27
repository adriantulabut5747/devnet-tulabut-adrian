"""
Module 2 — Lesson 3: Loops & Lists
Student: [Tulabut Adrian A]
Date: [9-27-26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[

--------- list ----------
list is basically a container or a box, inside the list are items 
and those items are stored in one variable, so for example we have a pencil case (which is the list)
and there are pencil inside (which is the items inside the list)
pencilcase = ["blackpencil", "redpencil", "whitepencil"]

--------- for loop ----------
for loop is a loop that repeats the block of code once for each items
so for example i want to loop the list we made earlier
pencilcase = ["blackpencil", "redpencil", "whitepencil"]
for pencil in pencilcase:
  print(pencil)
]
and the output would be those 3 pencils we have
blackpencil redpencil whitepencil


--------- while loop ----------
base on my understanding, while loop is similar to the for loop
but were using "while" instead of "for" and the main difference here
is that it will only continue to loop if the statement or the value you 
assigned it to is True,

money = 10: #assigning variable
while money = 10: #condition statement
print ("i am so yaman") #output if the condition statement is true
money = money - 5  #spend 5 pesos each time so we have a way to break the loop
print ("im not yaman anymore") #prints a different output to let user knows money is not = to 10 


--------- index ----------
indexing is using a square bracket to specify a posion, for example on the list we have earlier
pencilcase = ["blackpencil", "redpencil", "whitepencil"]
print(pencil[1])

in this case the blackpencil is not the #1 on the list,
if i print the code above, it will print red pencil because in coding,
number 0 always comes first, so in the list i made earlier, number 0 us the black pencil, therefore
its the first one, and the red pencil would be the second one and the red pencil id is [1]


--------- iteration ----------
iteration is one round of the loop, so if the loop runs around 3 times
then thats 3 iterations
for example on the 
pencilcase = ["blackpencil", "redpencil", "whitepencil"]
for pencil in pencilcase:
  print(pencil)
there are 3 pencil on that list so the loop will do 3 iterations 
and then it will stop if there are no pencil left

============================================
KEY VOCABULARY
============================================
- list:
- for loop:
- while loop:
- index:
- iteration:
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

pencilcase = ["blackpencil", "redpencil", "whitepencil"]
for pencil in pencilcase:
  print(pencil)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[i always forgot how to break a loop, and sometimes i dont even break the loop
if i should use end, break, or, theyre all different so you need to memorize their syntaxes
cuz loops are no doubt one of the most confusing thing in coding
]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
