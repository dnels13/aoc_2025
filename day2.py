input_path = './inputs/day2.txt'
sample_input_path = './inputs/day2_sample.txt'

input = open(input_path, 'r')
ranges = input.read().split(',')
invalid_ids = []
for int_range in ranges:
  start, end = map(int, int_range.split('-'))

  for n in range(start, end+1):
    str_n = str(n)
    if len(str_n) % 2 != 0:
      continue

    first_half = str_n[:len(str_n)//2]
    second_half = str_n[len(str_n)//2:]
    if first_half == second_half:
      invalid_ids.append(str_n)


part1_solution = sum(map(int, invalid_ids))
print("Day 2 - Part 1: " + str(part1_solution))


##### PART 2 #####

def groups_of(text, group_size):
  groupings = []
  curr_text = ''
  for i in range(len(text)):
    if i % group_size == 0 and i > 0:
      groupings.append(curr_text)
      curr_text = ''

    curr_text += text[i]

  groupings.append(curr_text)
  return groupings

def has_identical_groups(arr):
  identical = True
  for group in arr:
    identical = identical and group == arr[0]

  return identical

invalid_ids = []
for int_range in ranges:
  start, end = map(int, int_range.split('-'))

  for n in range(start, end+1):
    str_n = str(n)

    for i in range(1, len(str_n) // 2 + 1):
      if len(str_n) % i > 0:
        continue

      groupings = groups_of(str_n, i)
      if has_identical_groups(groupings):
        invalid_ids.append(str_n)
        break

  # print('Range: ' + int_range)
  # print('Invalid IDs: ' + str(invalid_ids))

part2_solution = sum(map(int, invalid_ids))
print('Day 2 - Part 2: ' + str(part2_solution))




