// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

    // Take the value of register 0
    @R0
    D=M

    // Put 0 to register 2
    @R2
    M=0

    // Take the value of register 1
    @R1
    D=M

    // Set an index and put the value of register 0 to the index
    @index
    M=D

(LOOP)
    // Take the value of the index
    @index
    D=M

    // If index is 0, jump to the end
    @END
    D;JEQ

    // Take the value of register 0
    @R0
    D=M

    // Add the value of register 0 to the register 2 which will sum of the product
    @R2
    D=D+M
    M=D

    // Decrease the index by 1
    @index
    D=M
    D=D-1
    M=D

    // Continue the loop
    @LOOP
    0;JMP

(END)
    @END
    0;JMP
