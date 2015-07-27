// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

	@1  //Store R1 in D
	D=M
	@i  //Make a loop counter
	M=D
	@2 
	M=0   //Zero R2
(LOOP)
	@i
	D=M
	@END
	D;JLE // If i <= 0 goto END

	@0
	D=M
	@2    
	M=M+D //Add R0 to R2


	@i
	M=M-1
	@LOOP
	0;JMP //Goto Loop

(END)