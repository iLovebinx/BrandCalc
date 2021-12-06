import math
import statistics


print ("██████╗░██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░░█████╗░██╗░░░░░░█████╗░")
print ("██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗")
print ("██████╦╝██████╔╝███████║██╔██╗██║██║░░██║██║░░╚═╝███████║██║░░░░░██║░░╚═╝")
print ("██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║██║░░██╗██╔══██║██║░░░░░██║░░██╗")
print ("██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██║░░██║███████╗╚█████╔╝")
print ("╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░")
print ("by brandon")

print (                                                                                )







OriginQ = input (
    "1 : Basic Arithmitic\n" 
    "2 : Complex Math\n"
    "3 : Collatz Checker\n"

)



def statisticsCalc():

     input_string = input('Enter elements of a list separated by space ')
     print("\n")
     listSTDev = input_string.split()

     print('Data: ', listSTDev)    

     for i in range(len(listSTDev)):
          
          listSTDev[i] = int(listSTDev[i])


     def mean (x): 
          return statistics.mean(x)

     def stDev (x): 
          return statistics.stdev(x)

     def mode (x): 
          return statistics.mode(x)

     def median (x): 
          return statistics.median(x)

     def medianLow (x): 
          return statistics.median_low(x)

     def medianHigh (x): 
          return statistics.median_high(x)
     
     
     meanResult = mean (listSTDev)
     stdev = stDev (listSTDev)
     modeResult = mode (listSTDev)
     medianResult = median (listSTDev)
     q1Result = medianLow (listSTDev)
     q2Reuslt = medianHigh (listSTDev)


     print ("Results")
     print ("Mean: "+ str(meanResult))
     print ("Median: "+ str(medianResult))
     print ("Mode: "+ str(modeResult)) 
     print ("Q1: "+ str(q1Result))
     print ("Q2: "+ str(q2Reuslt))
     print ("Standard Deviation: "+ str(stdev))
     
def BasicMath ():

     opperation = input (

     "1 : Add\n" 
     "2 : Subtract\n"
     "3 : Divide\n"
     "4 : Modulo\n"
     
     )
     
     


     number1 = input ("mumber 1")
     number2 = input ("number 2")

     
     def calculateAdd (num0, num1):
          return (int(num0) + int(num1))

     def calculateSubtract (num0, num1):
          return (int(num0) - int(num1))

     def calculateDivide (num0, num1):
          return (int(num0) / int(num1))

     def calculateMod (num0, num1):
          return (int(num0) % int(num1))

     


     result_add = (calculateAdd(number1, number2))
     result_subtract = (calculateSubtract(number1, number2))
     result_divide = (calculateDivide(number1, number2))
     result_mod = (calculateMod(number1, number2))


     if opperation == ("1"):
          print (number1 + "+" + number2 + "=" + result_add)
          
     elif opperation == ("2"):
          print (number1 + "-" + number2 + "=" + result_subtract)
    
     elif opperation == ("3"):
          print (number1 + "/" + number2 + "=" + result_divide)

     elif opperation == ("4"):
          print (number1 + "mod" + number2 + "=" + result_mod)

     else:
          print ("invalid input")

def collatz ():
     
     CollatzNumber = input ("enter any number from one to infinity")
     iteration = 0


     def calculateCollatzEven (num0):
          return float (num0) / 2

     def calculateColaltzOdd (num1):
          return float (num1) * 3 + 1 


     while float(CollatzNumber) > 1:

          if float(CollatzNumber) % 2 == 0:
               CollatzNumber = calculateCollatzEven (CollatzNumber)
          
     
     else:
          CollatzNumber = calculateColaltzOdd (CollatzNumber)
     
     iteration = iteration + 1

     
     print (iteration, float(CollatzNumber))
     
     if iteration >= 62118:
          print ("the amount of steps has been greater than the record amount, I would advise bringing this number to a research team !")


     print ("better luck next time this number had a total of " + str(iteration) + " iterations before stoping to 4, 2, 1")

if OriginQ == ("1" or "BasicMath" or "basic math"):
     BasicMath ()

elif OriginQ == ("2" or "statisitics" or "stat"):
     statisticsCalc ()


elif OriginQ == ("3" or "Collatz Checker" or "collatz checker"):
     collatz ()






















