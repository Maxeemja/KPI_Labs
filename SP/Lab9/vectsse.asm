.686
.xmm
.model flat, C

.data
null dd 8 dup(0)

.code

MyDotProduct_SSE proc res: DWORD, pa: DWORD, pb: DWORD, n: DWORD
		mov ecx, n
		mov edx, pb
		mov eax, pa
		mov edi, res
		movups xmm2, [null]
		@cycle:
				sub ecx, 4
				movaps xmm0, [eax + 4*ecx]
				movaps xmm1, [edx + 4*ecx]
				mulps xmm0, xmm1
				addps xmm2, xmm0
				cmp ecx, 0
				jne @cycle
		haddps xmm2,xmm2
		haddps xmm2,xmm2
		movss dword ptr[edi], xmm2
		ret
MyDotProduct_SSE endp

end