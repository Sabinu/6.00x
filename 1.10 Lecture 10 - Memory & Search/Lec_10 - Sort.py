# Selection sort

def selSort(L):
	"""
	@param: list

	Sorts the list & modifies it.
	"""
	for i in range(len(L)-1):
		minIndx = i
		minVal = L[i]
		j = i + 1
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal = L[j]
			j += 1
		temp = L[i]
		L[i] = L[minIndx]
		L[minIndx] = temp
	return None