#Serafeim Themistokleous A.M. 4555

import random

pinakas1=['1','2','3','4','5']
pinakas2=['a','b','c','d','e']
PCpos=[]
lista=0
pi1=0
pi2=0
bombs=[]
bombs2=[]
Y=True
Y1=True

def OX(miss):
    miss=list(M2)
    m=int(miss[1])
    if miss[0]=='a':
        a[m-1]='x'
    if miss[0]=='b':
        b[m-1]='x'
    if miss[0]=='c':
        c[m-1]='x'
    if miss[0]=='d':
        d[m-1]='x'
    if miss[0]=='e':
        e[m-1]='x'    

def OX1(miss):
    miss=list(M1)
    m=int(miss[1])
    if miss[0]=='a':
        a2[m-1]='x'
    if miss[0]=='b':
        b2[m-1]='x'
    if miss[0]=='c':
        c2[m-1]='x'
    if miss[0]=='d':
        d2[m-1]='x'
    if miss[0]=='e':
        e2[m-1]='x'    

def XO1(hit):
    hit=list(M1)
    h=int(hit[1])
    if hit[0]=='a':
        a2[h-1]='o'
    if hit[0]=='b':
        b2[h-1]='o'
    if hit[0]=='c':
        c2[h-1]='o'
    if hit[0]=='d':
        d2[h-1]='o'
    if hit[0]=='e':
        e2[h-1]='o'    

def XO(hit):
    hit=list(M2)
    h=int(hit[1])
    if hit[0]=='a':
        a[h-1]='o'
    if hit[0]=='b':
        b[h-1]='o'
    if hit[0]=='c':
        c[h-1]='o'
    if hit[0]=='d':
        d[h-1]='0'
    if hit[0]=='e':
        e[h-1]='o'    
        

def pcShips(pi1,pi2):
    for i in range(5):
        pi1=random.choice(pinakas1)
        pi2=random.choice(pinakas2)
        pi=pi2+pi1
        if pi not in PCpos:
              PCpos.append(pi)
    if len(PCpos)==4:
        pi1=random.choice(pinakas1)
        pi2=random.choice(pinakas2)
        pi=pi2+pi1
        if pi not in PCpos:
              PCpos.append(pi)
    return PCpos

loc=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']
locpc=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']
p1pos=[]
p2pos=[]

a=[' ',' ',' ',' ',' ']
b=[' ',' ',' ',' ',' ']
c=[' ',' ',' ',' ',' ']
d=[' ',' ',' ',' ',' ']
e=[' ',' ',' ',' ',' ']
a2=[' ',' ',' ',' ',' ']
b2=[' ',' ',' ',' ',' ']
c2=[' ',' ',' ',' ',' ']
d2=[' ',' ',' ',' ',' ']
e2=[' ',' ',' ',' ',' ']
    
print('BATTLESHIP GAME')
print('The objective is to sink the opponent\'s ships before the opponent sinks yours.')
game=int(input('Input 1 for 1-player game or 2 for 2-player game: '))
while (game!=1 and game!=2):
      game=int(input('Wrong number, please give number 1 for 1-player game or number 2 for 2-player game:'))
