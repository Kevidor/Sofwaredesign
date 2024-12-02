def merge_sort(a_list):
  n = len(a_list)
  if n > 1:
    mid = n // 2
    lefthalf = a_list[:mid]
    righthalf = a_list[mid:]
    
    merge_sort(lefthalf)
    merge_sort(righthalf)

    i=j=k=0
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] <= righthalf[j]:
        a_list[k]=lefthalf[i]
        i=i+1
      else:
        a_list[k]=righthalf[j]
        j=j+1
      k=k+1

    while i < len(lefthalf):
      a_list[k]=lefthalf[i]
      i=i+1
      k=k+1
      
    while j < len(righthalf):
      a_list[k]=righthalf[j]
      j=j+1
      k=k+1
        
a_list = [1, 16, 8, 3, 25, 94, 46]
merge_sort(a_list)
print(a_list)