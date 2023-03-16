def getNumbers():
    f = open('ch8p4.txt', 'w')
    userinput=input('Enter an integer or type Q to exit:\t')
    while userinput != 'Q' :

        try :
            num = int(userinput)
            f.write(userinput + "\n")
        except:
            print('Input is not an integer and will be ignored')
        finally:
            userinput=input('Enter an integer or type Q to exit:\t')

    f.close()



def findSum():
    f=open('ch8p4.txt', 'r')
    som=0
    for line in f:

        som=som+int(line)
    print(som)
    f.close()


print(findSum())



