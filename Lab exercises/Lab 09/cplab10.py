def countup_timer(i,n):
    #base case
    if(i>n):
        return 0
    else:
      print(i)
      countup_timer(i+1,n)
#recursive function
f __name__=='__main__':
    n=int(input("enter number"))
    i=1
    countup_timer(i,n)