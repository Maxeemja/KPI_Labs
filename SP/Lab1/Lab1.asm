.386
.model flat, stdcall

include C:\masm32\include\kernel32.inc
include C:\masm32\include\user32.inc

includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

  
.data
  Caption db "Я програма на асемблері",0
  Text db "Здоровенькі були!", 10, 13, "Грицюк Максим Юрійович",0
.code
start:
  invoke MessageBoxA, 0, ADDR Text, ADDR Caption, 0
  invoke ExitProcess, 0
end start