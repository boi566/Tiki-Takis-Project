board = [" " , " " , " " ,
" " , " " , " " ,
" " , " " , " "]
sub_board = [[0 , 1 , 2] , [3 , 4 , 5] , [6 , 7 , 8] , [0 , 3 , 6] , [2 , 5 , 8] , [1 , 4 , 7] , [2 , 4 , 6] , [0 , 4 , 8]]
you = 'O'
booty = 'X'
curent = you
def chkwn(b):
    for von in sub_board:
        if board[von[0]] == board[von[1]] == board[von[2]] and board[von[0]] != " ":
            return(b[von[0]])
    if " " not in b:
        return "Draw"
    return None
def mimx(b , depth , is_maximizing):
    slt = chkwn(b)
    if slt == booty:
        return 10 - depth
    elif slt == you:
        return depth - 10
    elif slt == "Draw":
        return 0
    if is_maximizing:
        bs = float('-inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = booty
                s = mimx(b , depth + 1 , False)
                b[i] = " "
                bs = max(s , bs)
        return bs
    else:
        bs = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = you
                s = mimx(b , depth + 1 , True)
                b[i] = " "
                bs = min(s , bs)
        return bs
def fbm(b):
    bs = float("-inf")
    bi = None
    for i in range(9):
        if b[i] == " ":
            b[i] = booty
            s = mimx(b , 0 , False)
            b[i] = " "
            if s > bs:
                bs = s
                bi = i
    return bi
while True:
    try:
        if curent == booty:
            print("thinking...")
            i = fbm(board)
            print(f"\033[H\033[2J{board[0:3]}\n{'-' * 15}\n{board[3:6]}\n{'-' * 15}\n{board[6:9]}")
        else:
            i = int(input("enter 0-8: "))
        if board[i] == " ":
            board[i] = curent
            for i in range(1):
                print(f"\033[H\033[2J{board[0:3]}\n{'-' * 15}\n{board[3:6]}\n{'-' * 15}\n{board[6:9]}")
            ck = chkwn(board)
            if ck == "Draw":
                print("its a tie bois")
                break
            elif ck is not None:
                print(f"the winner is {ck}")
                break
            if curent == you:
                curent = booty
            else:
                curent = you
        else:
            print("spot taken bitch lolol")
    except ValueError:
        print("try again")
    except IndexError:
        print("0-8 only")