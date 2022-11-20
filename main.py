# my2DList = [ ["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"] ]

# print(my2DList[1])

# This code outputs ['Johnny', 21, 'Mac'].
# my2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]

# print(my2DList[0][0])
# This code outputs 'Johnny'. It's Johnny's name from list 0 (first square bracket), item 0 (second square bracket)

# print(my2DList[1][2])
# This code outputs 'PC'. It's Sian's computing preferene from list 1 (first square bracket), item 2 (second square bracket)



# my2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]

# my2DList[1][2] = "Linux"
# The line above changes list 1, item 2 from PC to Linux

# print(my2DList[1])
# I'm using this line to output list 1 to check that the change has happened correctly.


# my2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]

# print(my2DList[0][2])



# my2DList =  [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]

# print(my2DList[0][1])



import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()