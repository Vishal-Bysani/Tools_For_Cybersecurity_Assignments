from pwn import *

p=process("./ttt")
p.recvuntil(b"]\n")
for i in range(250):
    print(i)
    f=0
    while 1:
        f+=1
        print(f)
        k=0
        l1=p.readline().decode()
        l2=p.readline().decode()
        l3=p.readline().decode()
        p.readline()
        board=[l1.split(" "),l2.split(" "),l3.split(" ")]
        board = [[cell.replace('\n', '') for cell in row] for row in board]
        print(board)

        fc=[row[0] for row in board]
        sc=[row[1] for row in board]
        tc=[row[2] for row in board]
        
        col=[fc,sc,tc]
        if board.count(['_','_','_',''])==3:
            p.writeline(b'0,0')
            continue
        x_h=[board[0].count('x'),board[1].count('x'),board[2].count('x')]
        o_h=[board[0].count('o'),board[1].count('o'),board[2].count('o')]
        under_h=[board[0].count('_'),board[1].count('_'),board[2].count('_')]
        x_v=[fc.count('x'),sc.count('x'),tc.count('x')]
        o_v=[fc.count('o'),sc.count('o'),tc.count('o')]
        under_v=[fc.count('_'),sc.count('_'),tc.count('_')]

        if sum(under_h)==1:
            index1 = under_h.index( next( num for num in under_h if num ==1 ) )
            index2 = under_v.index( next( num for num in under_v if num ==1 ) )
            p.writeline((f"{index1},{index2}".encode('utf-8')))
            break

        for j in range(3):
            if o_h[j]==2 and x_h[j]==0:
                index = board[j].index( next( num for num in board[j] if num != 'o' ) )
                p.writeline(f"{j},{index}".encode('utf-8'))
                k+=1
                break
        if k==1:
            break

        for j in range(3):
            if o_v[j]==2 and x_v[j]==0:
                index = col[j].index( next( num for num in col[j] if num != 'o' ) )
                p.writeline(f"{index},{j}".encode('utf-8'))
                k+=1
                break
        if k==1:
            break
        if board[0][0]==board[1][1] and board[0][0]=='o' and board[2][2]=='_':
            p.writeline(b'2,2')
            
            k+=1
            break

        if board[0][0]==board[2][2] and board[0][0]=='o' and board[1][1]=='_':
            p.writeline(b'1,1')
            k+=1
            break

        if board[2][2]==board[1][1] and board[1][1]=='o' and board[0][0]=='_':
            p.writeline(b'0,0')
            k+=1
            break

        if board[2][0]==board[1][1] and board[2][0]=='o' and board[0][2]=='_':
            p.writeline(b'0,2')
            k+=1
            break

        if board[0][2]==board[1][1] and board[0][2]=='o' and board[2][0]=='_':
            p.writeline(b'2,0')
            k+=1
            break

        if board[0][2]==board[2][0] and board[2][0]=='o' and board[1][1]=='_':
            p.writeline(b'1,1')
            k+=1
            break



        for j in range(3):
            if o_h[j]==0 and x_h[j]==2:
                index = board[j].index( next( num for num in board[j] if num != 'x' ) )
                p.writeline(f"{j},{index}".encode('utf-8'))
                k+=1
                break
        if k==1:
            continue

        for j in range(3):
            if o_v[j]==0 and x_v[j]==2:
                index = col[j].index( next( num for num in col[j] if num != 'x' ) )
                p.writeline(f"{index},{j}".encode('utf-8'))
                k+=1
                break
        if k==1:
            continue
        if board[0][0]==board[1][1] and board[0][0]=='x' and board[2][2]=='_':
            p.writeline(b'2,2')
            
            k+=1
        if k==1:
            continue
        if board[0][0]==board[2][2] and board[0][0]=='x' and board[1][1]=='_':
            p.writeline(b'1,1')
            k+=1
        if k==1:
            continue
        if board[2][2]==board[1][1] and board[1][1]=='x' and board[0][0]=='_':
            p.writeline(b'0,0')
            k+=1
        if k==1:
            continue
        if board[2][0]==board[1][1] and board[2][0]=='x' and board[0][2]=='_':
            p.writeline(b'0,2')
            k+=1
        if k==1:
            continue
        if board[0][2]==board[1][1] and board[0][2]=='x' and board[2][0]=='_':
            p.writeline(b'2,0')
            k+=1
        if k==1:
            continue
        if board[0][2]==board[2][0] and board[2][0]=='x' and board[1][1]=='_':
            p.writeline(b'1,1')
            k+=1
        if k==1:
            continue

        
        if f==2:
            if board[2][2]!='x':
                p.writeline(b'2,2')

            else:
                p.writeline(b'0,2')

        if f==3:
            p.writeline(b'2,0')
    if i!=249:
        l=p.recvuntil(b"]\n")
    if i==249:
        p.readline()
        l=p.readline()
        print(l)
        p.close()



