.586
.model flat, c
.code


StrHex_MY proc
	push ebp
	mov ebp,esp
	mov ecx, [ebp+8] 
	cmp ecx, 0
	jle @exitp
	shr ecx, 3 
	mov esi, [ebp+12] 
	mov ebx, [ebp+16]
@cycle:
	mov dl, byte ptr[esi+ecx-1] 
	mov al, dl
	shr al, 4 
	call HexSymbol_MY
	mov byte ptr[ebx], al
	mov al, dl 
	call HexSymbol_MY
	mov byte ptr[ebx+1], al
	mov eax, ecx
	cmp eax, 4
	jle @next
	dec eax
	and eax, 3 
	cmp al, 0
	jne @next
	mov byte ptr[ebx+2], 32 
	inc ebx
@next:
	add ebx, 2
	dec ecx
	jnz @cycle
	mov byte ptr[ebx], 0
@exitp:
	pop ebp
	ret 12

StrHex_MY endp


HexSymbol_MY proc
	and al, 0Fh
	add al, 48 
	cmp al, 58
	jl @exitp
	add al, 7 
@exitp:
	ret
HexSymbol_MY endp



DwordToStrHex proc
push ebp
mov ebp,esp
mov ebx,[ebp+8]
mov edx,[ebp+12] 
xor eax,eax
mov edi,7
@next:
mov al,dl
and al,0Fh 
add ax,48 
cmp ax,58
jl @store
add ax,7 
@store:
mov [ebx+edi],al
shr edx,4
dec edi
cmp edi,0
jge @next
pop ebp
ret 8
DwordToStrHex endp

end
