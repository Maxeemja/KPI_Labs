.586
.model flat, stdcall

include C:\masm32\include\kernel32.inc
include C:\masm32\include\user32.inc

includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

  
.data
	res dd 256 dup(0)
	Text db 'EAX=xxxxxxxx',13,10,
			'EBX=xxxxxxxx',13,10,
			'ECX=xxxxxxxx',13,10,
			'EDX=xxxxxxxx',0

	Caption0 db "Результат CPUID 0",0
	Caption1 db "Результат CPUID 1",0
	Caption2 db "Результат CPUID 2",0

	Caption00 db "Результат CPUID 80000000h",0
	Caption01 db "Результат CPUID 80000001h",0
	Caption02 db "Результат CPUID 80000002h",0
	Caption03 db "Результат CPUID 80000003h",0
	Caption04 db "Результат CPUID 80000004h",0
	Caption05 db "Результат CPUID 80000005h",0	
	Caption08 db "Результат CPUID 80000008h",0

	Vendor db 16 dup(0)
	CaptionVendor db "CPUID 0 Vendor",0

.code

	;ця процедура записує 8 символів HEX коду числа
	;перший параметр - 32-бітове число
	;другий параметр - адреса буфера тексту

	DwordToStrHex proc
		push ebp
		mov ebp,esp
		mov ebx,[ebp+8]          ;другий параметр
		mov edx,[ebp+12]         ;перший параметр
		xor eax,eax
		mov edi,7
	@next:
		mov al,dl
		and al,0Fh              ;виділяємо одну шістнадцяткову цифру
		add ax,48               ;так можна тільки для цифр 0-9
		cmp ax,58
		jl @store
		add ax,7                ;для цифр A,B,C,D,E,F
	@store:
		mov [ebx+edi],al
		shr edx,4
		dec edi
		cmp edi,0
		jge @next
		pop ebp
		ret 8
	DwordToStrHex endp

main:

	mov eax, 0
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						;значення регістру EAX з масиву res
	push offset [Text+4]					;адреса, куди записуються 8 символів
	call DwordToStrHex
	push [res+4]						;значення регістру EBX з масиву res
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]						;значення регістру ECX з масиву res
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]						;значення регістру EDX з масиву res
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption0, 0

	mov eax, 1
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						;значення регістру EAX з масиву res
	push offset [Text+4]					;адреса, куди записуються 8 символів
	call DwordToStrHex
	push [res+4]						;значення регістру EBX з масиву res
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]						;значення регістру ECX з масиву res
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]						;значення регістру EDX з масиву res
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption1, 0

	mov eax, 2
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						;значення регістру EAX з масиву res
	push offset [Text+4]					;адреса, куди записуються 8 символів
	call DwordToStrHex
	push [res+4]						;значення регістру EBX з масиву res
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]						;значення регістру ECX з масиву res
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]						;значення регістру EDX з масиву res
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption2, 0

	mov eax, 80000000h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						;значення регістру EAX з масиву res
	push offset [Text+4]					;адреса, куди записуються 8 символів
	call DwordToStrHex
	push [res+4]						;значення регістру EBX з масиву res
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]						;значення регістру ECX з масиву res
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]						;значення регістру EDX з масиву res
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption00, 0

	mov eax, 80000001h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						
	push offset [Text+4]			
	call DwordToStrHex
	push [res+4]						
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]						
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]						
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption01, 0

	mov eax, 80000002h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						
	push offset [Text+4]			
	call DwordToStrHex
	push [res+4]					
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]					
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]					
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption02, 0

	mov eax, 80000003h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						
	push offset [Text+4]			
	call DwordToStrHex
	push [res+4]					
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]					
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]					
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption03, 0

	mov eax, 80000004h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						
	push offset [Text+4]			
	call DwordToStrHex
	push [res+4]					
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]					
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]					
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption04, 0

	mov eax, 80000005h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						
	push offset [Text+4]			
	call DwordToStrHex
	push [res+4]					
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]					
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]					
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption05, 0

	mov eax, 80000008h
	cpuid
	mov dword ptr[res], eax
	mov dword ptr[res+4], ebx
	mov dword ptr[res+8], ecx
	mov dword ptr[res+12], edx
	push [res]						
	push offset [Text+4]			
	call DwordToStrHex
	push [res+4]					
	push offset [Text+18]
	call DwordToStrHex
	push [res+8]					
	push offset [Text+32]
	call DwordToStrHex
	push [res+12]					
	push offset [Text+46]
	call DwordToStrHex
	invoke MessageBoxA, 0, ADDR Text, ADDR Caption08, 0

	mov eax, 0
	cpuid
	mov dword ptr[Vendor], ebx
	mov dword ptr[Vendor+4], edx
	mov dword ptr[Vendor+8], ecx	
	invoke MessageBoxA, 0, ADDR Vendor, ADDR CaptionVendor, 0

	invoke ExitProcess, 0
end main