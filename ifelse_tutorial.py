if __name__ == '__main__':
    try:
        n = 18
        if (n%2==1):
            print ("Weird")
        elif (n%2==0):
            if(n>=2 and n<=5):
                print("Not Weird")
            elif (n>=6 and n<=20):
                print ("Weird")
            else:
                print ("Not Weird")
    except ValueError:
        print("Not a valid number.  Try again...")