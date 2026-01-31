.global _fib_asm
.align 4

_fib_asm:
    // Input: x0 = n
    // Output: x0 = fib(n)

    // Base case: if n <= 1, return n
    cmp x0, #1
    b.le .Lret

    // Stack frame setup
    // We need to save FP(x29), LR(x30), and callee-saved regs x19, x20
    // Stack must be 16-byte aligned. We need 4 regs = 32 bytes to save + 32 bytes for FP/LR = 64 bytes?
    // Actually stp pushes pairs.
    // [sp-16]! -> x29, x30 (pre-index decrement)
    // then stp x19, x20, [sp, -16]! ... but simpler to allocate all at once.
    // Allocate 32 bytes total?
    // 8 bytes * 4 regs = 32 bytes.
    stp x29, x30, [sp, #-32]!  // Push FP, LR, allocate 32 bytes
    mov x29, sp
    stp x19, x20, [sp, #16]    // Save x19, x20 at offset 16

    mov x19, x0                // Safe keep n in x19

    // fib(n-1)
    sub x0, x19, #1
    bl _fib_asm
    mov x20, x0                // Save result of fib(n-1) in x20

    // fib(n-2)
    sub x0, x19, #2
    bl _fib_asm

    // result = fib(n-2) + fib(n-1)
    // x0 has fib(n-2), x20 has fib(n-1)
    add x0, x0, x20

    // Epilogue
    ldp x19, x20, [sp, #16]    // Restore callee-saved regs
    ldp x29, x30, [sp], #32    // Restore FP, LR and deallocate
    ret

.Lret:
    ret
