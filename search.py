#linear search
def search(arr, x):
        for i in range(len(arr)):
        	if arr[i] == x:
        		print(x,"found in",i,"index position")
#binary search
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and found==False):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
			print(item,"found in",mid,"index position")
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
list=[1,67,34,23]
search(list,34)
list.sort()
binary_search(list,34)