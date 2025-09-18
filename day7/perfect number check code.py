n = int(input())
sum_divisors = sum(i for i in range(1, n) if n % i == 0)
print("YES" if sum_divisors == n else "NO")
