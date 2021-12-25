from tkinter import *
from tkinter import messagebox
from Models.Dictionary import Dictionary
from Models.Word import Word
from functools import partial


class Application:

    def __init__(self, root):
        self.root = root
        self.root.title('Dictionaire')
        self.root.geometry("500x700+0+0")
        self.root.resizable(1000, 1000)
        self.root['bg'] = "#26CFFF"
        self.bgFont = "#26CFFF"
        self.mot = StringVar()
        self.motSearch = StringVar(value="")
        self.action = 'home'
        self.dictionary = Dictionary()
        self.menu()
        self.canvas()
        self.search()

    def canvas(self):

        canvas = Canvas(self.root, background="#26CFFF", width=200)
        scroll_y = Scrollbar(self.root, orient="vertical",
                             command=canvas.yview)

        self.mainFrame = Frame(canvas, width=470,
                               height=3000,)
        self.mainFrame['bg'] = "#26CFFF"
        self.mainFrame.pack()

        canvas.create_window(0, 0, anchor='nw', window=self.mainFrame)
        # make sure everything is displayed before configuring the scrollregion
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox(
            'all'), yscrollcommand=scroll_y.set)

        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')

    def menu(self):
        menubar = Menu(self.root,
                       activebackground="#26CFFF",
                       background="#26CFFF")
        menubar.add_command(
            activebackground="#DEC221",
            background="#DEC221",
            label="Liste de mots",
            command=self.display, compound=LEFT
        )
        menubar.add_command(
            activebackground="#26CFFF",
            background="#26CFFF",
            label=15*" ",)
        menubar.add_command(label="Ajouter un mot",
                            activebackground="#F55E31",
                            background="#F55E31",
                            compound=CENTER,
                            command=self.addWord)
        menubar.add_command(
            activebackground="#26CFFF",
            background="#26CFFF",
            label=15*" ",)
        menubar.add_command(label="Rechercher un mot",
                            activebackground="#4BFA71",
                            background="#4BFA71",
                            compound=RIGHT,
                            command=self.search)
        self.root.config(menu=menubar)

    def destroyWidget(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

# Supprimer

    def deleteWord(self, nom):
        self.destroyWidget()
        Label(self.mainFrame,
              font=('Algerian', 15, "bold"),
              bg=self.bgFont, text=f"Suppression du mot {nom}",
              justify="center").place(x=100, y=25)

        Label(self.mainFrame, bg=self.bgFont, text="Voulez vouz supprimez ce mot").place(
            x=125, y=100)

        Button(self.mainFrame,
               activebackground="#DEC221",
               bg='#DEC221', command=partial(self.delete, nom), text="Oui").place(
            x=150, y=150)
        Button(self.mainFrame,
               activebackground="#4BFA71", bg='#4BFA71', command=self.display, text="Non").place(
            x=250, y=150)
# Supprimer un mot

    def delete(self, nom):
        self.dictionary.supprimerUnMot(nom)
        messagebox.showinfo(message=f"Le mot {nom} a bien ete supprimer")
        self.display()
# lister de mot

    def display(self):
        self.destroyWidget()

        Label(self.mainFrame,
              bg="#26CFFF",
              font=('times new roman', 20, "bold"),
              text="Liste de mots",
              justify="center").place(x=175, y=8)
        resultats = Dictionary().afficherTout()
        i, y = 0, 50
        for resultat in resultats:
            i += 1
            Label(self.mainFrame,
                  bg="#26CFFF",
                  fg="#8F21DE",
                  font=('Algerian', 10, "bold"),
                  text=f"{i}- {resultat[0]}").place(x=20, y=y)
            Button(self.mainFrame,
                   activebackground="#DEC221",
                   bg="#DEC221",
                   command=partial(self.consulterMot,
                                   resultat[0]), text="Consulter").place(x=175, y=y)
            Button(self.mainFrame,
                   activebackground="red",
                   bg="#F55E31",
                   text="Supprimer", command=partial(self.deleteWord,
                                                     resultat[0])).place(x=275, y=y)
            Button(self.mainFrame,
                   activebackground="#4BFA71",
                   bg="#4BFA71", command=partial(self.updateWord,
                                                 resultat[0]), text="Modifier").place(x=375, y=y)
            y += 50

# consulter un mot

    def consulterMot(self, nom):
        self.destroyWidget()
        self.mot.set(nom)
        mot = Word(self.mot.get())
        Label(self.mainFrame,
              bg=self.bgFont,
              font=('Algerian', 15, "bold"), text=f"Consultation du mot {self.mot.get()}",
              justify="center").place(x=50, y=10)
        i = 0
        print(mot.definition() == '')
        if len(mot.etymologie()) != 0:
            i += 50
            Label(self.mainFrame, bg=self.bgFont, font=('Algerian', 10, "bold"),
                  text="Etymologie : ").place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont, wraplength=250,
                  text=mot.etymologie()).place(x=200, y=i)

        if len(mot.definition()) != 0:
            i += 50
            Label(self.mainFrame, bg=self.bgFont, font=('Algerian', 10, "bold"),
                  text="Definition : ").place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont, wraplength=250,
                  text=mot.definition()).place(x=200, y=i)

        if len(mot.synonyme()) != 0:
            i += 50
            Label(self.mainFrame, bg=self.bgFont, font=('Algerian', 10, "bold"),
                  text="Synonyme : ").place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont, wraplength=250,
                  text=mot.synonyme()).place(x=200, y=i)

        if len(mot.antonyme()) != 0:
            i += 50
            Label(self.mainFrame,  bg=self.bgFont, font=('Algerian', 10, "bold"),
                  text="Antonyme : ").place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont, wraplength=250,
                  text=mot.antonyme()).place(x=200, y=i)

        if len(mot.homonyme()) != 0:
            i += 50
            Label(self.mainFrame, bg=self.bgFont, text="Homonyme : ", font=(
                'Algerian', 10, "bold")).place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont, wraplength=250,
                  text=mot.homonyme()).place(x=200, y=i)

        if len(mot.paronyme()) != 0:
            i += 50
            Label(self.mainFrame, bg=self.bgFont, text="Paronyme : ", font=(
                'Algerian', 10, "bold")).place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont, wraplength=250,
                  text=mot.paronyme()).place(x=200, y=i)

        if len(mot.difficulte()) != 0:
            i += 50
            Label(self.mainFrame, bg=self.bgFont, text="Difficulte : ", font=(
                'Algerian', 10, "bold")).place(x=100, y=i)
            Label(self.mainFrame, bg=self.bgFont,  wraplength=250,
                  text=mot.difficulte()).place(x=200, y=i)
        i += 150
        Button(self.mainFrame,
               activebackground="#DEC221",
               bg="#DEC221",
               command=partial(self.updateWord, nom), text="Modifier").place(x=175, y=i)
        Button(self.mainFrame,
               activebackground="red",
               bg="#F55E31",
               text="Supprimer", command=partial(self.deleteWord,
                                                 nom)).place(x=275, y=i)