print('')
if game==1:
   for i in range(1,6):
         y=str(i)
         x=input('Player 1 enter the position of your ship no'+y+':')
         while x not in loc or x in p1pos:
               x=input('Wrong position or position already given.Please enter right position of ship no'+y+':')
         p1pos.append(x)
         if x in loc and x not in p1pos:
               p1pos.append(x)
   print('')
   play=['pc','p1']
   PC=pcShips(pi1,pi2)
   p=random.choice(play)
   if p=='pc':
       print('CPU starts firts!!')
       print('')
       print('    P1    ','        P2')
       print('  12345','         12345')
       print('a',''.join(a),                   '      ','a',''.join(a2))
       print('b',''.join(b),                   '      ','b',''.join(b2))
       print('c',''.join(c),                    '      ','c',''.join(c2))
       print('d',''.join(d),                   '      ','d',''.join(d2))
       print('e',''.join(e),                    '      ','e',''.join(e2))
       M2=random.choice(locpc)
       locpc.remove(M2)
       y=str(M2)
       print('Missile thrown at'+' '+M2)                        
       if M2 in p1pos:
              print('Target hit!')
              hit=M2
              XO(hit)
              p1pos.remove(M2)
       else:
              print('Target missed')
              miss=M2
              OX(miss)
   else:
          print('Player 1 starts first!!')
   print('    P1    ','        P2')
   print('  12345','         12345')
   print('a',''.join(a),                   '      ','a',''.join(a2))
   print('b',''.join(b),                   '      ','b',''.join(b2))
   print('c',''.join(c),                    '      ','c',''.join(c2))
   print('d',''.join(d),                   '      ','d',''.join(d2))
   print('e',''.join(e),                    '      ','e',''.join(e2))
   while (Y and Y1):
             M1=input('Player 1 enter the position to throw your missile:')
             x=str(M1)    
             while M1 not in loc:
                   M1=input('Invalid position, or missile already thrown there. Try again:')
             while M1 in bombs:
                   M1=input('Invalid position, or missile already thrown there. Try again:')
             print('Missile thrown at'+' '+x)
             if M1 in PC:
                   print('Target hit!')
                   hit=M1
                   XO1(hit)
                   PC.remove(M1)
             else:
                   print('Target missed!')
                   miss=M1
                   OX1(miss)
             bombs.append(M1)
             print('    P1    ','        P2')
             print('  12345','         12345')
             print('a',''.join(a),                   '      ','a',''.join(a2))
             print('b',''.join(b),                   '      ','b',''.join(b2))
             print('c',''.join(c),                    '      ','c',''.join(c2))
             print('d',''.join(d),                   '      ','d',''.join(d2))
             print('e',''.join(e),                    '      ','e',''.join(e2))      
             M2=random.choice(locpc)
             locpc.remove(M2)
             M2=str(M2)
             print('Missile thrown at'+' '+M2)                        
             if M2 in p1pos:
                    print('Target hit!')
                    hit=M2
                    XO(hit)
                    p1pos.remove(M2)
             else:
                    print('Target missed!')
                    miss=M2
                    OX(miss)
             print('    P1    ','        P2')
             print('  12345','         12345')
             print('a',''.join(a),                   '      ','a',''.join(a2))
             print('b',''.join(b),                   '      ','b',''.join(b2))
             print('c',''.join(c),                    '      ','c',''.join(c2))
             print('d',''.join(d),                   '      ','d',''.join(d2))
             print('e',''.join(e),                    '      ','e',''.join(e2))      
             if PC==[]:
                   Y=False
                   print('GAME OVER. Player 1 won the game!')
             if p1pos==[]:
                   Y1=False
                   print('GAME OVER. CPU won the game!')
       
