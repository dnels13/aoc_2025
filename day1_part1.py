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


input = open('./inputs/day1_part1.txt', 'r') # question
password = 0  # answer

rotations = input.read().split("\n")
lock = Lock(100, 50)
for rotation in rotations:
  lock.process_rotation(rotation)
  if lock.position == 0:
    password += 1

print("DAY 1.1\n\npassword: " + str(password))
