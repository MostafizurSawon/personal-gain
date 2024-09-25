# input_string = input()

# numbers = input_string.split()

# width = float(numbers[0])
# height = float(numbers[1])
# radius = float(numbers[2])
# import math

# a = width**2 + height**2
# a = math.sqrt(a)
# b=radius*2

# if a <= b:
#   print("true")
# else:
#   print("false")


# input_string = input()

# numbers = input_string.split()

# a = int(numbers[0])
# b = int(numbers[1])

# ans = a - b*2

# if ans>=0:
#   print(ans)
# else:
#   print(ans*-1)


from collections import Counter

li = list(map(int, input().split()))

item_counts = Counter(li)
# print(item_counts)
for item, count in item_counts.items():
    if count%2:
      print(item)
      break
