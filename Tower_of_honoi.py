def TOH(numbers,start,aux,end):
    if numbers==1:
        print("Move disk 1 from red {} to rod {}".format(start,end))
        return
    TOH(numbers-1,start,end,aux)
    print("Move disk {} from rod {} to rod {}".format(numbers,start,end))
    TOH(numbers-1,aux,start,end)
disc=2
TOH(disc,"A","B","c")


 