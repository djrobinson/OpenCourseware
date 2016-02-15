# https://opentechschool.github.io/python-beginners/en/loops.html

# for name in "Danny", "Jeff", "Mary":
#   print("Haldo " + name)

# for i in range(10):
#   print(i)

# total = 0
# for i in 5, 7, 11, 13:
#   print(i)
#   total = total + i

# print(total)

# for _ in range(10):
#   print("haldo")

snake = ""
# for i in range(10):
#   snake = " ---" + snake
#   print(snake)

for i in range(10):
  snake = snake + " " + "-"* i
  print(snake + ">")