// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(CHECK)
	// Set current screen to first register 
	@SCREEN
	D=A
	@current_screen
	M=D

	// Learn whether key is pressed
	@KBD
	D=M

	// If key is pressed, set screen color value to black
	@val
	M=-1

	// If key is pressed, fill the screen with black
	@FILL
	D;JNE

	// If key is not pressed, set screen color value to white
	@val
	M=0

(FILL)
	// Learn the color value
	@val
	D=M

	// Set the color value to color value for current register
	@current_screen
	A=M
	M=D

	// Take the current screen register address
	@current_screen
	D=M

	// Subtract the current screen register address from last screen register address
	@24575
	D=A-D
    
	// If the difference is less than the 0, the screen is full
	// Then go to the check part
	@CHECK
	D;JLE

	// If the difference is greater than the 0, the screen is not full
	// Then increment the current register address
	@current_screen
	M=M+1

	// Continue the loop
	@FILL
	0;JMP