# Modifier un mot


    def updateWord(self, nom):
        self.destroyWidget()
        self.nom = StringVar()
        self.definition = StringVar()
        self.synonyme = StringVar()
        self.antonyme = StringVar()
        self.homonyme = StringVar()
        self.paronyme = StringVar()
        self.etymologie = StringVar()
        self.difficulte = StringVar()
        self.mot.set(nom)

        mot = Word(self.mot.get())

        self.nom.set(self.mot.get())
        self.definition.set(mot.definition())
        self.synonyme.set(mot.synonyme())
        self.antonyme.set(mot.antonyme())
        self.homonyme.set(mot.homonyme())
        self.paronyme.set(mot.paronyme())
        self.difficulte.set(
            mot.difficulte()if mot.difficulte() != None else '')
        self.etymologie.set(
            mot.etymologie()if mot.etymologie() != None else '')

        Label(self.mainFrame, bg=self.bgFont,
              font=('Algerian', 15, "bold"),
              text="Modifier un mot",
              justify="center").place(x=150, y=10)

        Label(self.mainFrame, bg=self.bgFont, text="Nom : ").place(x=100, y=50)
        Entry(self.mainFrame, textvariable=self.nom).place(x=200, y=50)

        Label(self.mainFrame, bg=self.bgFont,
              text="Definition : ").place(x=100, y=100)
        Entry(self.mainFrame, textvariable=self.definition).place(
            x=200, y=90, width=165, height=50)

        Label(self.mainFrame, bg=self.bgFont,
              text="Synonyme : ").place(x=100, y=150)
        Entry(self.mainFrame, textvariable=self.synonyme).place(x=200, y=150)

        Label(self.mainFrame, bg=self.bgFont,
              text="Antonyme : ").place(x=100, y=200)
        Entry(self.mainFrame, textvariable=self.antonyme).place(x=200, y=200)

        Label(self.mainFrame, bg=self.bgFont,
              text="Homonyme : ").place(x=100, y=250)
        Entry(self.mainFrame, textvariable=self.homonyme).place(x=200, y=250)

        Label(self.mainFrame, bg=self.bgFont,
              text="Difficulte : ").place(x=100, y=300)
        Entry(self.mainFrame, textvariable=self.difficulte).place(x=200, y=300)

        Label(self.mainFrame, bg=self.bgFont,
              text="Paronyme : ").place(x=100, y=350)
        Entry(self.mainFrame, textvariable=self.paronyme).place(x=200, y=350)

        Label(self.mainFrame, bg=self.bgFont,
              text="Etymologie : ").place(x=100, y=400)
        Entry(self.mainFrame, textvariable=self.etymologie).place(x=200, y=400)

        Button(self.mainFrame, text="Modifier",
               activebackground="#DEC221",
               bg="#DEC221",
               command=partial(self.modifier, nom)).place(x=200, y=450)

    def modifier(self, nom):
        if self.definition.get() == "" or self.nom.get() == "":
            messagebox.showerror(message=f"Entrer un nom et une definition")
        else:
            if Word(self.nom.get()).existe() and self.nom.get() == self.nom:
                messagebox.showerror(message=f"Un modifier le nom")
            else:
                datas = {
                    'nom': self.nom.get(),
                    'definition': self.definition.get(),
                    'etymologie': self.etymologie.get(),
                    'synonyme': self.synonyme.get(),
                    'antonyme': self.antonyme.get(),
                    'paronyme': self.paronyme.get(),
                    'homonyme': self.homonyme.get(),
                    'difficulte': self.difficulte.get()
                }
                self.dictionary.modifierUnMot(nom, datas)
                messagebox.showinfo(message=f"Mot modifier avec succes")
                self.display()


