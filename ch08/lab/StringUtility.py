class StringUtility():
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string


def vowels(self):
    count = 0
    for i in self.string:
      vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
      if i in vowels:
        count += 1
    if count < 5:
      return f"{count}"
    else:
      return "many"

      
  def bothEnds(self): 
      length = len(self.string)
      if length > 0:
        return f"{self.string[0]}{self.string[1]}{self.string[length-2]}{self.string[length-1]}"
      else:
        return ""