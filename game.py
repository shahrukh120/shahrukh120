# DISPLAY PART

l='_|_|_\n_|_|_\n | | '


def diplay():
    print(l)
    return 

# VERIFICATION PART

def varify():
    change=False
    while change==False:
        c =input(('choose the position: '))
        
            
           
        if c in ['1','2','3','4','5','6','7','8','9']:

            change=True
        else:
            print('please provide the valid input')
            change=False

    return c        

# POSITIONING PART

def position(c,g):
    i=a[c]
    h=0


    li=list(l)
    while h<17:

        
        if h==i:
            

            
           
            if g%2==0 and (li[h]!='X' or li[h]!='O'):
            
                li[h]='X'
                
            elif g%2!=0 and (li[h]!='X' or li[h]!='O'):

                li[h]='O'
            else:
                print('sryy already taken try again !')
        
        else:
            pass
       
        h=h+1 

    return ''.join(li)





















#GAME PROCESS

l='_|_|_\n_|_|_\n | | '
a={'1':0,'2':2,'3':4,'4':6,'5':8,'6':10,'7':12,'8':14,'9':16}

game=True
g=0
while game==True:
    if (l[0]==l[2]==l[4]=='X') or(l[6]==l[8]==l[10]=='X') or (l[12]==l[14]==l[16]=='X') or(l[0]==l[8]==l[16]=='X') or(l[4]==l[8]==l[12]=='X') or(l[0]==l[6]==l[12]=='X') or(l[2]==l[8]==l[14]=='X')or(l[4]==l[10]==l[16]=='X'):
        print(l) 
        print('X owner win')
        
        
        ask=input("wanna play again ? : ")
        if ask=='y':
            l='_|_|_\n_|_|_\n | | '
            game=True
            
        elif ask=='n':
            game=False
            print('Ok thank you for playing !')
        
    elif (l[0]==l[2]==l[4]=='O') or(l[6]==l[8]==l[10]=='O') or (l[12]==l[14]==l[16]=='O') or(l[0]==l[8]==l[16]=='O') or(l[4]==l[8]==l[12]=='O')or(l[0]==l[6]==l[12]=='O')or(l[2]==l[8]==l[14]=='O')or(l[4]==l[10]==l[16]=='O'):
        print(l) 
        print('O owner win')
        
        
        ask=input("wanna play again ? : ")
        if ask=='y':
            l='_|_|_\n_|_|_\n | | '
            game=True



                    
        elif ask=='n':
            game=False
            print('Ok thank you for playing !')
    elif ('_'not in l) and (' ' not in l):
        print('DRAW')
        print(l)
        
        
        ask=input("wanna play again ? : ")
        if ask=='y':
            l='_|_|_\n_|_|_\n | | '
            game=True
            
        elif ask=='n':
            game=False
            print('Ok thank you for playing !')
    else:
        game=True
        
        diplay()

        c=varify()
        r=position(c,g)
        l=r
        g=g+1
   
       

