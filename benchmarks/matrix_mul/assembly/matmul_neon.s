.global _matmul_asm
.align 4

_matmul_asm:
    // x0: A, x1: B, x2: C, x3: N
    
    // Triple loop: i, k, j (cache friendly)
    // for i from 0 to N-1
    //   for k from 0 to N-1
    //     r = A[i*N + k]
    //     for j from 0 to N-1 (step 2 or 4)
    //       C[i*N + j] += r * B[k*N + j]

    mov x4, #0          // i = 0
.Li_loop:
    cmp x4, x3
    b.ge .Ldone
    
    mov x5, #0          // k = 0
.Lk_loop:
    cmp x5, x3
    b.ge .Li_next

    // Load r = A[i*N + k]
    // index = i*N + k
    mul x6, x4, x3      // x6 = i*N
    add x6, x6, x5      // x6 = i*N + k
    lsl x6, x6, #3      // x6 = index * 8
    ldr d0, [x0, x6]    // d0 = r
    dup v0.2d, v0.d[0]  // v0 = [r, r]

    // Pointers for C[i][j] and B[k][j]
    mul x7, x4, x3      // x7 = i*N
    lsl x7, x7, #3
    add x7, x7, x2      // x7 = &C[i*N]
    
    mul x8, x5, x3      // x8 = k*N
    lsl x8, x8, #3
    add x8, x8, x1      // x8 = &B[k*N]

    mov x9, #0          // j = 0
.Lj_loop:
    cmp x9, x3
    b.ge .Lk_next

    // Load 2 doubles from B and C
    ld1 {v1.2d}, [x8], #16    // v1 = [B[k*N+j], B[k*N+j+1]]
    ld1 {v2.2d}, [x7]         // v2 = [C[i*N+j], C[i*N+j+1]]
    
    // Fused Multiply-Add: v2 = v2 + v1 * r
    fmla v2.2d, v1.2d, v0.2d
    
    // Store back to C
    st1 {v2.2d}, [x7], #16
    
    add x9, x9, #2
    b .Lj_loop

.Lk_next:
    add x5, x5, #1
    b .Lk_loop

.Li_next:
    add x4, x4, #1
    b .Li_loop

.Ldone:
    ret
