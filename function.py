def subtractor(a,b):
    """I subtract b from a and return result"""
    print("My name is {}".format(subtractor.__name__))
    print("I subtract {} and {}".format(a,b))
    return a-b

if __name__=='__main__':
    print("result is {}".format(subtractor(3,2)))