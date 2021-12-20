from Models.DataBase import DataBase
from Models.QueryBuilder import QueryBuilder


class Word:

    def __init__(self, nom):
        self.nom = nom
        self.bd = DataBase('dictionary')
        self.query = QueryBuilder()

    def definition(self):
        return self.selectElt('definition')

    def etymologie(self):
        return self.selectElt('etymologie')

    def synonyme(self):
        return self.selectElt('synonyme')

    def etymologie(self):
        return self.selectElt('etymologie')

    def antonyme(self):
        return self.selectElt('antonyme')

    def homonyme(self):
        return self.selectElt('homonyme')

    def paronyme(self):
        return self.selectElt('paronyme')

    def existe(self):
        return self.selectElt('nom') != None

    def update(self, datas):
        self.query.cleaner()
        self.query.update('word', datas).where(
            'nom', '=', f" '{self.nom}'")
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.commit()

    def delete(self):
        self.query.cleaner()
        self.query.delete('word').where('nom', '=', f" '{self.nom}'")
        self.bd.requete = self.query
        self.bd.execute()
        self.bd.commit()

    def selectElt(self, nom):
        self.query.cleaner()
        self.query.select([nom], 'word').where(
            'nom', '=', f" '{self.nom}'")
        self.bd.requete = self.query
        self.bd.execute().fetchOne()
        if self.bd.results == None:
            result = None
        else:
            result = self.bd.results[0]
        return result
