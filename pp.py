
a=1

def pippo():
    global a
    a= 15
    print(a)
    

if __name__ == "__main__":
    #a = 10
    print(a)
    pippo()
    print(a)
    # output 1 15 15