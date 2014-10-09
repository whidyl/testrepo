import math

class Vector3:
  def __init__(self, x = 0,y = 0,z = 0):
    self.x = x
    self.y = y
    self.z = z
  def add(v):
    self.x += v.x
    self.y += v.y
    self.z += v.z
  def sub(v):
    self.x -= v.x
    self.y -= v.y
    self.z -= v.z
  def mult(n):
    self.x *= n
    self.y *= n
    self.z *= n
  def div(n):
    self.x /= n
    self.y /= n
    self.z /= n
  def mag():
    return math.sqrt(self.x * self.x + self.y * self.y)
  def normalize():
    self.div(self.mag)
