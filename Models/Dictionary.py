from Models.DataBase import DataBase
from Models.QueryBuilder import QueryBuilder
from Models.Word import Word


class Dictionary:

    def __init__(self):
        self.bd = DataBase('dictionary')
        self.query = QueryBuilder()
        self.word = Word('')

    def afficherTout(self):
        self.query.cleaner()
        self.query.select(['nom'], 'word')
        self.query.orderBY({'id': 'DESC'})
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.fetchAll()
        results = self.bd.results
        return results

    def afficherUnMot(self, nom):
        self.word.nom = nom
        return {
            'definition': self.word.definition(),
            'etymologie': self.word.etymologie(),
            'synonyme': self.word.synonyme(),
            'antonyme': self.word.antonyme(),
            'paronyme': self.word.paronyme(),
            'homonyme': self.word.homonyme()
        }

    def rechercherUnMot(self, nom):
        self.query.cleaner()
        self.query.select(['nom'], 'word').like('nom', f"{nom}")
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.fetchAll()
        results = self.bd.results
        if len(results) != 0:
            return results
        else:
            return None

    def AjouterUnMot(self, datas):
        self.query.cleaner()
        self.query.insert('word', datas)
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.commit()

    def modifierUnMot(self, nom, datas):
        self.query.cleaner()
        self.query.update('word', datas)
        self.query.where('nom', '=', f'"{nom}"')
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.commit()

    def supprimerUnMot(self, nom):
        self.query.cleaner()
        self.query.delete('word')
        self.query.where('nom', '=', f'"{nom}"')
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.commit()
