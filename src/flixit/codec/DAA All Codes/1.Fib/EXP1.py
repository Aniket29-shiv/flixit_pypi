# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("Enter the number of terms: "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer!")

# If there is only one term, return n1
elif nterms == 1:
   print(f"Fibonacci sequence upto {nterms}: ")
   print(n1)

# Generate fibonacci sequence
else:
   print(f"Fibonacci sequence upto {nterms}: ")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
