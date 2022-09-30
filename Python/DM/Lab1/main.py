from tkinter import *
# for imgs
from PIL import ImageTk, Image
# for saving files
from tkinter.filedialog import asksaveasfile
import utils as ut
from fullSol import *
from shortSol import *
from setZ import *
########### мій варіант ##############
G = 2
N = 10
M = "ІО"
print("Моя група: ", M+"-"+"0"+str(G))
print("Мій номер у групі:", N)
if M == "ІО": N += 2
print("Мій варіант:", (N+G % 60) % 30+1)
myVariant = (N+G % 60) % 30 + 1

#######################################
# window 2 for short solutions
def createWindowForShortSolution(a, b, c):
    # function for calculations
    def calc():
        result = shortSolution(a, b, c)
        resultVar = StringVar(value=result)
        res.config(textvariable=resultVar)
        step1.config(textvariable=unifVar)
        step2.config(textvariable=intrVar)

    def fileSave():
        if(res.get()):
            files = [('All Files', '*.*'),
                     ('Python Files', '*.py'),
                     ('Text Document', '*.txt')]
            f = asksaveasfile(mode='w', defaultextension=files, filetypes=files)
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            text4save = res.get()
            f.write(text4save)
            f.close()
        return

    newWindow = Toplevel(root)
    newWindow.geometry('852x600')
    newWindow.resizable(width=False, height=False)
    newWindow.title('Simply solution')
    fr = Frame(newWindow, bg='#318CE7')
    fr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    # outputs sets` info
    Label(fr, text="множина A", bg='orange', font=20).grid(row=0, column=0)
    Label(fr, text="множина B", bg='orange', font=20).grid(row=2, column=0)
    Label(fr, text="множина C", bg='orange', font=20).grid(row=4, column=0)

    A = StringVar(value=a)
    B = StringVar(value=b)
    C = StringVar(value=c)
    unificated = ut.unification(a, b)
    intr = ut.intersection(unificated, c)
    unifVar = StringVar(value=unificated)
    intrVar = StringVar(value=intr)

    e1 = Entry(fr, textvariable=A, state='readonly', font=20, width=30)
    e2 = Entry(fr, textvariable=B, state='readonly', font=20, width=30)
    e3 = Entry(fr, textvariable=C, state='readonly', font=20, width=30)
    e1.grid(row=0, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=4, column=1)

    e1Scroll = Scrollbar(fr, orient='horizontal', command=e1.xview)
    e1.config(xscrollcommand=e1Scroll.set)
    e1Scroll.grid(row=1, column=1, sticky='ew', pady=(0, 10))
    e2Scroll = Scrollbar(fr, orient='horizontal', command=e2.xview)
    e2.config(xscrollcommand=e2Scroll.set)
    e2Scroll.grid(row=3, column=1, sticky='ew', pady=(0, 10))
    e3Scroll = Scrollbar(fr, orient='horizontal', command=e3.xview)
    e3.config(xscrollcommand=e3Scroll.set)
    e3Scroll.grid(row=5, column=1, sticky='ew', pady=(0, 10))
    # /outputs info

    # calculation
    btnCalc = Button(fr, text='Порахувати', font=20, bg='#8a8988', activebackground='#e0dcd8', command=calc)
    btnCalc.grid(row=6, column=0, columnspan=3, pady=(20, 0))
    # steps
    loadFull = Image.open('img/full.png')
    renderFull = ImageTk.PhotoImage(loadFull)
    imgFull = Label(fr, image=renderFull)
    imgFull.image = renderFull
    imgFull.grid(row=7, columnspan=3, padx=(30, 0))

    # step - 1 img
    step1Img = Image.open('img/s_1.png')
    renderStep1Img = ImageTk.PhotoImage(step1Img)
    step1Img = Label(fr, image=renderStep1Img)
    step1Img.image = renderStep1Img
    step1Img.grid(row=8, column=0, padx=(30, 0), pady=(20, 0))
    # step - 1 entry
    step1 = Entry(fr, state='readonly', font=20, width=20)
    step1.grid(row=8, column=1, pady=(20, 0))
    step1Scroll = Scrollbar(fr, orient='horizontal', command=step1.xview)
    step1.config(xscrollcommand=step1Scroll.set)
    step1Scroll.grid(row=9, column=1, sticky='ew', pady=(0, 10))

    # step - 2 img
    step2Img = Image.open('img/s_2.png')
    renderStep2Img = ImageTk.PhotoImage(step2Img)
    step2Img = Label(fr, image=renderStep2Img)
    step2Img.image = renderStep2Img
    step2Img.grid(row=10, column=0, padx=(30, 0), pady=(20, 0))
    # step - 2 entry
    step2 = Entry(fr, state='readonly', font=20, width=20)
    step2.grid(row=10, column=1, pady=(20, 0))
    step2Scroll = Scrollbar(fr, orient='horizontal', command=step2.xview)
    step2.config(xscrollcommand=step2Scroll.set)
    step2Scroll.grid(row=11, column=1, sticky='ew', pady=(0, 10))
    # result
    resLab = Label(fr, text=f'Результат:', bg='gray', font=34)
    resLab.grid(row=12)
    res = Entry(fr, state='readonly', font=34)
    res.grid(row=12, column=1)
    resScroll = Scrollbar(fr, orient='horizontal', command=res.xview)
    res.config(xscrollcommand=resScroll.set)
    resScroll.grid(row=13, column=1, sticky='ew')
    # save button
    saveBtn = Button(fr, text='Зберігти результат', font=34, bg='#8a8988', activebackground='#e0dcd8', command=fileSave)
    saveBtn.grid(row=14, column=0, columnspan=2)
