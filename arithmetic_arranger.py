
def arithmetic_arranger(problems, boolean = False):

  splitted = split_problems(problems)

  #Error handlers
  if too_many_problems(problems) == True:
    return "Error: Too many problems."

  if invalid_operator(problems) == True:
    return "Error: Operator must be '+' or '-'."
  if too_many_digits(splitted) == True:
    return "Error: Numbers cannot be more than four digits."
  if only_numbers(splitted) == True:
    return "Error: Numbers must only contain digits."
  return resolve(splitted, boolean)


def convert(string):
  try:
    string_int = int(string)
    return string_int
  except ValueError:
    return False

def operate(array, boolean):
  result = 0
  width = len(array[0]) if len(array[0]) > len(array[2])  else len(array[2])
  hyphens = "".rjust(width + 2, "-")
  second_width = (width + 1 - len(array[2]))
  
  space = "".rjust(second_width)

  if array[1] == "+":
    result = int(array[0]) + int(array[2])
  else:
    result = int(array[0]) - int(array[2])
  first_line = (array[0]+ "\n").rjust(width+3)
  pre_second_line = array[1] + space + array[2] + "\n"
  second_line = (pre_second_line).rjust(width+3)
  pre_third_line = hyphens
  third_line_width = width+2
  if boolean == True:
    pre_third_line += "\n"
    third_line_width += 1
  third_line = pre_third_line.rjust(third_line_width)
  fourth_line = str(result).rjust(width+2)
  render =  first_line +  second_line + third_line
  if boolean == True:
    render += fourth_line
  return render

def too_many_problems(problems):
  if len(problems) > 5:
      return True

def invalid_operator(problems):
  splitted = []
  arranged_problems = ""
  for i in problems:
    splitted.append(i.split(' '))
  for i in splitted:
    if i[1] == "*" or i[1] == "/":
      return True

def split_problems(problems):
  splitted = []
  for i in problems:
    splitted.append(i.split(' '))
  return splitted

def too_many_digits(splitted):
  for i in splitted:
    if len(i[0]) > 4 or len(i[2]) > 4:
      return True

def only_numbers(splitted):
  for i in splitted:
    if convert(i[0]) == False or convert(i[2]) == False:
      return True

def resolve(splitted, boolean):
  all = []
  result = ""
  for i in splitted:
    all.append(operate(i, boolean))
  if len(all) == 1:
    return all[0]
  elif len(all) == 2:
    result = "\n".join(["    ".join(elem) for elem in zip(all[0].split("\n"),all[1].split("\n"))])
  elif len(all) == 3:
    result = "\n".join(["    ".join(elem) for elem in zip(all[0].split("\n"),all[1].split("\n"), all[2].split("\n"))])
  elif len(all) == 4:
    result = "\n".join(["    ".join(elem) for elem in zip(all[0].split("\n"),all[1].split("\n"), all[2].split("\n"), all[3].split("\n"))])
  elif len(all) == 5:
    result = "\n".join(["    ".join(elem) for elem in zip(all[0].split("\n"),all[1].split("\n"), all[2].split("\n"), all[3].split("\n"), all[4].split("\n"))])
  
  return result
