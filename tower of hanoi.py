def hanoi(disk,source,destination,auxilary):
   if disk==1:
        print("Move disk from source to destination")
   else:
        hanoi(disk-1,source,auxilary,destination)
        print("Move disk from",source,"to",destination)
        hanoi(disk-1,auxilary,destination,source)
disk=int(input("enter the number of disk:"))
hanoi(disk,"Source","Destination","Auxilary")