# /window for simply solution

# window for full solution
def createWindowForFullSolution(u, a, b, c):
    def calc():
        result = fullSolution(u, a, b, c)
        resultVar = StringVar(value=result)
        res.config(textvariable=resultVar)
        step1.config(textvariable=firstVar)
        step2.config(textvariable=secondVar)
        step3.config(textvariable=thirdVar)
        step4.config(textvariable=lastVar)

    def fileSave():
        if(res.get()):
            files = [('All Files', '*.*'),
                     ('Python Files', '*.py'),
                     ('Text Document', '*.txt')]
            f = asksaveasfile(mode='w', defaultextension=files, filetypes=files)
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            textSave = res.get()
            f.write(textSave)
            f.close()
        return

    newWindow = Toplevel(root)
    newWindow.geometry('672x760')
    newWindow.resizable(width=False, height=False)
    newWindow.title('Full solution')
    fr = Frame(newWindow, bg='#6262FF')
    fr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    A = StringVar(value=a)
    B = StringVar(value=b)
    C = StringVar(value=c)
    U = StringVar(value=u)
    firstStep = ut.nope(u, a)
    secondStep = ut.unification(a,b)
    thirdStep = c
    lastStep = ut.intersection(secondStep,thirdStep)
    firstVar = StringVar(value=firstStep)
    secondVar = StringVar(value=secondStep)
    thirdVar = StringVar(value=thirdStep)
    lastVar = StringVar(value=lastStep)

    # outputs info
    Label(fr, text="множина A", bg='#00BB00', font=20).grid(row=0, column=0)
    Label(fr, text="множина B", bg='#00BB00', font=20).grid(row=2, column=0)
    Label(fr, text="множина C", bg='#00BB00', font=20).grid(row=4, column=0)
    Label(fr, text="множина U", bg='#00BB00', font=20).grid(row=6, column=0)

    e1 = Entry(fr, textvariable=A, state='readonly', font=20, width=30)
    e2 = Entry(fr, textvariable=B, state='readonly', font=20, width=30)
    e3 = Entry(fr, textvariable=C, state='readonly', font=20, width=30)
    e4 = Entry(fr, textvariable=U, state='readonly', font=20, width=30)
    e1.grid(row=0, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=4, column=1)
    e4.grid(row=6, column=1)

    e1Scroll = Scrollbar(fr, orient='horizontal', command=e1.xview)
    e1.config(xscrollcommand=e1Scroll.set)
    e1Scroll.grid(row=1, column=1, sticky='ew', pady=(0, 10))
    e2Scroll = Scrollbar(fr, orient='horizontal', command=e2.xview)
    e2.config(xscrollcommand=e2Scroll.set)
    e2Scroll.grid(row=3, column=1, sticky='ew', pady=(0, 10))
    e3Scroll = Scrollbar(fr, orient='horizontal', command=e3.xview)
    e3.config(xscrollcommand=e3Scroll.set)
    e3Scroll.grid(row=5, column=1, sticky='ew', pady=(0, 10))
    e4Scroll = Scrollbar(fr, orient='horizontal', command=e4.xview)
    e4.config(xscrollcommand=e4Scroll.set)
    e4Scroll.grid(row=7, column=1, sticky='ew', pady=(0, 10))
    # /outputs info

    # calculation
    btnCalc = Button(fr, text='Порахувати!', font=20, bg='#8a8988', activebackground='#e0dcd8', command=calc)
    btnCalc.grid(row=8, column=0, columnspan=3, pady=(20, 0))
    # steps
    loadFull = Image.open('img/sFull_0.png')
    renderFull = ImageTk.PhotoImage(loadFull)
    imgFull = Label(fr, image=renderFull)
    imgFull.image = renderFull
    imgFull.grid(row=9, columnspan=3, padx=(20, 0))

    # step - 1
    sFull_1 = Image.open('img/sFull_1.png')
    renderSFull_1 = ImageTk.PhotoImage(sFull_1)
    img_1 = Label(fr, image=renderSFull_1)
    img_1.image = renderSFull_1
    img_1.grid(row=10, column=0, padx=(20, 0), pady=(10, 0))
    # step - 1 entry
    step1 = Entry(fr, state='readonly', font=20, width=20)
    step1.grid(row=10, column=1, pady=(10, 0))
    step1Scroll = Scrollbar(fr, orient='horizontal', command=step1.xview)
    step1.config(xscrollcommand=step1Scroll.set)
    step1Scroll.grid(row=11, column=1, sticky='ew')

    # step - 2
    sFull_2 = Image.open('img/sFull_2.png')
    renderSFull_2 = ImageTk.PhotoImage(sFull_2)
    img_2 = Label(fr, image=renderSFull_2)
    img_2.image = renderSFull_2
    img_2.grid(row=12, column=0, padx=(20, 0), pady=(10, 0))
    # step - 2 entry
    step2 = Entry(fr, state='readonly', font=20, width=20)
    step2.grid(row=12, column=1, pady=(10, 0))
    step2Scroll = Scrollbar(fr, orient='horizontal', command=step2.xview)
    step2.config(xscrollcommand=step2Scroll.set)
    step2Scroll.grid(row=13, column=1, sticky='ew')

    # step - 3
    sFull_3 = Image.open('img/sFull_3.png')
    renderSFull_3 = ImageTk.PhotoImage(sFull_3)
    img_3 = Label(fr, image=renderSFull_3)
    img_3.image = renderSFull_3
    img_3.grid(row=14, column=0, padx=(20, 0), pady=(10, 0))
    # step - 3 entry
    step3 = Entry(fr, state='readonly', font=20, width=20)
    step3.grid(row=14, column=1, pady=(10, 0))
    step3Scroll = Scrollbar(fr, orient='horizontal', command=step3.xview)
    step3.config(xscrollcommand=step3Scroll.set)
    step3Scroll.grid(row=15, column=1, sticky='ew')

    # step - 4
    sFull_4 = Image.open('img/sFull_4.png')
    renderSFull_4 = ImageTk.PhotoImage(sFull_4)
    img_4 = Label(fr, image=renderSFull_4)
    img_4.image = renderSFull_4
    img_4.grid(row=16, column=0, padx=(20, 0), pady=(10, 0))
    # step - 4 entry
    step4 = Entry(fr, state='readonly', font=20, width=20)
    step4.grid(row=16, column=1, pady=(10, 0))
    step4Scroll = Scrollbar(fr, orient='horizontal', command=step4.xview)
    step4.config(xscrollcommand=step4Scroll.set)
    step4Scroll.grid(row=17, column=1, sticky='ew')
    # result
    resLab = Label(fr, text=f'Результат:', bg='gray', font=34)
    resLab.grid(row=18)
    res = Entry(fr, state='readonly', font=34)
    res.grid(row=18, column=1)
    resScroll = Scrollbar(fr, orient='horizontal', command=res.xview)
    res.config(xscrollcommand=resScroll.set)
    resScroll.grid(row=19, column=1, sticky='ew')
    # save button
    saveBtn = Button(fr, text='Зберігти результат', font=34, bg='#8a8988', activebackground='#e0dcd8', command=fileSave)
    saveBtn.grid(row=20, column=0, columnspan=2, pady=10)

