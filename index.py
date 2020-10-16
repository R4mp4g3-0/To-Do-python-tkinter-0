import tkinter as tk
from tkinter import messagebox
from todoListDb import *

def goAdminInstagram(x=None):
    import webbrowser
    try:
        webbrowser.open('https://www.instagram.com/rampage.cpp/')
        webbrowser.get()
    except:
        messagebox.showinfo('Admin', "Bir Hata oluştu.\n'purposeless.000' Instagramı açılamıyor")
# anb
# c -> Colors, B1 -> Button1
C = {
    "title": "#008798",
    "bgB1": "#065535",
    "bgB2": "#9999cc",
    "bgDelB": "#ff3030",
    "bgAddB": "#228b22",
    "bgEditB": "#a47c48",
    "fgB1": "#ffff66",
    "activeFgB1": "#ffff00",
    "fgL1": "#003436"
}
# F -> Fonts
F = {
    "title": ("Jokerman", 50),
    "fgL1": ("Verdana", 10, "bold"),
    "fgL2": ("Times", 17, "bold"),
    "fgB1": ("Fixedsys", 11, "bold"),
    "fgB2": ("Fixedsys", 17, "bold"),
}



class Home(tk.Tk):
    myCurrenUser = User.currentData()
    frames = None
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('1200x650+70+35')
        self.resizable(False, False)
        self.title('Yapılacaklar Listesi')

        container = tk.LabelFrame(self, width=300, height=500, bd=9)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, LoginPage, HomeNtLogPage, AppSettingsPage, UserSettingsPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        Home.frames = self.frames
        if Home.myCurrenUser:
            self.show_frame(HomePage)
        else:
            self.show_frame(HomeNtLogPage)

    def __del__(self):
        User.closeDbConnect()
        To_Do.closeDbConnect()


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    @staticmethod
    def createLabelTitle(root):
        titleLabel = tk.Label(root, text="Yapılacaklar listesi", fg=C["title"], font=F["title"])
        titleLabel.place(x=300, y=10)
        tk.Label(root, text="-" * 235).place(x=0, y=105)

    @staticmethod
    def createSettingsLabels(root, func, home):
        tk.Label(root, text="-" * 235).place(x=0, y=105)

        # Create Title Label
        l = tk.Label(root, text="Ayarlar", fg=C["title"], font=F["title"])
        l.place(x=480, y=4)
        # Create go Home button
        goHomeButton = tk.Button(
            root,
            text="<",
            bg=C["bgB2"],
            activebackground=C["bgB2"], activeforeground="#fff",
            font=tuple(i + 24 if type(i) == int else i for i in F["fgB1"]),
            cursor='hand2',
            command=func
        )
        goHomeButton.place(x=5, y=7)

        l0 = tk.Label(root, text='Rampage | Developer', cursor='hand2',
                 font=('Old English Text MT', 14, 'bold', 'underline'), fg='#726a95')
        l0.place(x=10, y=590)
        l0.bind('<Button-1>', goAdminInstagram)


        for i in 135, 252, 300, 417:
            tk.Label(root, text="-" * 56).place(x=0, y=i)

