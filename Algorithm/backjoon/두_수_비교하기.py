def compare(A :int,B:int) :
    if A > B :
        return ">"
    elif A < B :
        return "<"
    else :
        return "=="

a = compare(1,2)
b = compare(10,2)
c = compare(5,5)

print(a,b,c)