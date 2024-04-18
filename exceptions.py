print("starting block")
a=[11,22,33]
#print(y)


try:
 #a=10/2
  #print(a[5])
  print(a)
except ZeroDivisionError:
    print("exception raised due to zero division error")
except IndexError:
    print("exception raised due to index out of range")   
except NameError:
    print("exception raised due to undefined variable") 
except:
        print("some exception raised")
else:
        print("no exception raised,everything worked perfectly")
finally:
    print("this is a final block")
print("outside try block")
 
