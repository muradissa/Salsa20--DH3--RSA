from globals import *
from User import User
#import msvcrt
import sys
#dh.generate_p_and_g()

users = [User("Alice","123"),  User("George", "0245"),User("Bob", "3165")]


generate_mutual_K_for_3(users[0], users[1], users[2])

print(f"{users[0].name} mutual : {users[0].dh_mutual_key}")
print(f"{users[1].name} mutual : {users[1].dh_mutual_key}")
print(f"{users[2].name} mutual : {users[2].dh_mutual_key}")
####### Start UI #######

print("\n\n***press 'esc' to quit***")
while True :

    print("\nSend a message from: ")
    for i in range (0, len(users)):
        print(f"\tpress ({i + 1}) for {users[i].name}")

    #ch = msvcrt.getch()
    #ch = sys.stdin.read(1)
    ch = input()
    ch = ord(ch[0])

    if ch == 27:
        break;
    if ch < 49 or ch >= 49 + len(users):
        print("\n**Error input, please try agian\n")
    else:
        msg = input('Enter the message : \n')
        users[int(ch)- 49].send_msg(msg)
        ####### Information Start #######
        print(f"\nPublic message is : {str_msg['msg']}\n\nSigniture is : {str_msg['signiture']}\n\n")
        for user in users:
            print(f"{user.name} got : {user.get_msg()}")
        ####### Information End #######

####### End UI #######

    
    
