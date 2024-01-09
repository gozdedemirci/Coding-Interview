def calc(nested, depth = 0):
  res = 0
  if type(nested) is list:
    for item in nested:
      res += calc(item, depth + 1)
  else:
    res += (nested * depth)
  return res

print(calc([[2, [9, 1, 3], 8], 1, 4])) # 64
print(calc([[[3, [2, 4]]], 3]))        # 36
