// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
	
@SCREEN
D=A	
@curr_screen_pos
M=D
// and set screen_size variable
@8191
D=A
@SCREEN
D=D+A
@max_screen_pos
M=D	
	
(START)
	// If key is not pressed, jump to white
	@KBD
	D=M // if no key pressed, d == 0
	@WHITE
	D; JEQ
	// otherwise, jump to black
	@BLACK
	0; JMP

(BLACK)

	// Set one pixel to black
	@curr_screen_pos
	A=M // D is now the number that we want
	M=-1 // M[curr_screen_pos] = -1
	// and increment the screen pointer
	@INCR
	0; JMP

(WHITE)
	// set one pixel to white
	@curr_screen_pos
	A=M
	M=0
	@INCR

(INCR)
	// increment the pointer; if greater thyan max_screen_pos, reset it
	@curr_screen_pos
	D=M+1
	M=D

	@max_screen_pos
	D=D-M // d = curr_screen_pos - max_screen_pos
	@START
	D;JNE // If not the same, don't reset
	
	// otherwise,reset M
	@SCREEN
	D=A
	@curr_screen_pos
	M=D
	@START
	0;JMP 