# Ajouter un mot


    def addWord(self):
        self.destroyWidget()

        self.nom = StringVar()
        self.definition = StringVar()
        self.synonyme = StringVar()
        self.antonyme = StringVar()
        self.homonyme = StringVar()
        self.paronyme = StringVar()
        self.etymologie = StringVar()
        self.difficulte = StringVar()

        Label(self.mainFrame, bg=self.bgFont,
              font=('Algerian', 15, "bold"), text="Ajouter un mot",
              justify="center").place(x=200, y=10)

        Label(self.mainFrame,  bg=self.bgFont,
              text="Nom : ").place(x=100, y=50)
        Entry(self.mainFrame, textvariable=self.nom).place(x=200, y=50)

        Label(self.mainFrame, bg=self.bgFont,
              text="Definition : ").place(x=100, y=100)
        Entry(self.mainFrame, textvariable=self.definition).place(
            x=200, y=90, width=165, height=50)

        Label(self.mainFrame, bg=self.bgFont,
              text="Synonyme : ").place(x=100, y=150)
        Entry(self.mainFrame, textvariable=self.synonyme).place(x=200, y=150)

        Label(self.mainFrame, bg=self.bgFont,
              text="Antonyme : ").place(x=100, y=200)
        Entry(self.mainFrame, textvariable=self.antonyme).place(x=200, y=200)

        Label(self.mainFrame, bg=self.bgFont,
              text="Homonyme : ").place(x=100, y=250)
        Entry(self.mainFrame, textvariable=self.homonyme).place(x=200, y=250)

        Label(self.mainFrame, bg=self.bgFont,
              text="Paronyme : ").place(x=100, y=300)
        Entry(self.mainFrame, textvariable=self.paronyme).place(x=200, y=300)

        Label(self.mainFrame, bg=self.bgFont,
              text="Difficulte : ").place(x=100, y=350)
        Entry(self.mainFrame, textvariable=self.difficulte).place(x=200, y=350)

        Label(self.mainFrame, bg=self.bgFont,
              text="Etymologie : ").place(x=100, y=400)
        Entry(self.mainFrame, textvariable=self.etymologie).place(x=200, y=400)

        Button(self.mainFrame,
               activebackground="#F55E31",
               bg="#F55E31", text="Enregistrer",
               command=self.enregistrer).place(x=200, y=450)

    def enregistrer(self):
        if self.definition.get() == "" or self.nom.get() == "":
            messagebox.showerror(message=f"Entrer un nom et une definition")
        else:
            if Word(self.nom.get()).existe():
                messagebox.showerror(message=f"Un mot avec ce nom existe deja")
            else:
                datas = {
                    'nom': self.nom.get(),
                    'definition': self.definition.get(),
                    'etymologie': self.etymologie.get(),
                    'synonyme': self.synonyme.get(),
                    'antonyme': self.antonyme.get(),
                    'paronyme': self.paronyme.get(),
                    'homonyme': self.homonyme.get(),
                    'difficulte': self.difficulte.get()
                }
                self.dictionary.AjouterUnMot(datas)
                self.nom.set('')
                self.definition.set('')
                self.etymologie.set('')
                self.synonyme.set('')
                self.antonyme.set('')
                self.paronyme.set('')
                self.homonyme.set('')
                self.difficulte.set('')
                messagebox.showinfo(message=f"Mot enregistrer avec succes")
                self.display()

