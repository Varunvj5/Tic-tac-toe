print("Hello would u like me to know about u?(reply with yes or no):")
x=str(input())
if x == 'yes':
    print("What is your name?:")
    name=str(input())
    print(name,'!!! Wowww... what a beautifull name that is. Would you mind giving me your number?:')
    prm=str(input())

    if prm=='no':
        nmbr=int(input())
        print('Thanks a lot:)')
    else:
        print('No problem')
else:
    print('Have a good day ahead!!!')
