import math as m

print(" |        sin(x)       |            x           |")
print(f" |       0.000000      |        6.283185        |")

def main():
    for i in range(1000):

        x = ((2*m.pi)-2*m.pi*((i+1)/1000))    #gives x in radians, m.sin(x) is for radians
        s=""
        if(m.sin(x) >= 0):
            s=" "
        
        print(f" |   {s}   {m.sin(x):.6f}      |        {x:.6f}        |")



if __name__ == "__main__":
    main()  