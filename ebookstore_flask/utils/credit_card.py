def luhn_algorithm(number: str):
   digits = [int(d) for d in reversed(number)]
   result = [digit*2-9 if idx%2==1 and digit*2>9 else digit*2 if idx%2==1 else digit for idx,digit in enumerate(digits)]
   total = sum(result)
   return total%10==0

def bin_number_checker(number: int):
   number = int(number)
   import pandas as pd, os
   data = pd.read_csv(os.path.join(os.getcwd(), "binlist.csv"))
   data1 = data[data['BIN'] == number]
   if data1.empty: return {'Brand': 'N/A', 'Issuer': 'N/A'}
   result = data1[['Brand', 'Issuer']].iloc[0].to_dict()
   result['Brand'] = result['Brand'].title()
   result['Issuer'] = result['Issuer'].title()
   return result