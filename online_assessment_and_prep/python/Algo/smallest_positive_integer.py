def solution(A):
  # Set up a set to store the positive integers that occur in A
  positive_int_set = set()
  
  # Iterate through the elements of A and add the positive integers to the set
  for a in A:
    if a > 0:
      positive_int_set.add(a)
  
  # Start the counter at 1, since we want to find the smallest positive integer
  # that does not occur in A
  counter = 1
  
  # While the counter is in the set of positive integers that occur in A,
  # increment the counter
  while counter in positive_int_set:
    counter += 1
  
  # Return the counter when we exit the loop, since this will be the smallest
  # positive integer that does not occur in A
  return counter

    # Fill this in.
  set


print(solution([1, 3, 6, 4, 1, 2]))




# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].