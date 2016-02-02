def factorial(n):
   """
   Return the product of all positive integers less than 
   or equal to n.

   Example:
   >>> factorial(3)
   6
   >>> factorial(4)
   24
   """ 
   if n <= 1:
	result = 1
   else:
       result = n * factorial(n-1)
   return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