def createZsolution(u, a, b):
    global x, y
    def fileSave():
        if(setZ.get()):
            files = [('All Files', '*.*'),
                     ('Python Files', '*.py'),
                     ('Text Document', '*.txt')]
            f = asksaveasfile(mode='w', defaultextension=files, filetypes=files)
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            textSave = setZ.get()
            f.write(textSave)
            f.close()
        return

    newWindow = Toplevel(root)
    newWindow.geometry('672x300')
    newWindow.resizable(width=False, height=False)
    newWindow.title('Z solution')
    fr = Frame(newWindow, bg='#EB4C42')
    fr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    # vars
    x = ut.nope(u,a)
    y = b
    Y = StringVar(value=y)
    X = StringVar(value=x)
    Z = StringVar(value=calculateZ(u, a, b))
    # full - img
    full_z = Image.open('img/full_z.png')
    renderFull_z = ImageTk.PhotoImage(full_z)
    imgFull_z = Label(fr, image=renderFull_z)
    imgFull_z.image = renderFull_z
    imgFull_z.grid(row=0, column=0, columnspan=2, padx=(80, 0) ,pady=(10, 0))
    # set X
    Label(fr, text='множина X:', bg='#14B3BD', font=24).grid(row=1)
    setX = Entry(fr, state='readonly', font=34, textvariable=X)
    setX.grid(row=1, column=1)
    setXScroll = Scrollbar(fr, orient='horizontal', command=setX.xview)
    setX.config(xscrollcommand=setXScroll.set)
    setXScroll.grid(row=2, column=1, sticky='ew')
    # set Y
    Label(fr, text='множина Y: ', bg='#14B3BD', font=24).grid(row=3)
    setY = Entry(fr, state='readonly', font=34,  textvariable=Y)
    setY.grid(row=3, column=1)
    setYScroll = Scrollbar(fr, orient='horizontal', command=setY.xview)
    setY.config(xscrollcommand=setYScroll.set)
    setYScroll.grid(row=4, column=1, sticky='ew')
    # set Z (result)
    Label(fr, text='множина Z: ', bg='#14B3BD', font=24).grid(row=5)
    setZ = Entry(fr, state='readonly', font=34, textvariable=Z)
    setZ.grid(row=5, column=1)
    setZScroll = Scrollbar(fr, orient='horizontal', command=setZ.xview)
    setZ.config(xscrollcommand=setZScroll.set)
    setZScroll.grid(row=6, column=1, sticky='ew')
    # save button
    saveBtn = Button(fr, text='Зберігти результат', font=34, bg='#8a8988', activebackground='#e0dcd8', command=fileSave)
    saveBtn.grid(row=7, column=0, columnspan=2, pady=10)

