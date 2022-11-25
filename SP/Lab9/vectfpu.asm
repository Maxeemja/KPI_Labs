.586
.model flat, C

.data
result dd 0

.code

MyDotProduct_FPU proc res:DWORD, pa:DWORD, pb:DWORD, n:DWORD
	mov ecx, n
	mov edi, res
	mov eax, pa
	mov edx, pb
	fld result
	@cycle:
		dec ecx
		fld dword ptr[eax + 4*ecx]
		fmul dword ptr[edx + 4*ecx]
		faddp st(1), st(0)
		cmp ecx, 0
		jne @cycle
	fstp dword ptr[edi]
	ret
MyDotProduct_FPU endp

end
