import numpy as np


class Item:
  """This class has the attributes file_name="fname", desired_value="value"
  array1d_of_data="array", shape_of_array="_shape".

  All data is in 1D array form.
  """
  _shape = (10,10) # the shape of the matrix data
  def __init__(self,fname=""):
    self.fname = fname
    self.value = 0
    self.array = None
    if fname:
      self.load_file()

  def load_file(self):
    with open(self.fname,"r") as file:
      self.value = int(file.readline().strip())
      matrix = []

      def return_1(character):
        if character==".":
          return -1
        return 1

      for line in file.read().split("\n"):
        if len(line)>1:
          matrix.extend([return_1(char) for char in line.split()])

      self.array = np.array(matrix,float).reshape(Item._shape)


  def __repr__(self):
    array = self.array.reshape(*Item._shape).copy()
    char = str(self.value)+">>\n"
    for i in range(Item._shape[0]):
      for j in range(Item._shape[1]):
        if array[i,j] == -1:
          char += " "
        else:
          char += "*"
      char += "\n"
    return char # >>> terminal

  def __str__(self):
    array = self.array.reshape(*Item._shape).copy()
    char = "\n\033[91;103mMy value is \033[91;5m "
    char += "{:2d}".format(self.value)
    char += 5*" " + "\033[m\n"
    for i in range(Item._shape[0]):
      for j in range(Item._shape[1]):
        if array[i,j] == -1:
          char += "\033[47m  \033[m"
        else:
          char += "\033[44m  \033[m"
      char += "\n"
    return char # >>> terminal
