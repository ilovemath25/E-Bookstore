def luhn_algorithm(number: str):
   digits = [int(d) for d in reversed(number)]
   result = [digit*2-9 if idx%2==1 and digit*2>9 else digit*2 if idx%2==1 else digit for idx,digit in enumerate(digits)]
   total = sum(result)
   return total%10==0