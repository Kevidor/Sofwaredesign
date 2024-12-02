def bubble_sort(a_list):
  n = len(a_list)
  for i in range(0, n-1):
    for j in range(0, n-i-1):
      if a_list[j] > a_list[j+1]:
        a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        #tuple assignment for swap
  return a_list

a_list = [1, 16, 8, 3, 25, 94, 46]
print(bubble_sort(a_list))