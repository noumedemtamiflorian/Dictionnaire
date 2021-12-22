class QueryBuilder:

    def __init__(self):
        self.requete = ""

    def select(self, champs, table):
        champs = " , ".join(champs)
        self.requete += f' SELECT {champs} FROM {table}'
        return self

    def where(self, champ, operateur, value):
        self.requete += f' WHERE {champ} {operateur} {value}'
        return self

    def whereOr(self, champ, operateur, value):
        self.requete += f' OR {champ} {operateur} {value}'
        return self

    def whereAnd(self, champ, operateur, value):
        self.requete += f' AND  {champ} {operateur} {value}'
        return self

    def insert(self, table, datas):
        values = ",".join(['"'+str(x)+'"' for x in datas.values()])
        columns = ",".join([str(x) for x in datas.keys()])
        self.requete += f' INSERT INTO {table} ({columns}) VALUES({values})'
        return self

    def orderBY(self, datas):
        condition = ""
        for key, value in datas.items():
            condition += f' {key}  {value},'
        requete = f' ORDER BY {condition}'
        self.requete += requete[0:-1]
        return self

    def update(self, table, datas):
        condition = ""
        for key, value in datas.items():
            condition += f'{key} = "{value}",'
        requete = f' UPDATE {table} SET {condition}'
        self.requete += requete[0:-1]
        return self

    def delete(self, table):
        self.requete += f' DELETE FROM {table}'
        return self

    def like(self, champ, recherche):
        isWhere = self.requete.find('WHERE') != -1
        if(isWhere):
            where = " AND "
        else:
            where = " WHERE "
        self.requete += f' {where} {champ} LIKE "%{recherche}%"'
        return self

    def cleaner(self):
        self.requete = ""
        return self

    def __str__(self):
        return self.requete
