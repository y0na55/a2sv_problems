# n = len of the array
# m = sum of elements
# p  = len of segment
# q  = sum of the segment
# (1≤p≤n≤100, 1≤q,m≤100)

# p == q
# n = m


# He believes that if every segment of a fixed length p sums to the exact same value q, 
# the array achieves a state of "local resonance."
# However, he also needs the entire array of length n to sum to a total value m to satisfy the "global equilibrium."

# Raphael is obsessed with the concept of "The Harmonic Constraint." To him, an array isn't just a list of numbers; 
# it's a rhythm that must be perfectly balanced. 
# He believes that if every segment of a fixed length p sums to the exact same value q, the array achieves a state of "local resonance." 
# However, he also needs the entire array of length n to sum to a total value m to satisfy the "global equilibrium."

# His friends think he’s overcomplicating things, but Raphael is convinced that such arrays are the key to understanding the universe. 
# Can you help him determine if his dream array actually exists, or if he's chasing a mathematical ghost?

# Given four integers n, m, p, and q, 
# determine whether there exists an integer array a1,a2,…,an (elements may be negative) satisfying the following conditions:

#     The sum of all elements in the array is equal to m:
#     a1+a2+…+an=m
#     The sum of every p consecutive elements is equal to q:
#     ai+ai+1+…+ai+p−1=q, for all 1≤i≤n−p+1

# Input

# Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.

# The first and only line of each test case contains four integers n, m, p, and q (1≤p≤n≤100, 1≤q,m≤100) — the length of the array, 
# the sum of elements, the length of a segment, and the sum of a segment, respectively.

# Output

# For each test case, output "YES" (without quotes) if there exists an array satisfying the above conditions, and "NO" (without quotes) otherwise.

# You can output "YES" and "NO" in any case (for example, strings "yES", "yes", and "Yes" will all be recognized as valid responses).


# t = int(input())

# for _ in range(t):
#     n, m, p, q = map(int, input())


t = int(input())

for _ in range(t):
    n,m, p, q = map(int, input().split())
    
    if n % p == 0:
        if m == (n // p) * q:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")