import mysql.connector

class Database:
    def __init__(self):
        self.connection = None

    def Connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password=f"root",
                database="Server"
            )
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def setReceive(self, user, message):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO Receive (user, message) VALUES (%s, %s)", (user, message))
                print(user, message)
                self.connection.commit()
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Erro ao obter os tamanhos: {e}")
                return None
        else:
            print("Conexão não estabelecida.")
            return None

    def getSize(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT size FROM Data ORDER BY id DESC LIMIT 5")
                sizes = [size[0] for size in cursor.fetchall()]
                cursor.close()
                return sizes
            except mysql.connector.Error as e:
                print(f"Erro ao obter os tamanhos: {e}")
                return None
        else:
            print("Conexão não estabelecida.")
            return None

    def getTime(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT time FROM Data ORDER BY id DESC LIMIT 5")
                times = [time[0] for time in cursor.fetchall()]
                cursor.close()
                return times
            except mysql.connector.Error as e:
                print(f"Erro ao obter os tempos: {e}")
                return None
        else:
            print("Conexão não estabelecida.")
            return None
        
    def getAll(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM Receive")
                getAll = cursor.fetchall()
                cursor.close()
                return getAll
            except mysql.connector.Error as e:
                print(f"Erro ao obter os tempos: {e}")
                return None
        else:
            print("Conexão não estabelecida.")
            return None
    
    def getAllData2(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM Data2")
                getAll = cursor.fetchall()
                cursor.close()
                return getAll
            except mysql.connector.Error as e:
                print(f"Erro ao obter os tempos: {e}")
                return None
        else:
            print("Conexão não estabelecida.")
            return None
        
    def separete_data(self):
        self.database = Database()
        self.database.Connect()
        alldata = self.database.getAll()
        data = []
        datac = []
        for j in alldata:
            datac.append(j)
            if len(datac) == 5:
                data.append(datac)
                datac = []
        if datac:  
            data.append(datac)
        return data

    def separete_data2(self):
        self.database = Database()
        self.database.Connect()
        alldata = self.database.getAllData2()
        data = []
        datac = []
        for j in alldata:
            datac.append(j)
            if len(datac) == 25:
                data.append(datac)
                datac = []
        if datac:  
            data.append(datac)
        return data