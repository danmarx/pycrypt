def encrypt(char):
    code = []
    if 1 == 1:
        if char == 'a':
            code.append('z')
            
        elif char == 'b':
            code.append('y')
            
        elif char == 'c':
            code.append('x')
            
        elif char == 'd':
            code.append('w')
            
        elif char == 'e':
            code.append('v')
            
        elif char == 'f':
            code.append('u')
            
        elif char == 'g':
            code.append('t')
            
        elif char == 'h':
            code.append('s')
            
        elif char == 'i':
            code.append('r')
            
        elif char == 'j':
            code.append('q')
            
        elif char == 'k':
            code.append('p')
            
        elif char == 'l':
            code.append('o')
            
        elif char == 'm':
            code.append('n')
            
        elif char == 'n':
            code.append('m')
            
        elif char == 'o':
            code.append('l')
            
        elif char == 'p':
            code.append('k')
            
        elif char == 'q':
            code.append('j')
            
        elif char == 'r':
            code.append('i')
            
        elif char == 's':
            code.append('h')
            
        elif char == 't':
            code.append('g')
            
        elif char == 'u':
            code.append('f')
            
        elif char == 'v':
            code.append('e')
            
        elif char == 'w':
            code.append('d')
            
        elif char == 'x':
            code.append('c')
            
        elif char == 'y':
            code.append('b')
            
        elif char == 'z':
            code.append('a')
            
        elif char == 'A':
            code.append('Z')
            
        elif char == 'B':
            code.append('Y')
            
        elif char == 'C':
            code.append('X')
            
        elif char == 'D':
            code.append('W')
            
        elif char == 'E':
            code.append('V')
            
        elif char == 'F':
            code.append('U')
            
        elif char == 'G':
            code.append('T')
            
        elif char == 'H':
            code.append('S')
            
        elif char == 'I':
            code.append('R')
            
        elif char == 'J':
            code.append('Q')
            
        elif char == 'K':
            code.append('P')
            
        elif char == 'L':
            code.append('O')
            
        elif char == 'M':
            code.append('N')
            
        elif char == 'N':
            code.append('M')
            
        elif char == 'O':
            code.append('L')
            
        elif char == 'P':
            code.append('K')
            
        elif char == 'Q':
            code.append('J')
            
        elif char == 'R':
            code.append('I')
            
        elif char == 'S':
            code.append('H')
            
        elif char == 'T':
            code.append('G')
            
        elif char == 'U':
            code.append('F')
            
        elif char == 'V':
            code.append('E')
            
        elif char == 'W':
            code.append('D')
            
        elif char == 'X':
            code.append('C')
            
        elif char == 'Y':
            code.append('B')
            
        elif char == 'Z':
            code.append('A')
            
        elif char == '1':
            code.append('9')
            
        elif char == '2':
            code.append('8')
            
        elif char == '3':
            code.append('7')
            
        elif char == '4':
            code.append('6')
            
        elif char == '5':
            code.append('5')
            
        elif char == '6':
            code.append('4')
            
        elif char == '7':
            code.append('3')
            
        elif char == '8':
            code.append('2')
            
        elif char == '9':
            code.append('1')
            
        elif char == '0':
            code.append('0')
            
        elif char == ' ':
            code.append(' ')
        else:
            code.append(char)
        print char
    return ''.join(code)
u = []
while True:
    to_crypt = raw_input("Enter Words to Encrypt ('quit' to exit): ")
    if to_crypt == 'quit':
        break
    for i in to_crypt:
        encrypted_string = encrypt(i)
        u.append(encrypted_string)
    print "Encrypted: ",''.join(u)
    u = []
