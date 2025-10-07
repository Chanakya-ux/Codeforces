import sys
input = sys.stdin.readline
def solve():
  """
  Reads a permutation p and prints a valid permutation q.
  """
  # Read the size of the permutation. An empty line would cause an error here.
  
  #if not n_str: return # Handles case where input stream ends unexpectedly
  n = int(input())
  
  # Read the permutation p.
  p = list(map(int, input().split()))
  
  # Construct q using the correct formula.
  q = [(n + 1) - val for val in p]
  
  # Print the resulting permutation q.
  print(*q)

def main():
  """
  Handles multiple test cases.
  """
  # Read the number of test cases.
  
  #if not t_str: return # Handles empty input
  num_test_cases = int(input())

  # Loop through all test cases.
  for _ in range(num_test_cases):
    solve()

if __name__ == "__main__":
  main()