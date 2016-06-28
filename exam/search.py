# BINARY SEARCH

def bin(x,z):
	low=0
	high=len(x)-1
	while high-low>1:
		mid=int(round((high+low)/2))
		if z >= x[mid]:	low=mid
		else: high=mid
	return low
