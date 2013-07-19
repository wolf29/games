#!/usr/bin/env python
# TicTacToe game
# wolf@sourcefreedom.com

def main():
    scores = [0, 0]
    r1 = ['X', 'O', 'X']
    r2 = ['O', 'X', 'O']
    r3 = ['X', 'O', 'X']
    print '''
     %s | %s | %s
     ------------
     %s | %s | %s
     ------------
     %s | %s | %s''' % (r1[0], r1[1], r1[2], r2[0], \
    r2[1], r2[2], r3[0], r3[1], r3[2])
    print '''\nWelcome to the tic tac toe game\nthe object of the game \n\
    is to place 3 of your marks, \n\
    either Xs or Os in a line.\n ~~~GOOD LUCK~~~'''
    win = ''
    #The following module call resets the board.
    r1, r2, r3, win = resetbrd(r1, r2, r3, win)
    choice = 0
    turn = 0
    # win = 'false'
    p1 = raw_input('Enter 1st player name: ')
    p2 = raw_input('Enter 2nd player name: ')
    while choice != 3:
        print '\nMain Menu\n --> 1 = play a game\n\
 --> 2 = check scores\n --> 3 = quit\n'''
        choice = input('Enter your Choice: ')
        if choice == 1:
            #reset board
            r1, r2, r3, win = resetbrd(r1, r2, r3, win)
            while win == 'false':
                r1, r2, r3, turn, win, scores, p1, p2 = \
                turns(r1, r2, r3, turn, win, scores, p1, p2)
        elif choice == 2:
            print 'Player 1, %s, score is %d \n\
            Player 2, %s, score is %d' % (p1, scores[0], p2, scores[1])


def resetbrd(r1, r2, r3, win):
    r1 = ['', '', '']; r2 = ['', '', '']; r3 = ['', '', '']
    # print r1, r2, r3, win
    win = 'false'
    return r1, r2, r3, win


def turns(r1, r2, r3, turn, win, scores, p1, p2):
    if turn % 2 == 0:
        mark = 'X'; player = p1
    elif turn % 2 != 0:
        mark = 'O'; player = p2
    print '\nEnter the capital letter \n\
that corresponds with the place\nin the diagram below\n\
where you want to put your mark'
    print '\n'
    print ' A | B | C '
    print '-----------'
    print ' D | E | F '
    print '-----------'
    print ' G | H | I '
    print '+++++++++++'
    print 'to abort game, chose \'Q\''
    mw = raw_input('Enter your mark: ')
    if mw == 'X':
        print ' please enter one of \nthe capital letters A through I'
        # need to add a module for this error handler ???
    elif mw == 'O':
        print ' please enter one of \nthe capital letters A through I'
        # need to add a module for this error handler ???
    elif mw == 'A':
        if r1[0] != '': # 'X' or 'O':
            print 'A is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r1[0] = mark
            turn = turn + 1
    elif mw == 'B':
        if r1[1] != '': # 'X' or 'O':
            print 'B is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r1[1] = mark
            turn = turn + 1
    elif mw == 'C':
        if r1[2] != '': # 'X' or 'O':
            print 'C is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r1[2] = mark
            turn = turn + 1
    elif mw == 'D':
        if r2[0] != '': # 'X' or 'O':
            print 'D is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r2[0] = mark
            turn = turn + 1
    elif mw == 'E':
        if r2[1] != '': # 'X' or 'O':
            print 'E is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r2[1] = mark
            turn = turn + 1
    elif mw == 'F':
        if r2[2] != '': # 'X' or 'O':
            print 'F is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r2[2] = mark
            turn = turn + 1
    elif mw == 'G':
        if r3[0] != '': # 'X' or 'O':
            print 'G is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r3[0] = mark
            turn = turn + 1
    elif mw == 'H':
        if r3[1] != '': # 'X' or 'O':
            print 'H is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r3[1] = mark
            turn = turn + 1
    elif mw == 'I':
        if r3[2] != '': # 'X' or 'O':
            print 'I is already chosen, please make another choice'
            print 'turn is %d' % (turn)
        else:
            r3[2] = mark
            turn = turn + 1
    elif mw == 'Q':
        win = 'abort'
        return r1, r2, r3, turn, win, scores, p1, p2
    print '''
     %s | %s | %s
     ------------
     %s | %s | %s
     ------------
     %s | %s | %s''' % (r1[0], r1[1], r1[2], r2[0], \
r2[1], r2[2], r3[0], r3[1], r3[2])
    #turn = turn + 1
    r1, r2, r3, turn, win, scores, p1, p2, player = \
wins(r1, r2, r3, turn, win, scores, p1, p2, player)
    return r1, r2, r3, turn, win, scores, p1, p2


def wins(r1, r2, r3, turn, win, scores, p1, p2, player):
    a = r1[0]; b = r1[1]; c = r1[2]
    d = r2[0]; e = r2[1]; f = r2[2]
    g = r3[0]; h = r3[1]; i = r3[2]
    if (a != '' and b != '' and c != '' and a==b==c) or (a != '' and d != '' \
    and g != '' and a==d==g) or (a != '' and e != '' and i != '' and a==e==i) \
    or (b != '' and e != '' and h != '' and b==e==h) or (c != '' and f != '' \
    and i != '' and c==f==i) or (c != '' and e != '' and g != '' and c==e==g) \
    or (d != '' and e != '' and f != '' and d==e==f) or (g != '' and h != '' \
    and i != '' and g==h==i):
        print '\n%s has won the game\n' % (player)
        print a, b, c, d, e, f, g, h, i
        if player == p1:
            scores[0] = scores[0] + 1
        elif player == p2:
            scores[1] = scores[1] + 1
        win = 'true'
    elif a or b or c or d or e or f or g or h or i == '':
        if player == p1:
            print '\n it is %s\'s turn ...' % (p2)
        elif player == p2:
            print '\n it is %s\'s turn ...' % (p1)
    else:
        print 'the game is a tie. '
        win = 'tie'
    return r1, r2, r3, turn, win, scores, p1, p2, player


main()
