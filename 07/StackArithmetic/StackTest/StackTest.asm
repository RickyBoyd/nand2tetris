@17
D=A
@SP
M=M+1
A=M-1
M=D
@17
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQUALS0
D;JEQ
@SP
A=M-1
M=0
@END0
0;JMP
(EQUALS0)
@SP
A=M-1
M=-1
(END0)
@17
D=A
@SP
M=M+1
A=M-1
M=D
@16
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQUALS1
D;JEQ
@SP
A=M-1
M=0
@END1
0;JMP
(EQUALS1)
@SP
A=M-1
M=-1
(END1)
@16
D=A
@SP
M=M+1
A=M-1
M=D
@17
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQUALS2
D;JEQ
@SP
A=M-1
M=0
@END2
0;JMP
(EQUALS2)
@SP
A=M-1
M=-1
(END2)
@892
D=A
@SP
M=M+1
A=M-1
M=D
@891
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LT3
D;JLT
@SP
A=M-1
M=0
@END3
0;JMP
(LT3)
@SP
A=M-1
M=-1
(END3)
@891
D=A
@SP
M=M+1
A=M-1
M=D
@892
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LT4
D;JLT
@SP
A=M-1
M=0
@END4
0;JMP
(LT4)
@SP
A=M-1
M=-1
(END4)
@891
D=A
@SP
M=M+1
A=M-1
M=D
@891
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LT5
D;JLT
@SP
A=M-1
M=0
@END5
0;JMP
(LT5)
@SP
A=M-1
M=-1
(END5)
@32767
D=A
@SP
M=M+1
A=M-1
M=D
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@GT6
D;JGT
@SP
A=M-1
M=0
@END6
0;JMP
(GT6)
@SP
A=M-1
M=-1
(END6)
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@32767
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@GT7
D;JGT
@SP
A=M-1
M=0
@END7
0;JMP
(GT7)
@SP
A=M-1
M=-1
(END7)
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@GT8
D;JGT
@SP
A=M-1
M=0
@END8
0;JMP
(GT8)
@SP
A=M-1
M=-1
(END8)
@57
D=A
@SP
M=M+1
A=M-1
M=D
@31
D=A
@SP
M=M+1
A=M-1
M=D
@53
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M+D
@112
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M-D
@SP
A=M-1
M=-M
@SP
AM=M-1
D=M
A=A-1
M=M&D
@82
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M|D
@SP
A=M-1
M=!M
