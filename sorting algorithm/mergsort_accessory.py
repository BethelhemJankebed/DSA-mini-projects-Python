#we will sort the accessories we have according to their alphabetical order

items=[]

def merge_sort(arr):

    if len(arr)<=1:
        return arr
    
    else:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        left_sorted=merge_sort(left)
        right_sorted=merge_sort(right)

        i=0
        j=0
        merge=[]

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i]<right_sorted[j]:
                merge.append(left_sorted[i])
            else:
                merge.append(right_sorted[j])
        merged += left_sorted[i:]
        merged += right_sorted[j:]

    return merge



#collecting input
while True:
    accessory=input('enter the accessories you own(write STOP to exit): ')
    if accessory=='STOP':
        break
    else:
        items.append(accessory)

sorted_merge=merge_sort(items)

print('your accessories are: ')
print(sorted_merge)
