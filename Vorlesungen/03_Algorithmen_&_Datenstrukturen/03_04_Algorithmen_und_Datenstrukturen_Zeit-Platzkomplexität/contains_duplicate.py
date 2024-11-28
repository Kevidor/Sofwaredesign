def contains_duplicates(array):
  for i, outer in enumerate(array):
    for j, inner in enumerate(array):
      if i != j and outer == inner:
        return True
  return False

array = [0, 2, 5, 8, 3, 5, 3, 1, 7, 9]
has_dupes = contains_duplicates(array)