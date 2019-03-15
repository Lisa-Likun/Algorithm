


def main():

    n=int(input("n="))
    k=int(input("k="))
    position = input('Initial position of the zombies: ')
    i=0
    array = [None]*10
    for x in position.split(' '):
        array[i]=x
        print(array[i])
        i+=1
    minn=0 
    maxn=0
    for i in range(n):
        p=array[i]
        maxn=max(maxn, max(k-int(p)+1, int(p)))
        minn=max(minn, min(k-int(p)+1, int(p)))
    
    print(minn, maxn)

main()