if game==2:
   for i in range(1,6):
         y=str(i)
         x=input('Player 1 enter the position of your ship no'+y+':')
         while x not in loc or x in p1pos:
               x=input('Wrong position or position already given.Please enter right position of ship no'+y+':')
         p1pos.append(x)
         if x in loc and x not in p1pos:
               p1pos.append(x)
   print('Now it is player 2 turn!')
   for i in range(1,6):
         y=str(i)
         x1=input('Player 2 enter the position of your ship no'+y+':')
         while x1 not in loc or x1 in p2pos:
               x1=input('Wrong position or position already given.Please enter right position of ship no'+y+':')
         p2pos.append(x1)
         if x1 in loc and x1 not in p2pos:
               p2pos.append(x1)     
   print('')
   play=['p2','p1']
   p=random.choice(play)
   if p=='p2':
       print('Player 2 starts firts!')
       print('')
       print('    P1    ','        P2')
       print('  12345','         12345')
       print('a',''.join(a),                   '      ','a',''.join(a2))
       print('b',''.join(b),                   '      ','b',''.join(b2))
       print('c',''.join(c),                    '      ','c',''.join(c2))
       print('d',''.join(d),                   '      ','d',''.join(d2))
       print('e',''.join(e),                    '      ','e',''.join(e2)) 
       M2=input('Player 2 enter the position to throw your missile:')
       x=str(M2)
       while M2 not in loc:
             M2=input('Invalid position, or missile already thrown there. Try again:')
       while M2 in bombs2:
             M2=input('Invalid position, or missile already thrown there. Try again:')
       print('Missile thrown at'+' '+x)
       if M2 in p1pos:
            print('Target hit!')
            hit=M2
            XO(hit)
            p1pos.remove(M2)
       else:
            print('Target missed!')
            miss=M2
            OX(miss)
       bombs2.append(M2)
       print('    P1    ','        P2')
       print('  12345','         12345')
       print('a',''.join(a),                   '      ','a',''.join(a2))
       print('b',''.join(b),                   '      ','b',''.join(b2))
       print('c',''.join(c),                    '      ','c',''.join(c2))
       print('d',''.join(d),                   '      ','d',''.join(d2))
       print('e',''.join(e),                    '      ','e',''.join(e2)) 
   elif p=='p1':
         print('Player 1 starts first!!')
         print('')
         print('    P1    ','        P2')
         print('  12345','         12345')
         print('a',''.join(a),                   '      ','a',''.join(a2))
         print('b',''.join(b),                   '      ','b',''.join(b2))
         print('c',''.join(c),                    '      ','c',''.join(c2))
         print('d',''.join(d),                   '      ','d',''.join(d2))
         print('e',''.join(e),                    '      ','e',''.join(e2))  
   while (Y and Y1):
                  M1=input('Player 1 enter the position to throw your missile:')
                  x=str(M1)
                  while M1 not in loc:
                         M1=input('Invalid position, or missile already thrown there. Try again:')
                  while M1 in bombs:
                         M1=input('Invalid position, or missile already thrown there. Try again:')
                  print('Missile thrown at'+' '+x)
                  if M1 in p2pos:
                       print('Target hit!')
                       hit=M1
                       XO1(hit)
                       p2pos.remove(M1)
                  else:
                       print('Target missed!')
                       miss=M1
                       OX1(miss)
                  bombs.append(M1)
                  print('    P1    ','        P2')
                  print('  12345','         12345')
                  print('a',''.join(a),                   '      ','a',''.join(a2))
                  print('b',''.join(b),                   '      ','b',''.join(b2))
                  print('c',''.join(c),                    '      ','c',''.join(c2))
                  print('d',''.join(d),                   '      ','d',''.join(d2))
                  print('e',''.join(e),                    '      ','e',''.join(e2)) 
                  if p2pos==[]:
                        Y=False
                        print('GAME OVER. Player 1 won the game!')
                  else:
                        M2=input('Player 2 enter the position to throw your missile:')
                        x=str(M2)
                        while M2 not in loc:
                              M2=input('Invalid position, or missile already thrown there. Try again:')
                        
                        while M2 in bombs2:
                              M2=input('Invalid position, or missile already thrown there. Try again:')
                        print('Missile thrown at'+' '+x)
                        if M2 in p1pos:
                             print('Target hit!')
                             hit=M2
                             XO(hit)
                             p1pos.remove(M2)
                        else:
                             print('Target missed!')
                             miss=M2
                             OX(miss)
                        bombs2.append(M2)
                        print('    P1    ','        P2')
                        print('  12345','         12345')
                        print('a',''.join(a),                   '      ','a',''.join(a2))
                        print('b',''.join(b),                   '      ','b',''.join(b2))
                        print('c',''.join(c),                    '      ','c',''.join(c2))
                        print('d',''.join(d),                   '      ','d',''.join(d2))
                        print('e',''.join(e),                    '      ','e',''.join(e2))  
                        if p1pos==[]:
                              Y1=False
                              print('GAME OVER. Player 2 won the game!')               
                  
   




     
