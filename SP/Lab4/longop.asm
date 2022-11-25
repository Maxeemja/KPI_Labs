.586
.model flat, c
.data 
	x dd 1
	n dd 0

	inner dd 5
	outer dd 5

.code

Mul_Nx32_LONGOP proc

	
	push ebp
	mov ebp, esp

	
	mov edi, [ebp + 12]
	mov ebx, [ebp + 8]
	mov x, ebx
	mov n, 5

	xor ebx, ebx
	xor ecx, ecx
	@mult32:
			
		mov eax, dword ptr[edi + ecx]
		mul x
		mov dword ptr[edi + ecx], eax
		clc
		adc dword ptr[edi + ecx], ebx
		mov ebx, edx

		add ecx, 4
		dec n

		jnz @mult32


	pop ebp
	ret 8


Mul_Nx32_LONGOP endp


Mul_NxN_LONGOP proc

	push ebp
	mov ebp, esp

	mov esi, dword ptr[ebp + 16]
	mov edi, dword ptr[ebp + 12]
	mov ebx, dword ptr[ebp + 8]
	xor ecx, ecx
	xor edx, edx
	mov outer, 5

	
	@cycle:
	mov eax, dword ptr[esi + edx]
	push edx

	push ebx
	mov ebx, ecx
	sub ebx, edx
	mul dword ptr[edi + ebx]
	pop ebx

	add dword ptr[ebx + ecx], eax
	adc dword ptr[ebx + ecx + 4], edx

	jnc @ncf
	xor eax, eax
	mov eax, ecx
	@cf:
	add eax, 4
	add dword ptr[ebx + eax + 4], 1
	jc @cf
	@ncf:

	pop edx
	add ecx, 4
	dec inner
	jnz @cycle
	add edx, 4
	mov ecx, edx
	mov inner, 5
	dec outer
	jnz @cycle


	pop ebp
	ret 12


Mul_NxN_LONGOP endp

End
