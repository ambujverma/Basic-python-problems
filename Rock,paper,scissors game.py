import sys
user_1 =input("1st player's name :")
user_2 =input("2nd player's name :")
user1_answer = input("%s <<< do you want to choose (rock, paper and scissors) :>>>"%user_1)
user2_answer = input("%s <<< do you want to choose (rock, paper and scissors) :>>>"%user_2)
def campare(u1,u_1,u2,u_2):
        if u1==u2:
            return("game tie")
        elif u1== 'rock':
            if u2=='scissors':
                return("%s >> (rock) wins"%u_1)
            else:
                return("%s >> (paper) wins"%u_2)
        elif u1=='paper':
            if u2=='rock':
                return("%s >> (paper) wins"%u_1)
            else:
                return("%s >> (scissors) wins"%u_2)
        elif u1=='scissors':
            if u2=='paper':
                return("%s >> (scissors) wins"%u_1)
            else:
                return("%s >> (rock) wins"%u_2)
        else:
            return("invalid input")
            sys.exit()
            
print(campare(user1_answer,user_1,user2_answer,user_2))
