print("starting block")
a=[11,22,33]
#print(y)


try:
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
except:
        print("some exception raised")
else:
        print("no exception raised,everything worked perfectly")
finally:
    print("this is a final block")
print("outside try block")
