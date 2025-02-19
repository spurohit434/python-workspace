def catch():
    try:
        raise Exception("IO exception")
    except Exception as e:
        print( e.args)


def catch1():
    try:
        raise Exception("IO exception")
    except:
        pass

catch1()


