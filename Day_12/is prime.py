"""wang

素数的判断
"""
def is_prime(num:int) ->bool:
  for i in range(2,int(num**0.5)+1):
      if num % i ==0:
          return False
  return True
print(is_prime(12))