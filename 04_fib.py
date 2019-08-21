def labbits(n, k):
   if n == 0:
   	return 0
   if n == 1:
   	return 1
   else:
   	return labbits(n-1, k) + k*labbits(n-2, k)
print labbits(29,4)
