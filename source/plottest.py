def main():
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(0,10,50)
    y=np.cos(x)
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("cos(x)")
    plt.show()

if __name__=="__main__":
    main()    