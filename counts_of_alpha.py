word = input()
     upperCount, lowerCount, specialCount = 0, 0, 0
     for ch in word:
         # some logic 
         if ch.isalpha():
             if ch.islower():
                 lowerCount += 1 
             else:
                 upperCount += 1 
         else:
             specialCount += 1 
 
     print("no.of upper-case characters", upperCount)
     print("no.of lower-case characters", lowerCount)
     print("no.of special characters", specialCount)
 
