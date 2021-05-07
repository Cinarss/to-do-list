import tkinter as tk 

def ekle():
    box.insert(tk.END, e.get())
    e.delete(0, tk.END)
def sil():
    if len(box.curselection()) > 0:
        index = box.curselection()[0]
        box.delete(index)
def kaydet():
    f = open('yap.txt', 'w', encoding='utf-8')
    gorevler = box.get(0,tk.END)
    f.writelines('\n'.join(gorevler))
    f.close() 
def yukle():
    f = open('yap.txt','r',encoding='utf-8')
    gorevler = f.readlines()
    box.delete(0, tk.END)
    for gorev in gorevler:
        if '\n' in gorev:
            gorev = gorev.replace('\n', '')
        box.insert(tk.END,gorev)



pencere = tk.Tk()
pencere.title('Yapılacaklar Listesi ')
 


f = tk.Frame(pencere)
f.pack()
box = tk.Listbox(f, width=50,height=10)
box.pack(side=tk.LEFT)
scroll = tk.Scrollbar(f, command=box.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
box.config(yscrollcommand=scroll.set)


e =tk.Entry(pencere, width=40)
e.pack()
e.focus()
bekle=tk.Button(pencere, text='Görev Ekle',width=40, command=ekle)
bekle.pack()
bsil=tk.Button(pencere, text='Görev Sil',width=40, command=sil)
bsil.pack()
bkaydet=tk.Button(pencere, text='Görevleri Kaydet',width=40, command=kaydet)
bkaydet.pack()
byukle=tk.Button(pencere, text='Görevleri Yükle',width=40, command=yukle)
byukle.pack()


pencere.mainloop()