class Lock:
  """A Simple Lock"""

  def __init__(self, size, position):
    self.size = size
    self.position = position

  def rotate_right(self, clicks):
    self.position = (self.position + clicks) % self.size

  def rotate_left(self, clicks):
    self.position = (self.position - clicks) % self.size

  def process_rotation(self, rotation):
    clicks = int(rotation[1:])
    if rotation[0] == 'R':
      self.rotate_right(clicks)
    else:
      self.rotate_left(clicks)

  def count_full_rotations(self, rotation):
    clicks = int(rotation[1:])
    full_rotations = 0

    if rotation[0] == 'R':
      full_rotations = (self.position + clicks) // self.size
    else:
      if self.position - clicks <= 0:
        full_rotations = (self.position - clicks) // self.size

    return abs(full_rotations)

input = open('./inputs/day1_part1.txt', 'r') # question
password = 0  # answer

rotations = input.read().split("\n")
lock = Lock(100, 50)
for rotation in rotations:
  lock.process_rotation(rotation)
  if lock.position == 0:
    password += 1

print("DAY 1.1\npassword: " + str(password) + "\n")

##### PART 2 #####
password = 0

lock2 = Lock(100, 50)
for rotation in rotations:
  password += lock2.count_full_rotations(rotation)
  lock2.process_rotation(rotation)

print("DAY 1.2\npassword: " + str(password))