def createFinallWindow():
    if not x or not y:
        return
    newWindow = Toplevel(root)
    newWindow.geometry('672x300')
    newWindow.resizable(width=False, height=False)
    newWindow.title('Final window')
    fr = Frame(newWindow, bg='grey')
    fr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    data = {'z_calc': StringVar(value=set.union(x, y))}
    try:
        with open('full.txt') as f:
            data['full'] = StringVar(value=f.readline())
    except FileNotFoundError:
        data['full'] = StringVar(value='file full.txt not found')

    try:
        with open('simple.txt') as f:
            data['simple'] = StringVar(value=f.readline())
    except FileNotFoundError:
        data['simple'] = StringVar(value='file simple.txt not found')

    try:
        with open('z.txt') as f:
            data['z'] = StringVar(value=f.readline())
    except FileNotFoundError:
        data['z'] = StringVar(value='file z.txt not found')

    # set X
    Label(fr, text='Повний розв\'язок:', bg='gray', font=24).grid(row=1)
    full = Entry(fr, state='readonly', font=34, textvariable=data['full'])
    full.grid(row=1, column=1)
    fullScroll = Scrollbar(fr, orient='horizontal', command=full.xview)
    full.config(xscrollcommand=fullScroll.set)
    fullScroll.grid(row=2, column=1, sticky='ew')
    # set Y
    Label(fr, text='Спрощений розв\'язок: ', bg='gray', font=24).grid(row=3)
    simply = Entry(fr, state='readonly', font=34, textvariable=data['simple'])
    simply.grid(row=3, column=1)
    simplyScroll = Scrollbar(fr, orient='horizontal', command=simply.xview)
    simply.config(xscrollcommand=simplyScroll.set)
    simplyScroll.grid(row=4, column=1, sticky='ew')
    # compression between result
    data['frstComp'] = StringVar(value=str(full.get() == simply.get()))
    # set Z (result)
    Label(fr, text='Множина Z(минула відповідь): ', bg='gray', font=24).grid(row=5)
    zBefore = Entry(fr, state='readonly', font=34, textvariable=data['z'])
    zBefore.grid(row=5, column=1)
    zBeforeScroll = Scrollbar(fr, orient='horizontal', command=zBefore.xview)
    zBefore.config(xscrollcommand=zBeforeScroll.set)
    zBeforeScroll.grid(row=6, column=1, sticky='ew')
    # calculate set Z
    Label(fr, text='множина Z(порахована вбудованими методами): ', bg='gray', font=20).grid(row=7)
    zNext = Entry(fr, state='readonly', font=34, textvariable=data['z_calc'])
    zNext.grid(row=7, column=1)
    zNextScroll = Scrollbar(fr, orient='horizontal', command=zNext.xview)
    zNext.config(xscrollcommand=zNextScroll.set)
    zNextScroll.grid(row=8, column=1, sticky='ew')
    # compression between Z sets
    data['secComp'] = StringVar(value=str(zBefore.get() == zNext.get()))
    # outputs compression info
    Label(fr, text='Результати 1 і 2 обчислень збіглись?', bg='gray', font=20).grid(row=9)
    frst = Entry(fr, state='readonly', font=34, textvariable=data['frstComp'])
    frst.grid(row=9, column=1)
    Label(fr, text='Результати 3 і 4 обчислень збіглись?', bg='gray', font=20).grid(row=10)
    frst = Entry(fr, state='readonly', font=34, textvariable=data['secComp'])
    frst.grid(row=10, column=1)


