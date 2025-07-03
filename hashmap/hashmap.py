#your hosting a party but each person cant use their real name

my_party={}

while True:

    realname=input("enter your real name(stop to quit): ").lower()
    nickname=input("enter your nick name: ")
    if realname=='stop':
        break
    else:
        my_party[realname]=nickname
print("your list of party participats with their nickname",my_party)
