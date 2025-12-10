class BatteryBank:
  """sequence of digits"""

  def __init__(self, digits_string):
    self.digits = list(map(int, list(digits_string)))
    self.voltage = ''

  # deprecate this solution in favor of part 2
  def find_highest_voltage(self):
    max_digit = max(self.digits)
    index_of_max = self.digits.index(max_digit)
    if self.digits.index(max_digit) == len(self.digits) - 1:
      n2 = max(self.digits[:len(self.digits) - 1])
      self.voltage += str(n2) + str(max_digit)
    else:
      second_max_digit = max(self.digits[index_of_max + 1:])
      self.voltage += str(max_digit) + str(second_max_digit)

  # Part 2
  def activate_max_batteries(self, qty):
    left_bound = 0
    while qty > 0:
      right_bound = len(self.digits) + 1 - qty
      digits_sub_arr = self.digits[left_bound:right_bound]
      max_digit = max(digits_sub_arr)
      self.voltage += str(max_digit)

      left_bound += digits_sub_arr.index(max_digit) + 1 # left bound is inclusive, don't want to duplicate digits
      qty -= 1


input_path = './inputs/day3.txt'
sample_input_path = './inputs/day3_sample.txt'
lines = open(input_path, 'r').read().split('\n')

highest_voltages_arr = []
for line in lines:
  bank = BatteryBank(line)
  bank.activate_max_batteries(2)
  highest_voltages_arr.append(int(bank.voltage))

part1_solution = sum(highest_voltages_arr)
print("Part 1: " + str(part1_solution))

##### PART DEUX #####

voltage_arr = []
for line in lines:
  bank = BatteryBank(line)
  bank.activate_max_batteries(12)
  voltage_arr.append(int(bank.voltage))

part2_solution = sum(voltage_arr)
print("Part 2: " + str(part2_solution))