def calcZ():
    U = ut.createUniversal(universalEntry.get())

    if randEntry2.get():
        A = ut.randSet(int(randEntry1.get()))
        B = ut.randSet(int(randEntry2.get()))
        createZsolution(U, A, B)
    elif entry2.get():
        A = ut.setCreating(entry1.get())
        B = ut.setCreating(entry2.get())
        createZsolution(U, A, B)


def getRandEntry():
    A = ut.randSet(int(randEntry1.get()))
    B = ut.randSet(int(randEntry2.get()))
    C = ut.randSet(int(randEntry3.get()))
    return [A, B, C]

def getEntry():
    A = ut.setCreating(entry1.get())
    B = ut.setCreating(entry2.get())
    C = ut.setCreating(entry3.get())
    return [A, B, C]

def openShortRand():
    A, B, C = getRandEntry()
    if A and B and C:
        createWindowForShortSolution(A, B, C)
    return

def openShort():
    A, B, C = getEntry()
    if A and B and C:
        createWindowForShortSolution(A, B, C)
    return

def openFullRand():
    U = ut.createUniversal(universalEntry.get())
    A, B, C = getRandEntry()
    createWindowForFullSolution(U, A, B, C)

def openFull():
    U = ut.createUniversal(universalEntry.get())
    A, B, C = getEntry()
    if A and B and C and U:
        createWindowForFullSolution(U, A, B, C)
    return

