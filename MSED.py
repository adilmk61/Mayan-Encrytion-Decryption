import tkinter as tk

root = tk.Tk()
n=""
queue=[]
root.geometry("500x600")
root.resizable(width=False, height=False)
root.configure(background='white')

labelTitle = tk.Label(root,text="ENCRYPTION",bg='powder blue',fg='dark blue')
labelTitle.pack(fill="x",anchor="nw")
labelTitle = tk.Label(root,text="DECRYPTION",padx=230,bg='powder blue',fg='dark blue')
labelTitle.place(x=0,y=220)

textin = tk.StringVar()
textin1 = tk.StringVar()
textin2 = tk.StringVar()

d={     "*0000000"   : 'a',
        "**000000"   : 'b',
        "***00000"   : 'c',
        "****0000"   : 'd',
        "10000000"   : 'e',
        "1*000000"   : 'f',
        "1**00000"   : 'g',
        "1***0000"   : 'h',
        "1****000"   : 'i',
        "11000000"   : 'j',
        "11*00000"   : 'k',
        "11**0000"   : 'l',
        "11***000"   : 'm',
        "11****00"   : 'n',
        "11100000"   : 'o',
        "111*0000"   : 'p',
        "111**000"   : 'q',
        "111***00"   : 'r',
        "111****0"   : 's',
        "11110000"   : 't',
        "1111*000"   : 'u',
        "1111**00"   : 'v',
        "1111***0"   : 'w',
        "1111****"   : 'x',
        "11111000"   : 'y',
        "11111*00"   : 'z'}
str3=" "
str4=" "
def encrypt(str3,str4):
    str1 =textin.get()
    str2 = " "
    print(str1)
    for i in range(0, len(str1)):

        x = ord(str1[i]) - 96
        a =int( x / 5)
        b =int( x % 5)

        for j in range(0, a):
            str2 = str2 + "1"

        for j in range(0, b):
            str2 = str2 + "*"

        for k in range(0, 8 - b - a):
            str2 = str2 + "0"


        str3 = str3 + str(a)
        str4 = str4 + str(b)
    print(str2)
    textin.set(str2)

    n=textin.get()
    print(n)
    print(str3)
    print(str4)
    textin4.set(str3)
    textin5.set(str4)
    str3=""
    str4=""
    queue.append(n)



labelTitle = tk.Label(root,text="Enter message to encrypt",fg='dark blue',font=("Courier New", 10, 'bold'))
labelTitle.place(x=10,y=30)
metext = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin, width=45, bd=5, bg='powder blue')
metext.place(x=10,y=60)
labelTitle = tk.Label(root,text="keys",fg='dark blue',font=("Courier New", 10, 'bold'))
labelTitle.place(x=10,y=100)
textin4=tk.StringVar()
textin5=tk.StringVar()
metext = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin4, width=10, bd=5, bg='powder blue')
metext.place(x=10,y=150)
metext = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin5, width=10, bd=5, bg='powder blue')
metext.place(x=10,y=180)


but1 = tk.Button(root, padx=14, pady=4, bd=4, bg='white', command=lambda: encrypt(str3,str4), text="ENCRYPT",font=("Courier New", 14))
but1.place(x=10, y=100)

textin3=tk.StringVar()

def dcrypt():
    str2 = " "
    str5 = " "
    x = textin1.get()
    c = "corrupted hash or key"
    a = textin2.get()
    b = textin3.get()
    j=int(len(x) / 8)
    m=j
    index = 0
    q=8
    print("gerhgaihghiuhraiuhih")
    
    indicator=queue[0]
    final=""
    for i in range(1,len(indicator)):
        final=final+str(indicator[i])
    queue[0]=final
    print(queue[0])
    print(x)

    if queue[0]!=x:
        textin1.set(c)
        return c
    for s in range(0, j):
        index = index + q
        x = x[:index] + '#' + x[index:]

        q=9
    y = x.split("#")
    y.remove('')
    print(y)
    s=" "
    for i in y:
        flag=0
        for j in d:
            if j==i:
                s=s+str(d[j])
                flag=1
        if flag==0:
            print("Wrong!!")
            break
    for i in range(0,m):
        k=ord(a[i])-48
        h=ord(b[i])-48
        c = h*5 + k + 96
        str2 = str2 + chr(c)
    if flag==0:
        textin1.set(b)
    else:
        textin1.set(str2)
labelTitle = tk.Label(root,text="Enter encrypted message",fg='dark blue',font=("Courier New", 10, 'bold'))
labelTitle.place(x=10,y=250)
metext = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin1, width=45, bd=5, bg='powder blue')
metext.place(x=10,y=280)
metext = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin2, width=10, bd=5, bg='powder blue')
metext.place(x=10,y=450)
metext = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin3, width=10, bd=5, bg='powder blue')
metext.place(x=10,y=400)

a=textin2
b=textin3

but1 = tk.Button(root, padx=14, pady=4, bd=4, bg='white', command=lambda: dcrypt(), text="DECRYPT",
              font=("Courier New", 14))
but1.place(x=10, y=330)
root.mainloop()