class LogOrRegister(tk.Toplevel):
    myHome = None
    def __init__(self,home, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        LogOrRegister.myHome = home

        self.protocol('WM_DELETE_WINDOW', self.quitToplevel)

        self.geometry('300x425+530+110')
        self.resizable(False, False)
        self.title('TO-DO LIST')


        container = tk.LabelFrame(self, width=300, height=500, bd=9)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, RegisterPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quitToplevel(self):
        LogOrRegister.myHome.deiconify()
        self.after(2000, self.destroy)

    @staticmethod
    def creteTitleLabel(root, arg):
        titleLabel = tk.Label(root, text=arg[0], fg=C["title"], font=F["title"])
        titleLabel.place(x=arg[1], y=10)
        tk.Label(root, text="-" * 54).place(x=0, y=105)

    @staticmethod
    def crtNamePassLabels(root, fText):
        for i in [["Kullanıcı Adı :", 160], ["Şifre               :", 200]]:
            label = tk.Label(root, text=i[0], fg=C["fgL1"], font=F["fgL1"])
            label.place(x=10, y=i[1])
        tk.Label(root, text=fText).place(x=10, y=320)


class AddToDo(tk.Toplevel):
    myHome = None
    def __init__(self, home, currentFrame, settingPage=None, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        AddToDo.myHome = home

        self.protocol('WM_DELETE_WINDOW', self.quitToplevel)

        self.geometry('600x300+420+175')
        self.resizable(False, False)
        self.title('ADD TO-DO')


        container = tk.LabelFrame(self, width=300, height=500, bd=9)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (AddToDoPage, EditPassPage):
            if F == EditPassPage:
                frame = F(settingPage, container, self)
            else:
                frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(currentFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quitToplevel(self):
        AddToDo.myHome.deiconify()
        HomePage.toDoes = Home.frames[HomePage].insertTdList()
        HomePage.compToDoes = Home.frames[HomePage].insertCompTdList()
        self.after(500, self.destroy)


#######################################################################################################################
class HomePage(tk.Frame):
    toDoes = None
    compToDoes = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller

        # Create Title Label
        Home.createLabelTitle(self)

        # Create Settings button
        tk.Label(self, text="AYARLAR↓").place(x=1070, y=3)


        settingsButton = tk.Button(
            self,
            text="////", font=F["fgB2"],
            width=5, height=2,
            bg=C["bgB2"],
            activebackground=C["bgB2"], activeforeground="#fff",
            relief=tk.RAISED, cursor="hand2",
            command=lambda: controller.show_frame(UserSettingsPage)
        )
        settingsButton.place(x=1050, y=20)


        tk.Label(self, text="~~YAPILACAKLAR~~"+" "*10, font="forte 20 bold").place(x=160, y=122)
        tk.Label(self, text="~~YAPILANLAR~~"+" "*10, font="forte 20 bold").place(x=765, y=122)


        self.createCompFr()

        self.createToDoListFr()


    def createToDoListFr(self):
        # Create To Do List Frame
        tdList_frame = tk.Frame(self)
        tdList_frame.place(x=5, y=165)

        scroll = tk.Scrollbar(tdList_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Create To-Do ListBox
        self.tdListbox = tk.Listbox(
            tdList_frame,
            bg='#f3f3f3',
            fg='#000',
            selectbackground=C["title"],
            width=39,
            height=11,
            font="Times 22 bold",
            yscrollcommand=scroll.set
        )
        self.tdListbox.pack()


        # Configure the scrollbar
        scroll.config(command=self.tdListbox.yview)

        # this Current user td List

        if Home.myCurrenUser:
            self.toDoes = self.insertTdList()
            HomePage.toDoes = self.toDoes


        addToDoButton = tk.Button(self, text="EKLE", width=9, fg="#000", bg=C["bgB2"],
                                  activebackground=C["bgB2"], activeforeground="#fff",
                                  font=F["fgB2"],
                                  command=self.addToDo)
        addToDoButton.place(x=10, y=565)


        delSelectButton = tk.Button(self, text="SIL", width=9, fg="#000", bg=C["bgDelB"],
                                    activebackground=C["bgDelB"], activeforeground=C["bgB2"],
                                    font=F["fgB2"],
                                    command=self.delete_to_do)
        delSelectButton.place(x=200, y=565)
        #
        complatedButton = tk.Button(self, text="TAMAMLANDI", fg="#000", bg="#006400",
                                    activebackground="#006400", activeforeground=C["bgB2"],
                                    font=F["fgB2"],
                                    command=self.toDoComplated)
        complatedButton.place(x=393, y=565)


    def createCompFr(self): # Create Complated Frame
        # Create Complated Frame
        td_frame = tk.Frame(self)
        td_frame.place(x=625, y=165)

        scroll = tk.Scrollbar(td_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.compListbox = tk.Listbox(
            td_frame,
            bg='#f3f3f3', fg='#000',
            selectbackground=C["title"],
            font="Times 22 bold overstrike",
            width=35, height=11,
            yscrollcommand=scroll.set
        )
        self.compListbox.pack()

        # Configure the scrollbar
        scroll.config(command=self.compListbox.yview)

        if Home.myCurrenUser:
            self.toDoes = self.insertCompTdList()
            HomePage.compToDoes = self.toDoes

        notCompButton = tk.Button(self, text="TAMAMLANMADI", width=12, fg="#000", bg=C["bgEditB"],
                                  activebackground=C["bgEditB"], activeforeground=C["bgB2"],
                                  font=F["fgB2"],
                                  command=self.toDoNotComplated)
        notCompButton.place(x=880, y=565)

        delSelectButton = tk.Button(self, text="SIL", width=9, fg="#000", bg=C["bgDelB"],
                                    activebackground=C["bgDelB"], activeforeground=C["bgB2"],
                                    font=F["fgB2"],
                                    command=self.delete_comp_to_do)
        delSelectButton.place(x=680, y=565)


    def delete_to_do(self):
        t = self.tdListbox.get(tk.ACTIVE)
        if len(t) == 0: return 0
        msg = messagebox.askyesno('Admin', f'{t} Silinecek! Silinsinmi?')
        if msg:
            T = To_Do()
            tId = None
            for id, value in HomePage.toDoes.items():
                if value.get('yapilacak', '') == t:
                    tId = id
                    break


            T.deleteToDo(tId, t)
            HomePage.toDoes.pop(tId)
            Home.frames[HomePage].insertTdList()

    def delete_comp_to_do(self):
        t = self.compListbox.get(tk.ACTIVE)
        if len(t) == 0: return 0

        msg = messagebox.askyesno('Admin', f'{t} Silinecek! Silinsinmi?')
        if msg:
            T = To_Do()
            tId = None
            for id, value in HomePage.compToDoes.items():
                if value.get('yapilacak', '') == t:
                    tId = id
                    break


            T.deleteToDo(tId, t)
            HomePage.compToDoes.pop(tId)
            Home.frames[HomePage].insertCompTdList()

    # toDo is Complated Now
    def toDoComplated(self):
        t = self.tdListbox.get(tk.ACTIVE)
        if len(t) == 0: return 0
        T = To_Do()
        tId = None
        for id, value in HomePage.toDoes.items():
            if value.get('yapilacak', '') == t:
                tId = id
                break

        T.updateToDo(1, tId)
        HomePage.toDoes[tId]['durum'] = 1
        HomePage.toDoes = Home.frames[HomePage].insertTdList()
        HomePage.compToDoes = Home.frames[HomePage].insertCompTdList()


    # toDo is Not Complated Now
    def toDoNotComplated(self):
        t = self.compListbox.get(tk.ACTIVE)
        if len(t) == 0: return 0
        T = To_Do()
        tId = None
        for id, value in HomePage.compToDoes.items():
            if value.get('yapilacak', '') == t:
                tId = id
                break

        T.updateToDo(0, tId)
        HomePage.compToDoes[tId]['durum'] = 0
        HomePage.toDoes = Home.frames[HomePage].insertTdList()
        HomePage.compToDoes = Home.frames[HomePage].insertCompTdList()



    def addToDo(self):
        AddToDo(self.__toplevel, AddToDoPage)
        self.__toplevel.withdraw()

    def insertTdList(self):
        self.tdListbox.delete(0, tk.END)

        t = To_Do()
        tList = t.getTo_doByUser(Home.myCurrenUser) if Home.myCurrenUser else []
        tList = [i for i in tList if i[0] == 0]
        for cout, i in enumerate(tList):
            if cout % 2 == 0:
                self.tdListbox.insert(tk.END, i[1])
                self.tdListbox.itemconfig(cout, bg="#a47c48")
            else:
                self.tdListbox.insert(tk.END, i[1])
        return {i[2]: {'durum': i[0], 'yapilacak': i[1]} for i in tList}

    def insertCompTdList(self):
        self.compListbox.delete(0, tk.END)

        t = To_Do()
        tList = t.getTo_doByUser(Home.myCurrenUser) if Home.myCurrenUser else []
        tList = [i for i in tList if i[0] == 1]

        for cout, i in enumerate(tList):
            if cout % 2 == 0:
                self.compListbox.insert(tk.END, i[1])
                self.compListbox.itemconfig(cout, bg="#a47c48")
            else:
                self.compListbox.insert(tk.END, i[1])
        return {i[2]: {'durum': i[0], 'yapilacak': i[1]} for i in tList}


#-----------------------------------------------------------------------------------------------------
class UserSettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller

        Home.createSettingsLabels(self, lambda: controller.show_frame(HomePage), self.__toplevel)

        tk.Label(self, text='|' * 1, wraplength=1).place(x=275, y=117)
        tk.Label(self, text='|' * 25, wraplength=1).place(x=275, y=260)

        userSttngs = tk.Label(
            self,
            text="K. Ayarları",
            bg='#669999',
            fg=C["fgB1"],
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            cursor='hand2', relief=tk.SUNKEN

        )
        userSttngs.place(x=10, y=157, height=100, width=225)

        goAppSttngs = tk.Button(
            self,
            text="Uygulama\n  Ayarları",
            bg='#669999',
            activebackground='#669999', activeforeground=C["fgB1"],
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            cursor='hand2',
            command=lambda: controller.show_frame(AppSettingsPage)
        )
        goAppSttngs.place(x=10, y=320, height=100, width=225)



        self.createSettingPage()

    def createSettingPage(self):

        edit_password = tk.Button(
            self,
            text='Şifre Değiştir',
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            bg='#377aa7', fg='#000',
            activebackground='#377aa7', activeforeground='#fff',
            cursor='hand2',
            command=self.editPass
        )
        edit_password.place(x=400, y=250, width='250', height='80')

        del_user = tk.Button(
            self,
            text='Hesabı Sil !',
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            bg=C["bgDelB"], fg='#000',
            activebackground=C["bgDelB"], activeforeground='#fff',
            cursor='hand2',
            command=self.delUser
        )
        del_user.place(x=800, y=250, width='250', height='80')


        logOut = tk.Button(
            self,
            text='Çıkış Yap',
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            bg='#ff8c00', fg='#000',
            activebackground='#ff8c00', activeforeground='#fff',
            cursor='hand2',
            command=self.logOut
        )
        logOut.place(x=560, y=410, width='350', height='80')

    def logOut(self, K=True):
        if K:
            if messagebox.askokcancel('Admin', 'Çıkış yapılıcak.'):
                self.__toplevel.show_frame(HomeNtLogPage)
                User.delCurrentData()
                Home.myCurrenUser = None
        else:
            self.__toplevel.show_frame(HomeNtLogPage)
            User.delCurrentData()
            Home.myCurrenUser = None

    def editPass(self):
        AddToDo(self.__toplevel, EditPassPage, self)
        self.__toplevel.withdraw()



    def delUser(self):
        if messagebox.askyesno('Admin', 'Hesabınız silinecek !\n(Bütün görevlerinizde silinir)\nEminmisiniz ?'):
            User.deleteUser(Home.myCurrenUser)
            To_Do.deleteTodoes(Home.myCurrenUser.currentUser[0])
            self.logOut(False)
            messagebox.showinfo('Admin', 'Hesabınız başarıyla silindi.')


#-----------------------------------------------------------------------------------------------------

class AppSettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Home.createSettingsLabels(self, lambda: controller.show_frame(HomePage), controller)

        tk.Label(self, text='|' * 10, wraplength=1).place(x=275, y=117)
        tk.Label(self, text='|' * 3, wraplength=1).place(x=275, y=260)
        tk.Label(self, text='|' * 13, wraplength=1).place(x=275, y=430)

        goUserSttngs = tk.Button(
            self,
            text="K. Ayarları",
            bg='#669999',
            activebackground='#669999', activeforeground=C["fgB1"],
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            cursor='hand2',
            command=lambda: controller.show_frame(UserSettingsPage)

        )
        goUserSttngs.place(x=10, y=157, height=100, width=225)

        appSttngs = tk.Label(
            self,
            text="Uygulama\n  Ayarları",
            bg='#669999',
            fg=C["fgB1"],
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            cursor='hand2', relief=tk.SUNKEN
        )
        appSttngs.place(x=10, y=320, height=100, width=225)

        self.createSettingPage()

    def createSettingPage(self):

        del_all_todoes = tk.Button(
            self,
            text='Bütün Görevleri\nSil !',
            font=tuple(i + 13 if type(i) == int else i for i in F["fgB1"]),
            bg=C["bgDelB"], fg='#000',
            activebackground=C["bgDelB"], activeforeground='#fff',
            cursor='hand2',
            command=self.delTodoes
        )

        del_all_todoes.place(x=550, y=320, width='350', height='90')


    def delTodoes(self):
        if messagebox.askyesno('Admin', 'Bütün görevleriniz silinecek !\nEminmisiniz ?'):
            To_Do.deleteTodoes(Home.myCurrenUser.currentUser[0])
            HomePage.toDoes = Home.frames[HomePage].insertTdList()
            HomePage.compToDoes = Home.frames[HomePage].insertCompTdList()
            messagebox.showinfo('Admin', 'Bütün Görevleriniz\nbaşarıyla silindi.')



#-----------------------------------------------------------------------------------------------------

class HomeNtLogPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller

        # Create Title Label
        Home.createLabelTitle(self)

        footerLabel = tk.Label(self, fg='#ff0000',font=F["fgL2"],
                               text="Lütven Uygulamayı kullanmak için\n Giriş Yapınız. ☺ ↓↓↓"
                               )
        footerLabel.place(x=430, y=300)

        goLogin = tk.Button(
            self,
            text="Giris Yap", font=tuple(i+9 if type(i) == int else i for i in F["fgB1"]),
            bg=C["bgB1"], fg=C["fgB1"],
            activebackground=C["bgB1"], activeforeground=C["activeFgB1"],
            command=self.goLogPage)
        goLogin.place(x=500, y=400, width=200, height=75)


    def goLogPage(self):
        LogOrRegister(self.__toplevel)
        self.__toplevel.withdraw()
#-----------------------------------------------------------------------------------------------------
class AddToDoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller

        # is finish? Checkbutton variable
        self.value_x = tk.IntVar()
        self.value_x.set(0)

        # Create Title Label
        titleLabel = tk.Label(self, text="Add To Do", fg=C["title"], font=F["title"])
        titleLabel.place(x=130, y=10)
        tk.Label(self, text="-" * 115).place(x=0, y=105)


        label = tk.Label(self, text="Yapılacak :", fg=C["fgL1"], font=tuple(i+10 if type(i) == int else i for i in F["fgL1"]))
        label.place(x=10, y=160)

        # Todo Text
        self.__toDo = tk.Text(
            self,
            width=30,
            padx=5,
            pady=10,
            selectbackground=C["title"],
            font='Times 15 italic bold'
        )
        self.__toDo.place(x=200, y=140, height=80)

        isComplated = tk.Checkbutton(self, text='Tamamlandı', fg=C["fgL1"], font='Times 15', variable=self.value_x)
        isComplated.place(x=130, y=235)


        # Create buttons
        addButton = tk.Button(
            self,
            text="EKLE", font=F["fgB1"],
            bg=C["bgB1"], fg=C["fgB1"],
            activebackground=C["bgB1"], activeforeground=C["activeFgB1"],
            command=self.addToDoDb
        )
        addButton.place(x=290, y=240, width=100)
        cancelButton = tk.Button(
            self,
            text="IPTAL", font=F["fgB1"],
            bg=C["bgDelB"], fg=C["fgB1"],
            activebackground=C["bgDelB"], activeforeground=C["activeFgB1"],
            command=self.__toplevel.quitToplevel
        )
        cancelButton.place(x=410, y=240, width=100)

        self.__toDo.bind('<Insert>', self.addToDoDb)
        addButton.bind('<Insert>', self.addToDoDb)


        # Pres Enter to Login


    # ToDo add to Database
    def addToDoDb(self, x=None):
        k = True
        try:
            t = To_Do()
            t.addToDo(
                self.value_x.get(),
                self.__toDo.get('1.0', tk.END).replace('\n', ' '),
                Home.myCurrenUser.currentUser[0]
            )
        except:
            messagebox.showinfo("Admin", "Bilinmeyen bir hata\nLütven Tekrar deneyin")
            k = False
        if k:
            messagebox.showinfo("Admin", "Görev Başarıyla Eklendi ☻")

#-----------------------------------------------------------------------------------------------------
class EditPassPage(tk.Frame):

    def __init__(self, settingsPage, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller
        self.__settingsPage = settingsPage


        # Create Title Label
        titleLabel = tk.Label(self, text="Edit Password", fg=C["title"], font=F["title"])
        titleLabel.place(x=60, y=10)
        tk.Label(self, text="-" * 115).place(x=0, y=105)



        tk.Label(self, text='Eski Şifre     :', fg=C["fgL1"], font=F["fgL1"]).place(x=20, y=125)
        tk.Label(self, text='Yeni Şifre    :', fg=C["fgL1"], font=F["fgL1"]).place(x=20, y=160)
        tk.Label(self, text='Tekrar Şifre :', fg=C["fgL1"], font=F["fgL1"]).place(x=20, y=195)

        # Create old Password Entry
        self.__oldPassword = tk.Entry(self, width=30)
        self.__oldPassword.place(x=120, y=126)

        # Create new password Password Entry
        self.__password0 = tk.Entry(self, show="*", width=30)
        self.__password0.place(x=120, y=161)

        # Create Retry Password  Entry
        self.__password1 = tk.Entry(self, show="*", width=30)
        self.__password1.place(x=120, y=196)

        self.__password1.bind('<Return>', self.editPass)

        # Create buttons
        editButton = tk.Button(
            self,
            text="Deiştir", font=F["fgB1"],
            bg=C["bgDelB"], fg=C["fgB1"],
            activebackground=C["bgDelB"], activeforeground=C["activeFgB1"],
            command=self.editPass
        )
        editButton.place(x=290, y=240, width=100)
        cancelButton = tk.Button(
            self,
            text="IPTAL", font=F["fgB1"],
            bg=C["bgB1"], fg=C["fgB1"],
            activebackground=C["bgB1"], activeforeground=C["activeFgB1"],
            command=self.__toplevel.quitToplevel
        )
        cancelButton.place(x=410, y=240, width=100)


    def editPass(self, x=None):
        if self.checkPassword():
            print(Home.myCurrenUser.currentUser)
            User.updateUser(Home.myCurrenUser,
                            Home.myCurrenUser.currentUser[1],
                            self.__password0.get())
            self.__toplevel.quitToplevel()
            self.__settingsPage.logOut(False)


    def checkPassword(self):
        if self.__oldPassword.get() != Home.myCurrenUser.currentUser[2]:
            messagebox.showinfo("Admin", "Eski Şifrenizi Yanlış Girdiniz !")
            return False
        elif (self.__password0.get() != self.__password1.get()):
            messagebox.showinfo("Admin", "Şifreler Uyuşmuyor.\nLÜTVEN TEKRAR DENEYİN ♥")
            return False
        else:
            if (8 > len(self.__password0.get()) or len(self.__password0.get()) > 50):
                messagebox.showinfo("Admin", "Şifre; 8 karakterden küçük ve\n50 karakterden büyük olamaz")
                self.__password0.delete(0, "end")
                self.__password1.delete(0, "end")
                return False
            elif (" " in self.__password0.get()):
                messagebox.showinfo("Admin", "Şifrenin içinde boşluk olamaz !")
                self.__password0.delete(0, "end")
                self.__password1.delete(0, "end")
                return False
            else:
                return True


#-----------------------------------------------------------------------------------------------------
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller

        # remember me Checkbutton variable
        self.value_x = tk.IntVar()
        self.value_x.set(0)

        # Create Title Label
        LogOrRegister.creteTitleLabel(self, ["Giriş", 58])

        # Create Labels
        LogOrRegister.crtNamePassLabels(self, "Hala kaydolmadınmı?\nhemen Kaydola tıklayıp, Kaydola bilirsin ☻\n   ↓↓↓")

        # Username Entry
        self.__username = tk.Entry(self)
        self.__username.place(x=120, y=162)
        # Password Entry
        self.__password = tk.Entry(self, show="*")
        self.__password.place(x=120, y=202)

        # Create buttons
        logButton = tk.Button(
            self,
            text="Giris", font=F["fgB1"],
            bg=C["bgB1"], fg=C["fgB1"],
            activebackground=C["bgB1"], activeforeground=C["activeFgB1"],
            command=self.loginApp)
        logButton.place(x=145, y=270, width=100)
        #
        rememberCheck = tk.Checkbutton(self, text='Beni Hatırla', fg=C["fgL1"], variable=self.value_x)
        rememberCheck.place(x=160, y=235)
        #
        goRegButton = tk.Button(
            self,
            text="Kaydol",
            relief=tk.FLAT,
            fg="#ff0000", bg="#fff",
            activebackground="#fff", activeforeground="#ff0000",
            command=lambda: controller.show_frame(RegisterPage)
        )
        goRegButton.place(x=100, y=370, width="53", height="15")
        # Pres Enter to Login
        logButton.bind("<Return>", self.loginApp)
        self.__password.bind("<Return>", self.loginApp)

    def loginApp(self, x=None):
        user = User(self.__username.get(), self.__password.get())
        user.login()
        if user.currentUser is None:
            messagebox.showerror("Admin", "Kullanıcı Adı Veya Şifre Yanlış!\n\n LÜTVEN TEKRAR DENEYİN ♥")
        else:
            Home.myCurrenUser = user
            if self.value_x.get():
                user.addCurrentData()

            Home.frames[HomePage].insertTdList()
            Home.frames[HomePage].insertCompTdList()
            self.__toplevel.myHome.deiconify()
            self.__toplevel.myHome.show_frame(HomePage)
            self.__toplevel.after(2000, self.__toplevel.destroy)
            # user.closeDbConnect()
#-----------------------------------------------------------------------------------------------------
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__toplevel = controller

        # Create Title Label
        LogOrRegister.creteTitleLabel(self, ["Kaydol", 25])

        # Create Labels
        LogOrRegister.crtNamePassLabels(self, "Zaten Hesabın Varmı?\nO Halde Hemen Giriş Yapabilirsin ☻\n   ↓↓↓")

        # Create Retry Password Entry
        passLabel2 = tk.Label(self, fg=C["fgL1"], font=F["fgL1"])
        passLabel2.config(text="Doğrula         :")
        passLabel2.place(x=10, y=240)

        # Create Username Entry
        self.__username = tk.Entry(self)
        self.__username.place(x=120, y=162)

        # Create Password Entry
        self.__password0 = tk.Entry(self, show="*")
        self.__password0.place(x=120, y=202)

        # Create Retry Password  Entry
        self.__password1 = tk.Entry(self, show="*")
        self.__password1.place(x=120, y=242)

        regButton = tk.Button(
            self,
            text="Kaydol", font=F["fgB1"],
            bg=C["bgB1"], fg=C["fgB1"],
            activebackground=C["bgB1"], activeforeground=C["activeFgB1"],
            command=self.registerApp)
        regButton.place(x=175, y=275)

        goLogButton = tk.Button(
            self,
            text="Giriş Yap",
            relief=tk.FLAT,
            bg="#fff", fg="#ff0000",
            activebackground="#fff", activeforeground="#ff0000",
            command=lambda: controller.show_frame(LoginPage))
        goLogButton.place(x=85, y=375, width="53", height="15")

        self.__password1.bind('<Return>', self.registerApp)


    def registerApp(self, x=None):
        if self.checkPassword():
            myUser = User(self.__username.get(), self.__password0.get())
            myUser.register()
            messagebox.showinfo("Admin", "KAYIT BAŞARILI ✔")
            self.__username.delete(0, "end")
            self.__password0.delete(0, "end")
            self.__password1.delete(0, "end")
            self.__toplevel.show_frame(LoginPage)


    def checkPassword(self):
        if (self.__password0.get() == self.__password1.get()):
            if (8 > len(self.__password0.get()) or len(self.__password0.get()) > 50):
                messagebox.showinfo("Admin", "Şifre; 8 karakterden küçük ve\n50 karakterden büyük olamaz")
                self.__password0.delete(0, "end")
                self.__password1.delete(0, "end")
                return False
            elif (" " in self.__password0.get()):
                messagebox.showinfo("Admin", "Şifrenin içinde boşluk olamaz !")

                self.__password0.delete(0, "end")
                self.__password1.delete(0, "end")

                return False
            elif len(self.__username.get()) == 0:
                messagebox.showinfo("Admin", "Kullanıcı alanı boş bırakılmaz !")
                return False
            elif User.checkUsername(self.__username.get()):
                messagebox.showinfo("Admin", "Kullanıcı Adı daha önce alınmış !\nLütven başka bir kullanıcı adı deneyin")
                self.__username.delete(0, "end")
                return False
            else:
                return True
        else:
            messagebox.showinfo("Admin", "Şifreler Uyuşmuyor.\nLÜTVEN TEKRAR DENEYİN ♥")
            self.__password1.delete(0, "end")
            return False
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    u = Home()
    u.mainloop()