root = Tk()
root['bg'] = '#fafafa'
root.title('Hrytsiuk IO-02')
root.geometry('900x600')
root.resizable(width=False, height=False)

frame = Frame(root, bg='#4AFF32')
frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

# variant
name = Label(root, text='Грицюк Максим Юрійович', bg='white', font=24)
group = Label(root, text='Група: ІО-02', bg='white', font=20)
num = Label(root, text='Номер у списку: 10', bg='white', font=20)
variant = Label(root, text=f'Мій варіант: {myVariant}', bg='white', font=20)
name.pack()
group.pack()
num.pack()
variant.pack()

# universal set
Label(frame, text="Діапазон", bg='#FBFF1E', font=20).grid(row=0, column=1)
universalEntry = Entry(frame, width=30)
universalEntry.insert(0, '0, 255')
universalEntry.grid(row=0, column=2, pady=30)


# inputs for random generation
Label(frame, text="Потужність множини А", bg='#FBFF1E', font=20).grid(row=1)
Label(frame, text="Потужність множини B", bg='#FBFF1E', font=20).grid(row=2)
Label(frame, text="Потужність множини C", bg='#FBFF1E', font=20).grid(row=3)

randEntry1 = Entry(frame, width=25)
randEntry2 = Entry(frame, width=25)
randEntry3 = Entry(frame, width=25)

randEntry1.grid(row=1, column=1)
randEntry2.grid(row=2, column=1)
randEntry3.grid(row=3, column=1)

generateRandomlyBtnFull = Button(frame, text='Повний розв\'язок', font=20, bg='#8a8988', activebackground='#e0dcd8', command=openFullRand)
generateRandomlyBtnFull.grid(row=4, pady=(20, 0), padx=(5, 0))
generateRandomlyBtnShort = Button(frame, text='Спрощений розв\'язок', font=20, bg='#8a8988', activebackground='#e0dcd8', command=openShortRand)
generateRandomlyBtnShort.grid(row=4, column=1, pady=(20, 0))

# inputs
Label(frame, text="Елементи  А", bg='#FBFF1E', font=20).grid(row=1, column=2, padx=(130, 0))
Label(frame, text="Елементи  B", bg='#FBFF1E', font=20).grid(row=2, column=2, padx=(130, 0))
Label(frame, text="Елементи  C", bg='#FBFF1E', font=20).grid(row=3, column=2, padx=(130, 0))

entry1 = Entry(frame, width=30)
entry2 = Entry(frame, width=30)
entry3 = Entry(frame, width=30)

entry1.grid(row=1, column=3)
entry2.grid(row=2, column=3)
entry3.grid(row=3, column=3)

generateBtnFull = Button(frame, text='Повний розв\'язок', font=20, bg='#8a8988', activebackground='#e0dcd8', command=openFull)
generateBtnFull.grid(row=4, column=2, pady=(20, 0), padx=(140, 0))
generateBtnShort = Button(frame, text='Спрощений розв\'язок', font=20, bg='#8a8988', activebackground='#e0dcd8', command=openShort)
generateBtnShort.grid(row=4, column=3, pady=(20, 0))

# open 4 window
generateBtnFull = Button(frame, text='Порахувати множину Z', font=20, bg='#8a8988', activebackground='#e0dcd8', command=calcZ)
generateBtnFull.grid(row=5, column=0, columnspan=4, pady=(20, 0))

# open 5 window
generateBtnFull = Button(frame, text='Остаточні результати', font=20, bg='#8a8988', activebackground='#e0dcd8', command=createFinallWindow)
generateBtnFull.grid(row=6, column=0, columnspan=4, pady=(20, 0))


root.mainloop()