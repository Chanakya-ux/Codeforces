                            #ANOTHER DIVISIBILITY PROBLEM 


def solve():
  """
  This function reads an integer x and prints a valid y.
  The simplest solution that always works is y = 2 * x.
  """
  try:
    # Read the integer x for the current test case
    x = int(input())
    
    # Calculate y = 2 * x
    y = 2 * x
    
    # Print the result
    print(y)
  except (IOError, ValueError):
    # This handles potential errors with input, though it's
    # not strictly necessary on most competitive programming platforms.
    pass

def main():
  """
  Main function to handle multiple test cases.
  """
  try:
    # Read the number of test cases
    num_test_cases = int(input())
  except (IOError, ValueError):
    num_test_cases = 0

  # Loop through all test cases
  for _ in range(num_test_cases):
    solve()

if __name__ == "__main__":
  main()