input = open('./inputs/day1.txt', 'r')

lines = input.read().split("\n")
dial = 50
pwd = 0
for line in lines:
  direction = line[0]
  clicks = int(line[1:])

  for click in range(clicks):
    if direction == 'R':
      dial += 1
    else:
      dial -= 1

    if dial % 100 == 0:
      pwd += 1

  dial %= 100

print(pwd)