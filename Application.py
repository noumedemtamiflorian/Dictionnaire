from tkinter import *
from tkinter import messagebox
from Models.Dictionary import Dictionary
from Models.Word import Word
from functools import partial


class Application:

    def __init__(self, root):
        self.root = root
        self.root.title('Dictionaire')
        self.root.geometry("470x700+0+0")
        self.root.resizable(1000, 1000)
        self.mot = StringVar()
        self.motSearch = StringVar(value="")
        self.action = 'home'
        self.dictionary = Dictionary()

        Button(self.root, text="Liste de mot",
               command=self.display
               ).place(y=5, x=20)
        Button(self.root, text="Ajouter un mot",
               command=self.addWord
               ).place(y=5, x=153)
        Button(self.root, text="Rechercher un mot",
               command=self.search
               ).place(y=5, x=300)

        self.mainFrame = Frame(self.root, width=470,
                               height=1000,)
        self.mainFrame.place(x=0, y=50)

        self.display()

    def destroyWidget(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

# Supprimer

    def deleteWord(self, nom):
        self.destroyWidget()
        Label(self.mainFrame, text=f"Suppression du mot {nom}",
              justify="center").place(x=150, y=25)

        Label(self.mainFrame, text="Voulez vouz supprimer ce mot").place(
            x=125, y=100)

        Button(self.mainFrame, command=partial(self.delete, nom), text="Oui").place(
            x=150, y=150)
        Button(self.mainFrame, command=self.display, text="Non").place(
            x=250, y=150)

    def delete(self, nom):
        self.dictionary.supprimerUnMot(nom)
        self.display()
# lister de mot

    def display(self):
        self.destroyWidget()
        Label(self.mainFrame, text="Liste de mot",
              justify="center").place(x=200, y=10)
        resultats = Dictionary().afficherTout()
        i, y = 0, 50
        for resultat in resultats:
            i += 1
            Label(self.mainFrame, text=f"{i}- {resultat[0]}").place(x=20, y=y)
            Button(self.mainFrame, command=partial(self.consulterMot,
                   resultat[0]), text="consulter").place(x=175, y=y)
            Button(self.mainFrame, text="supprimer", command=partial(self.deleteWord,
                                                                     resultat[0])).place(x=275, y=y)
            Button(self.mainFrame,  command=partial(self.updateWord,
                                                    resultat[0]), text="modifier").place(x=375, y=y)
            y += 50

# consulter un mot

    def consulterMot(self, nom):
        self.destroyWidget()
        self.mot.set(nom)
        mot = Word(self.mot.get())
        Label(self.mainFrame, text=f"Consultation du mot {self.mot.get()}",
              justify="center").place(x=200, y=10)

        i = 50
        if mot.etymologie() != None:
            Label(self.mainFrame, text="Etymologie : ").place(x=100, y=i)
            Label(self.mainFrame, wraplength=250,
                  text=mot.etymologie()).place(x=200, y=i)

        if mot.definition() != None:
            i += 50
            Label(self.mainFrame, text="Definition : ").place(x=100, y=i)
            Label(self.mainFrame, wraplength=250,
                  text=mot.definition()).place(x=200, y=i)

        if mot.synonyme() != None:
            i += 50
            Label(self.mainFrame, text="Synonyme : ").place(x=100, y=i)
            Label(self.mainFrame, wraplength=250,
                  text=mot.synonyme()).place(x=200, y=i)

        if mot.antonyme() != None:
            i += 50
            Label(self.mainFrame, text="Antonyme : ").place(x=100, y=i)
            Label(self.mainFrame, wraplength=250,
                  text=mot.antonyme()).place(x=200, y=i)

        if mot.homonyme() != None:
            i += 50
            Label(self.mainFrame, text="Homonyme : ").place(x=100, y=i)
            Label(self.mainFrame, wraplength=250,
                  text=mot.homonyme()).place(x=200, y=i)

        if mot.paronyme() != None:
            i += 50
            Label(self.mainFrame, text="Paronyme : ").place(x=100, y=i)
            Label(self.mainFrame,  wraplength=250,
                  text=mot.paronyme()).place(x=200, y=i)

        if mot.difficulte() != None:
            i += 50
            Label(self.mainFrame, text="Difficulte : ").place(x=100, y=i)
            Label(self.mainFrame,  wraplength=250,
                  text=mot.difficulte()).place(x=200, y=i)

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
        self.synonyme.set(mot.synonyme() if mot.synonyme() != None else '')
        self.antonyme.set(mot.antonyme()if mot.antonyme() != None else '')
        self.homonyme.set(mot.homonyme()if mot.homonyme() != None else '')
        self.paronyme.set(mot.paronyme()if mot.paronyme() != None else '')
        self.difficulte.set(
            mot.difficulte()if mot.difficulte() != None else '')
        self.etymologie.set(
            mot.etymologie()if mot.etymologie() != None else '')

        Label(self.mainFrame, text="Modifier un mot",
              justify="center").place(x=200, y=10)

        Label(self.mainFrame, text="Nom : ").place(x=100, y=50)
        Entry(self.mainFrame, textvariable=self.nom).place(x=200, y=50)

        Label(self.mainFrame, text="Definition : ").place(x=100, y=100)
        Entry(self.mainFrame, textvariable=self.definition).place(
            x=200, y=90, width=165, height=50)

        Label(self.mainFrame, text="Synonyme : ").place(x=100, y=150)
        Entry(self.mainFrame, textvariable=self.synonyme).place(x=200, y=150)

        Label(self.mainFrame, text="Antonyme : ").place(x=100, y=200)
        Entry(self.mainFrame, textvariable=self.antonyme).place(x=200, y=200)

        Label(self.mainFrame, text="Homonyme : ").place(x=100, y=250)
        Entry(self.mainFrame, textvariable=self.homonyme).place(x=200, y=250)

        Label(self.mainFrame, text="Difficulte : ").place(x=100, y=300)
        Entry(self.mainFrame, textvariable=self.difficulte).place(x=200, y=300)

        Label(self.mainFrame, text="Paronyme : ").place(x=100, y=350)
        Entry(self.mainFrame, textvariable=self.paronyme).place(x=200, y=350)

        Label(self.mainFrame, text="Etymologie : ").place(x=100, y=400)
        Entry(self.mainFrame, textvariable=self.etymologie).place(x=200, y=400)

        Button(self.mainFrame, text="Modifier",
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

        Label(self.mainFrame, text="Ajouter un mot",
              justify="center").place(x=200, y=10)

        Label(self.mainFrame, text="Nom : ").place(x=100, y=50)
        Entry(self.mainFrame, textvariable=self.nom).place(x=200, y=50)

        Label(self.mainFrame, text="Definition : ").place(x=100, y=100)
        Entry(self.mainFrame, textvariable=self.definition).place(
            x=200, y=90, width=165, height=50)

        Label(self.mainFrame, text="Synonyme : ").place(x=100, y=150)
        Entry(self.mainFrame, textvariable=self.synonyme).place(x=200, y=150)

        Label(self.mainFrame, text="Antonyme : ").place(x=100, y=200)
        Entry(self.mainFrame, textvariable=self.antonyme).place(x=200, y=200)

        Label(self.mainFrame, text="Homonyme : ").place(x=100, y=250)
        Entry(self.mainFrame, textvariable=self.homonyme).place(x=200, y=250)

        Label(self.mainFrame, text="Paronyme : ").place(x=100, y=300)
        Entry(self.mainFrame, textvariable=self.paronyme).place(x=200, y=300)

        Label(self.mainFrame, text="Difficulte : ").place(x=100, y=350)
        Entry(self.mainFrame, textvariable=self.difficulte).place(x=200, y=350)

        Label(self.mainFrame, text="Etymologie : ").place(x=100, y=400)
        Entry(self.mainFrame, textvariable=self.etymologie).place(x=200, y=400)

        Button(self.mainFrame, text="Enregistrer",
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


# rechercher un mot

    def search(self):
        self.destroyWidget()
        Label(
            self.mainFrame,
            text="Rechercher un mot",
            bd=10,
            font=('Algerian', 10, "bold"),
            fg='white'
        ).place(x=0, y=0, width=470)
        Entry(self.mainFrame, textvariable=self.motSearch, font=(
            'times new roman', 20, "bold"),
        ).place(x=30, y=45)
        Button(
            self.mainFrame,
            text="Rechercher",
            font=('Algerian', 10),
            bg='cyan',
            command=self.rechercher
        ).place(x=300, y=46)
    ##################################
        self.rltFrame = Frame(self.mainFrame)
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
                          text=f"{i} -  {result[0]}"
                          ).place(x=40, y=y)
                    y += 40
            else:
                Label(self.rltFrame,
                      text=f"Aucun mot contenant le caractere {self.motSearch.get()}"
                      ).place(x=40, y=10)
