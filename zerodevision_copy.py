from time import sleep
a = int(input("Please provide First number:"))
b = int(input("Please provide Second number:"))

try:
    c = a/b
    sleep(5)
    assert 5==6

except KeyboardInterrupt:
    raise
except ZeroDivisionError:
    c = 0
except AssertionError:
    pass
print("\n\n{}/{}={}".format(a,b,c))
