# chromite-bug-bounty

Questions todo:
## List all the ratified extensions of the unprivileged spec
- Zifencei - Instruction-Fetch Fence
- Ziscr - Control and Status Registers (CSR)
- M - Integer Multiplication and Division
- A - Atomic Instructions
- F - Single Precision Floating Point Ops
- D - Double Precision Floating Point Ops
- Q - Quad Precision Floating Point Ops
- C - Compressed Instructions

## List atleast 4 unratified extensions of the unprivileged spec
- B - Bit manipulation
- V - Vector Operations
- J - Dynamically Translated Languages
- T - Transactional memory

## Why do immediates have such weird encodings?
Ans: The two variants of instruction formats B and J are used to  reduce the hardware cost of the simplest implementations. In all immediates, sign bit is always held at the 32st bit position. Since more complex implementations might have separate adders for branch and jump calculations and so would not benefit from keeping the location of immediate bits constant across types of instruction, By rotating bits in the instruction encoding of B and J immediates instead of using dynamic hardware muxes to multiply the immediate by 2, we reduce instruction signal fanout and immediate mux costs by around a factor of 2.

## Within the 32-bit instruction format, how many more instructions can you add?
Ans: Within 32 bit instruction format, we can add custom instructions in opcode labeled custom-0/1, and we can add 2^4 instructions i.e. 16 more instructions.
