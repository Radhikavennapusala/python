numbers=[12,14,5,7,9]
even_count =sum(1 for num in numbers if num%2==0)
odd_count =sum(1 for num in numbers if num%2==0)
print(f"even number count:",even_count)
print(f"odd number count:",odd_count)