from time import sleep
a = int(input("Please provide First number:"))
b = int(input("Please provide Second number:"))

try:
    c = a/b
    sleep(5)

except KeyboardInterrupt:
    print("\n\n{}/{}={}".format(a,b,c))
    raise
except:
    c = -10

print("\n\n{}/{}={}".format(a,b,c))
