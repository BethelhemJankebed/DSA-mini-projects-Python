#assume that we have a collection of musical disks in which we want to order in alphabetical order

print('I Heard that your a big fan of music so lets see some of your top 10 muscians ')

singer=[]

def quick_sort(arr):

    if len(arr)<=1:
        return arr

    pivot=arr[-1]
    left=[]
    right=[]

    for i in range(len(arr)-1):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
        
    left_sorted=quick_sort(left)
    right_sorted=quick_sort(right)

    return left_sorted + [pivot] + right_sorted


 #collect input from user   
for i in range(5):

    musican=input('enter your favoriate musician: ')

    singer.append(musican)
sorted_singer=quick_sort(singer)

print('your amazing musician list is: ')

for artists in sorted_singer:
    print(artists)