# rechercher un mot

    def search(self):
        self.destroyWidget()
        Label(
            self.mainFrame,
            text="Rechercher un mot",
            bd=10,
            bg=self.bgFont,
            font=('Algerian', 15, "bold"),
        ).place(x=0, y=0, width=470)
        Entry(self.mainFrame,
              textvariable=self.motSearch,
              font=('times new roman', 20, "bold"),
              ).place(x=30, y=45)
        Button(
            self.mainFrame,
            text="Rechercher",
            font=('Algerian', 10),
            activebackground="#4BFA71",
            bg="#4BFA71",
            command=self.rechercher
        ).place(x=300, y=46)
    ##################################

        self.rltFrame = Frame(self.mainFrame, bg=self.bgFont,)
        self.rltFrame.place(x=0, y=100, width=450, height=600)

    def rechercher(self):
        if self.motSearch.get() == "":
            messagebox.showerror(
                message="Entrer au moins une chaine de caractere")
        else:
            for widget in self.rltFrame.winfo_children():
                widget.destroy()
            dictionary = Dictionary()
            results = dictionary.rechercherUnMot(self.motSearch.get())
            if results != None:
                y = 10
                i = 0
                for result in results:
                    i += 1
                    Label(self.rltFrame,
                          bg=self.bgFont,
                          text=f"{i} -  {result[0]}"
                          ).place(x=40, y=y)
                    Button(self.rltFrame,
                           activebackground="#DEC221",
                           bg='#DEC221',
                           command=partial(self.consulterMot, result[0]),
                           text="Consulter").place(
                        x=300, y=y)
                    y += 40
            else:
                Label(self.rltFrame,
                      bg=self.bgFont,
                      text=f"Aucun mot contenant le caractere {self.motSearch.get()}"
                      ).place(x=40, y=10)
