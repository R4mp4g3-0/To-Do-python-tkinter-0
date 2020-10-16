import sqlite3 as sql
# anb



class To_Do:
    __connect = sql.connect("data.sqlite")
    __myCursor = __connect.cursor()

    def __init__(self):
        pass

    @staticmethod
    def closeDbConnect():
        To_Do.__connect.close()

    def addToDo(self, status, toDo, userId):
        sql_code = "INSERT INTO todos(durum,yapilacak,userId) VALUES (?,?,?)"
        values = (status, toDo, userId)
        self.sqlCommit(sql_code, values)

    def deleteToDo(self, id, yapilacak):
            sql_code = "DELETE FROM todos WHERE ((id=?) and (yapilacak=?))"
            values = (id, yapilacak)
            self.sqlCommit(sql_code, values)

    @staticmethod
    def deleteTodoes(userId):
        sql_code = "DELETE FROM todos WHERE (userId=?)"
        values = (userId,)
        To_Do.__myCursor.execute(sql_code, values)
        try:
            To_Do.__connect.commit()
        except sql.Error as err:
            print("eror:", err)


    def updateToDo(self, bool, id):
        sql_code = "UPDATE todos SET durum=? WHERE (id=?)"
        values = (bool, id)
        self.sqlCommit(sql_code, values)


    def getTo_does(self):
        sql_code = "SELECT durum,yapilacak FROM todos"

        To_Do.__myCursor.execute(sql_code)
        try:
            return To_Do.__myCursor.fetchall()
        except sql.Error as err:
            print('Hata : ', err)
        finally:
            # User.__connect.close()

            pass

    def getTo_doByUser(self, user):
        sql_code = "SELECT durum,yapilacak,id FROM todos WHERE (userId=?)"
        values = (user.currentUser[0],)

        To_Do.__myCursor.execute(sql_code, values)
        try:
            return To_Do.__myCursor.fetchall()
        except sql.Error as err:
            print('Hata : ', err)
        finally:
            # User.__connect.close()
            pass



    def sqlCommit(self, sql_code, values):
        To_Do.__myCursor.execute(sql_code, values)
        try:
            To_Do.__connect.commit()
        except sql.Error as err:
            print("eror:", err)











class User:
    __connect = sql.connect("data.sqlite")
    __myCursor = __connect.cursor()


    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.currentUser = tuple()

    @staticmethod
    def closeDbConnect():
        User.__connect.close()
    @staticmethod
    def createDbConnect():
        __connect = sql.connect("data.sqlite")
        __myCursor = __connect.cursor()

    def login(self):
        sql_code = "SELECT * FROM users WHERE (username=?) and (password=?)"
        values = (self.__username, self.__password)
        User.__myCursor.execute(sql_code, values)
        try:
            self.currentUser = User.__myCursor.fetchone()
        except sql.Error as err:
            print('Hata : ', err)
        finally:
            # User.__connect.close()
            pass


    def register(self):
        sql_code = "INSERT INTO users(username,password) VALUES (?,?)"
        values = (self.__username, self.__password)
        self.sqlCommit(sql_code, values)


    def sqlCommit(self,sql_code,values):
        User.__myCursor.execute(sql_code, values)
        try:
            User.__connect.commit()
        except sql.Error as err:
            print("eror:", err)


    @staticmethod
    def deleteUser(user):
            sql_code = "DELETE FROM users WHERE (id=?) and (password=?)"
            values = (user.currentUser[0], user.currentUser[2])
            User.__myCursor.execute(sql_code, values)
            try:
                User.__connect.commit()
            except sql.Error as err:
                print("eror:", err)



    def addCurrentData(self):
        sql_code = "INSERT INTO currentUser(userId,username,password) VALUES (?,?,?)"
        self.sqlCommit(sql_code, self.currentUser)



    @staticmethod
    def checkUsername(username):
        sql_code = "SELECT username FROM users"
        User.__myCursor.execute(sql_code)
        try:
            result = User.__myCursor.fetchall()
            for i in result:
                if username in i:
                    return True
            return False
        except sql.Error as err:
            print('Hata : ', err)



    @staticmethod
    def updateUser(user, newUsername, newPassword):
        sql_code = "UPDATE users SET username=?, password=? WHERE (id=?) and (username=?) and (password=?)"
        values = (newUsername, newPassword,
                  user.currentUser[0], user.currentUser[1], user.currentUser[2])
        User.__myCursor.execute(sql_code, values)
        try:
            User.__connect.commit()
        except sql.Error as err:
            print("eror:", err)

    @staticmethod
    def delCurrentData():
        sql_code = "DELETE  FROM currentUser"
        User.__myCursor.execute(sql_code)
        try:
            User.__connect.commit()
        except sql.Error as err:
            print("eror:", err)

    @staticmethod
    def currentData():
        sql_code = "SELECT * FROM currentUser "
        User.__myCursor.execute(sql_code)
        try:
            result = User.__myCursor.fetchone()
            if result is None:
                return False
            else:
                u = User(result[1], result[2])
                u.currentUser = result
                return u
        except sql.Error as err:
            print('Hata : ', err)






if __name__ == "__main__":
    # User.delCurrentData()
    pass
