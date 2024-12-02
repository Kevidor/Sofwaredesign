def insertion_sort(a_list):
  n = len(a_list) 
  for i in range(1, n):
    elem = a_list[i]
    while i > 0 and a_list[i -1] > elem: # sorting of sublist
      a_list[i] = a_list[i -1]
      i = i -1
    a_list[i] = elem
  return a_list

a_list = [1, 16, 8, 3, 25, 94, 46]
print(insertion_sort(a_list))