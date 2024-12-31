def isBouncy(number):
  arrayNumber=list(str(number))
  sortedDigitsAscending=sorted(arrayNumber)
  digitsSortedDescending=sortedDigitsAscending[::-1]
  return  not (digitsSortedDescending==arrayNumber or sortedDigitsAscending==arrayNumber)
   

def calculate_bouncy_proportion(target_bouncy_percentage):
  decimal= target_bouncy_percentage/100
  bouncy=0
  notBouncy=0
  actualNumber=1
  actualpercentaje=0
  while actualpercentaje!=decimal:
    if isBouncy(actualNumber):
      bouncy+=1
    else:
      notBouncy+=1
    actualpercentaje=bouncy/(notBouncy+bouncy)
    actualNumber+=1
  return (actualpercentaje, actualNumber-1)



proportion, number = calculate_bouncy_proportion(99)
print(f'Number: {number}, proportion: {proportion}')