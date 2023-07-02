import mysql.connector as x
import time as z


db = x.connect(host="localhost",user = "root",password = "")
cur = db.cursor()
if db.is_connected():
    print("Successfully connected")

    
print(db)

def database():
    try:
        db = x.connect(host="localhost",user = "root",password = "")
        cur = db.cursor()
        cur.execute("CREATE DATABASE OTT_DBMS")
        cur.execute("USE OTT_DBMS")

        cur.execute("CREATE TABLE IF NOT EXISTS Shows(Show_ID VARCHAR(10) PRIMARY KEY, Name VARCHAR(30), Genre VARCHAR(20),No_Of_Seasons INT, No_Of_Episodes INT, IMDb_Rating float, Platform VARCHAR(20))")

        cur.execute("CREATE TABLE IF NOT EXISTS Movies(Movie_ID VARCHAR(10) PRIMARY KEY, Name VARCHAR(30), Genre VARCHAR(20), IMDb_Rating float,Platform VARCHAR(20))")

        cur.execute("CREATE TABLE IF NOT EXISTS OTT(OTT_ID VARCHAR(10),Platform VARCHAR(20), No_Of_Shows INT, No_Of_Movies INT, No_Of_Subscribers INT)")


        cur.execute("CREATE TABLE IF NOT EXISTS Movie_OTT(Movie_ID VARCHAR(10), OTT_ID VARCHAR(10),FOREIGN KEY(Movie_ID) REFERENCES Movies(Movie_ID))")

        cur.execute("CREATE TABLE IF NOT EXISTS Show_OTT(Show_ID VARCHAR(10), OTT_ID VARCHAR(10),FOREIGN KEY(Show_ID) REFERENCES Shows(Show_ID))")

        cur.execute("CREATE TABLE IF NOT EXISTS Subscriber(Subscriber_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT, Name VARCHAR(30), Phone_Number VARCHAR(10),No_Of_Subscribed_OTT_Platforms INT)")

        print("database created")
        print("tables created")
    
        cur.close()
        db.close()

    except Exception as f:
        print("CANNOT CREATE DATABASE", 'REASON', f)
        pass


def insert_values_shows():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        cur.execute("INSERT INTO Shows VALUES('S01','Friends','Comedy',10,120,9,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S02','Money Heist','Thriller',5,50,9,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S03','The Game Of Thrones','Drama',8,76,8,'Hotstar')")
        cur.execute("INSERT INTO Shows VALUES('S04','House Of The Dragon','Drama',1,10,8,'Hotstar')")
        cur.execute("INSERT INTO Shows VALUES('S05','Asur','Thriller',1,8,8.4,'Voot')")
        cur.execute("INSERT INTO Shows VALUES('S06','All Of Us Are Dead','Thriller',1,10,7.5,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S07','Stranger Things','Mystery',4,40,8.7,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S08','Never Have I Ever','Drama',3,30,7.9,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S09','The Originals','Drama',5,120,8.3,'Amazon Prime')")
        cur.execute("INSERT INTO Shows VALUES('S10','The Vampire Diaries','Drama',8,120,9,'Amazon Prime')")
        cur.execute("INSERT INTO Shows VALUES('S11','Squid Game','Thriller',1,10,8,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S12','13 Reasons Why','Drama',4,36,7.5,'Amazon Prime')")
        cur.execute("INSERT INTO Shows VALUES('S13','Dark','Mystery',3,30,8.7,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S14','Peaky Blinders','Drama',6,48,8.8,'Hotstar')")
        cur.execute("INSERT INTO Shows VALUES('S15','Violet Evergarden','Romance',1,12,8.4,'Viki')")
        cur.execute("INSERT INTO Shows VALUES('S16','Buisness Proposal','Romance',1,16,8.1,'Viki')")
        cur.execute("INSERT INTO Shows VALUES('S17','More than Friends','Romance',1,16,6.7,'Hotstar')")
        cur.execute("INSERT INTO Shows VALUES('S18','Our Beloved Summer','Coming-of-age',1,16,8.3,'Netflix')")
        cur.execute("INSERT INTO Shows VALUES('S19','Extraordinary You','Romance',1,16,7.8,'MX Player')")
        cur.execute("INSERT INTO Shows VALUES('S20','Pinocchio','Drama',1,16,8.1,'MX Player')")
        db.commit()
        cur.close()
        db.close()
        


    except Exception as f:
        print("CANNOT INSERT VALUES IN SHOWS TABLE", 'REASON', f)
        pass



def insert_values_movies():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor() 
        cur.execute("INSERT INTO Movies VALUES('MV01','Parasite','Thriller',8.5,'Amazon Prime')")
        cur.execute("INSERT INTO Movies VALUES('MV02','The Conjuring','Horror',7.5,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV03','Interstellar','Sci-fi',8.6,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV04','The Martian','Sci-fi',8,'Apple TV')")   
        cur.execute("INSERT INTO Movies VALUES('MV05','Inception','Action',8.8,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV06','Little Women','Drama',7.8,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV07','Dune','Sci-fi',8,'Hotstar')")   
        cur.execute("INSERT INTO Movies VALUES('MV08','Dont Breathe','Thriller',7.1,'MX Player')")   
        cur.execute("INSERT INTO Movies VALUES('MV09','20th Century Girl','Romance',7.3,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV10','The Amazing Spider-Man','Action',6.9,'Hotstar')")   
        cur.execute("INSERT INTO Movies VALUES('MV11','Pride and Prejudice','Romance',7.8,'Netflix')") 
        cur.execute("INSERT INTO Movies VALUES('MV12','Annabelle Comes Home','Horror',5.9,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV13','Titanic','Romance',7.9,'Amazon Prime')")   
        cur.execute("INSERT INTO Movies VALUES('MV14','The Exorcist','Horror',8.1,'Amazon Prime')")   
        cur.execute("INSERT INTO Movies VALUES('MV15','The Avengers','Adventure',8,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV16','The Girl On The Train','Mystery',6.5,'Amazon Prime')")   
        cur.execute("INSERT INTO Movies VALUES('MV17','Gone Girl','Thriller',8.1,'Hotstar')")   
        cur.execute("INSERT INTO Movies VALUES('MV18','Nightcrawler','Thriller',7.8,'Netflix')")   
        cur.execute("INSERT INTO Movies VALUES('MV19','Tune In For Love','Romance',7.1,'Viki')")   
        cur.execute("INSERT INTO Movies VALUES('MV20','If I Stay','Romance',6.7,'Amazon Prime')")     
        db.commit()
        cur.close()
        db.close()



    except Exception as f:
        print("CANNOT INSERT VALUES IN MOVIES TABLE", 'REASON', f)
        pass    

def insert_values_OTT():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        cur.execute("INSERT INTO OTT VALUES('OTT01','Netflix',1000,1000,8000)")
        cur.execute("INSERT INTO OTT VALUES('OTT02','Hotstar',4000,3000,10000)")
        cur.execute("INSERT INTO OTT VALUES('OTT03','Amazon Prime',3000,2000,20000)")
        cur.execute("INSERT INTO OTT VALUES('OTT04','MX Player',10000,1000,2000)")
        cur.execute("INSERT INTO OTT VALUES('OTT05','Voot',500,300,5000)")
        cur.execute("INSERT INTO OTT VALUES('OTT06','Viki',400,100,4000)")
        cur.execute("INSERT INTO OTT VALUES('OTT07','Apple TV',200,100,1000)")
        db.commit()
        cur.close()
        db.close()

    except Exception as f:
        print("CANNOT INSERT VALUES IN OTT TABLE", 'REASON', f)
        pass   


def insert_subscribers():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        cur.execute("INSERT INTO Subscriber VALUES(101,'Purvi Rathore','9876543210',6)")
        cur.execute("INSERT INTO Subscriber VALUES(102,'Jigyaasa Meena','9876512340',3)")
        cur.execute("INSERT INTO Subscriber VALUES(103,'Shruti Pandey','9845673210',5)")
        cur.execute("INSERT INTO Subscriber VALUES(104,'Megha Gaur','8876543210',1)")
        cur.execute("INSERT INTO Subscriber VALUES(105,'Elena Gilbert','3117654378',4)")
        db.commit()
        cur.close()
        db.close()

    except Exception as f:
        print("CANNOT INSERT VALUES IN SUBSCRIBER TABLE", 'REASON', f)
        pass   



def insert_values_movie_ott():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()   
        cur.execute("INSERT INTO Movie_OTT VALUES('MV01','OTT03')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV02','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV03','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV04','OTT07')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV05','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV06','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV07','OTT02')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV08','OTT04')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV09','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV10','OTT02')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV11','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV12','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV13','OTT03')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV14','OTT03')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV15','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV16','OTT03')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV17','OTT02')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV18','OTT01')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV19','OTT06')")
        cur.execute("INSERT INTO Movie_OTT VALUES('MV20','OTT03')")
        db.commit()
        cur.close()
        db.close()

    except Exception as f:
        print("CANNOT INSERT VALUES IN MOVIE_OTT TABLE", 'REASON', f)
        pass 



def insert_values_show_ott():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        cur.execute("INSERT INTO Show_OTT VALUES('S01','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S02','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S03','OTT02')")
        cur.execute("INSERT INTO Show_OTT VALUES('S04','OTT02')")
        cur.execute("INSERT INTO Show_OTT VALUES('S05','OTT05')")
        cur.execute("INSERT INTO Show_OTT VALUES('S06','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S07','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S08','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S09','OTT03')")
        cur.execute("INSERT INTO Show_OTT VALUES('S10','OTT03')")
        cur.execute("INSERT INTO Show_OTT VALUES('S11','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S12','OTT03')")
        cur.execute("INSERT INTO Show_OTT VALUES('S13','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S14','OTT02')")
        cur.execute("INSERT INTO Show_OTT VALUES('S15','OTT06')")
        cur.execute("INSERT INTO Show_OTT VALUES('S16','OTT06')")
        cur.execute("INSERT INTO Show_OTT VALUES('S17','OTT02')")
        cur.execute("INSERT INTO Show_OTT VALUES('S18','OTT01')")
        cur.execute("INSERT INTO Show_OTT VALUES('S19','OTT04')")
        cur.execute("INSERT INTO Show_OTT VALUES('S20','OTT04')")
        db.commit()
        cur.close()
        db.close()



    except Exception as f:
        print("CANNOT INSERT VALUES IN SHOW_OTT TABLE", 'REASON', f)
        pass 




def insert_values():
    try:
        insert_values_OTT()
        insert_values_shows()
        insert_values_movies()
        insert_subscribers()
        
        insert_values_movie_ott()
        insert_values_show_ott()
        print("values inserted in tables")

    except Exception as f:
        print("CANNOT INSERT VALUES IN TABLES", 'REASON', f)
        pass    



database()
insert_values()  



def display_shows():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                  <<<<<<<<<        DISPLAY ALL SHOWS        >>>>>>>>")
        print("")
        print("")
        
        rows = cur.execute("SELECT * FROM Shows NATURAL JOIN Show_OTT")
        
        print("")
        print("")

        show_table=cur.fetchall()
        print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("||{0:^10}|{1:^40}|{2:^20}|{3:^20}|{4:^20}|{5:^15}|{6:^30}|{7:^10}||".format('SHOW ID','NAME OF THE SHOW','GENRE','NUMBER OF SEASONS','NUMBER OF EPISODES','IMDb RATING','AVAILABLE ON OTT PLATFORM','OTT_ID'))
        print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        for i in show_table:
            print("||{0:^10}|{1:<40}|{2:<20}|{3:^20}|{4:^20}|{5:^15}|{6:<30}|{7:^10}||".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
            print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")

        print("")
        print("")
        ch1=input("\tGO BACK TO MAIN MENU ? (Y/N) : ")
        if ch1.upper()=='Y':
            menu()
        else:
            quit()    

        cur.close()
        db.close()

    except:
        print("error in displaying SHOWS table")        




def display_movies():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                  <<<<<<<<<        DISPLAY ALL MOVIES        >>>>>>>>")
        print("")
        print("")
        rows = cur.execute("SELECT * FROM Movies NATURAL JOIN Movie_OTT")

        print("")
        print("")

        show_table=cur.fetchall()
        print("\t+--------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("\t||{0:^15}|{1:^40}|{2:^25}|{3:^20}|{4:^35}|{5:^10}||".format('MOVIE ID','NAME OF THE MOVIE','GENRE','IMDb RATING','AVAILABLE ON OTT PLATFORM','OTT-ID'))
        print("\t+--------------------------------------------------------------------------------------------------------------------------------------------------------+")
        for i in show_table:
            print("\t||{0:^15}|{1:<40}|{2:<25}|{3:^20}|{4:<35}|{5:^10}||".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            print("\t+--------------------------------------------------------------------------------------------------------------------------------------------------------+")

        print("")
        print("")

        go=input("\t\tGO BACK TO MAIN MENU ? (Y/N) : ")
        if go.upper()=='Y':
            menu()
        else:
            quit()    


        cur.close()
        db.close()

    except:
        print("error in displaying MOVIES table")








def search_sh(chs):
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                        <<<<<<<<<      TO SEARCH SHOW       >>>>>>>>")
        print("")
        print("")
        print("")
        

        if chs==1:
            n=input("\tEnter Name of the Show : ")
            m=n.title()
            q="SELECT * FROM Shows NATURAL JOIN Show_OTT WHERE Name ='{}' ".format(m,)
            
        elif chs==2:
            g=input("\tEnter Genre of the Show : ")
            h=g.title()
            q="SELECT * FROM Shows NATURAL JOIN Show_OTT WHERE Genre ='{}' ".format(h,)

        elif chs==3:
            d=input("\tEnter Show-ID : ")
            q="SELECT * FROM Shows NATURAL JOIN Show_OTT WHERE Show_ID ='{}' ".format(d,)  

        elif chs==4:
            t=int(input("\tEnter IMDb Rating : "))
            q="SELECT * FROM Shows NATURAL JOIN Show_OTT WHERE IMDb_Rating >= {} ".format(t,)

        elif chs==5:
            p=input("\tEnter OTT Platform : ")
            r=p.title()
            q="SELECT * FROM Shows NATURAL JOIN Show_OTT WHERE Platform ='{}' ".format(p,)        

        else:
            menu()        

        print("")
        print("")

        cur.execute(q)

        show_record= cur.fetchall()
        print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("||{0:^10}|{1:^40}|{2:^20}|{3:^20}|{4:^20}|{5:^15}|{6:^30}|{7:^10}||".format('SHOW ID','NAME OF THE SHOW','GENRE','NUMBER OF SEASONS','NUMBER OF EPISODES','IMDb RATING','AVAILABLE ON OTT PLATFORM','OTT-ID'))
        print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        for i in show_record:
            print("||{0:^10}|{1:<40}|{2:<20}|{3:^20}|{4:^20}|{5:^15}|{6:<30}|{7:^10}||".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
            print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")

        print("")
        print("")
        go=input("\tGO BACK TO SUB-MENU ? (Y/N) : ")
        if go.upper()=='Y':
            search_shows()
        else:
            quit()    

        cur.close()
        db.close()

    except Exception as f:
        print("CANNOT SEARCH Show", 'REASON', f)
        pass



def search_shows():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                       <<<<<<<<<        SEARCH SHOWS        >>>>>>>>")
        print("")
        print("")
        print("\t1.  Search by Name")
        print("")
        print("\t2.  Search by Genre")
        print("")
        print("\t3.  Search by Show-ID")
        print("")
        print("\t4.  Search by IMDb rating")
        print("")
        print("\t5.  Search by OTT Platform")
        print("")
        print("\t6.  Back to Main Menu")
        print("")
        print("")
        print("")

        chs = int(input("\t ENTER CHOICE: "))
        print("")
        print("")
        print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("")
        print("")
        print("")

        search_sh(chs)


        cur.close()
        db.close()

    except Exception as f:
        print("error search show menu", 'REASON', f)
        pass    






def search_m(chm):
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()  
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                   <<<<<<<<<        TO SEARCH MOVIE        >>>>>>>>")
        print("")
        print("")
        print("")
        

        if chm==1:
            n=input("\tEnter Name of the Movie: ")
            m=n.title()
            q="SELECT * FROM Movies NATURAL JOIN Movie_OTT WHERE Name ='{}' ".format(m,)

        elif chm==2:
            g=input("\tEnter Genre of the Movie : ")
            h=g.title()
            q="SELECT * FROM Movies NATURAL JOIN Movie_OTT WHERE Genre ='{}' ".format(h,)

        elif chm==3:
            d=input("\tEnter Movie-ID : ")
            q="SELECT * FROM Movies NATURAL JOIN Movie_OTT WHERE Movie_ID ='{}' ".format(d,)  

        elif chm==4:
            t=int(input("\tEnter IMDb Rating : "))
            q="SELECT * FROM Movies NATURAL JOIN Movie_OTT WHERE IMDb_Rating >={} ".format(t,)      

        elif chm==5:
            p=input("\tEnter OTT Platform : ")
            r=p.title()
            q="SELECT * FROM Movies NATURAL JOIN Movie_OTT WHERE Platform ='{}' ".format(p,)  

        else:
            menu()

        print("")
        print("")


        cur.execute(q)

        
        show_record= cur.fetchall()
        print("\t+-------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("\t||{0:^15}|{1:^40}|{2:^25}|{3:^20}|{4:^35}|{5:^15}||".format('MOVIE ID','NAME OF THE MOVIE','GENRE','IMDb RATING','AVAILABLE ON OTT PLATFORM','OTT-ID'))
        print("\t+-------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        for i in show_record:
            print("\t||{0:^15}|{1:<40}|{2:<25}|{3:^20}|{4:<35}|{5:^15}||".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            print("\t+-------------------------------------------------------------------------------------------------------------------------------------------------------------+")

        print("")
        print("")
        go=input("\tGO BACK TO SUB-MENU ? (Y/N) : ")
        if go.upper()=='Y':
            search_movies()
        else:
            quit()    

        cur.close()
        db.close()

    except Exception as f:
        print("CANNOT SEARCH MOVIES", 'REASON', f)
        pass





def search_movies():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                 <<<<<<<<<        SEARCH MOVIES        >>>>>>>>")
        print("")
        print("")
        print("\t1.  Search by Name")
        print("")
        print("\t2.  Search by Genre")
        print("")
        print("\t3.  Search by Movie-ID")
        print("")
        print("\t4.  Search by IMDb rating")
        print("")
        print("\t5.  Search by OTT Platform")
        print("")
        print("\t6.  Back to Main Menu")
        print("")
        print("")
        print("")

        chm = int(input("\t ENTER CHOICE: "))
        print("")
        print("")
        print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("")
        print("")
        print("")



        search_m(chm)

        cur.close()
        db.close()


    except Exception as f:
        print("error serach movie menu", 'REASON', f)
        pass    



def delete_acc(c):
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        q="DELETE FROM Subscriber WHERE Subscriber_ID={}".format(c,)
        cur.execute(q)
        db.commit()
        cur.close()
        db.close()
        print("")
        print("")
        print("\tSUCCESSFULLY DELETED.")
        print("")
        print("")
        print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        go=input("\tGO BACK TO SUB-MENU ? (Y/N) : ")
        if go.upper()=='Y':
            acc_menu()
        else:
            quit()    

    except Exception as f:
        print("error deleting subscriber details", 'REASON', f)
        pass  




def add_acc():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        n=input("\tEnter Name : ")
        name=n.title()
        print("")
        phone=input("\tEnter Phone number : ")
        print("")
        no=int(input("\tEnter number of subscribed OTT platforms : "))
        q="INSERT INTO Subscriber(Name,Phone_Number,No_Of_Subscribed_OTT_Platforms) VALUES('{}','{}',{})".format(name,phone,no)
        cur.execute(q)
        db.commit()
        cur.close()
        db.close()
        print("")
        print("")
        print("\tSUCCESSFULLY ADDED.")
        print("")
        print("")
        go=input("\tGO BACK TO SUB-MENU ? (Y/N) : ")
        if go.upper()=='Y':
            acc_menu()
        else:
            quit()    

        

    except Exception as f:
        print("error in adding new account ", 'REASON', f)
        pass  

    




def display_details(c):
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print("")
        q="SELECT * FROM Subscriber WHERE Subscriber_ID={} ".format(c,)
        cur.execute(q)

        print("")
        print("")

        show_record=cur.fetchall()
        print("\t\t+-----------------------------------------------------------------------------------------------------------------------------+")
        print("\t\t||{0:^20}|{1:^40}|{2:^25}|{3:^35}||".format('SUBSCRIBER ID','NAME','PHONE NUMBER','NUMBER OF SUBSCRIBED PLATFORMS'))
        print("\t\t+-----------------------------------------------------------------------------------------------------------------------------+")
        for i in show_record:
            print("\t\t||{0:^20}|{1:<40}|{2:<25}|{3:^35}||".format(i[0],i[1],i[2],i[3]))
            print("\t\t+-----------------------------------------------------------------------------------------------------------------------------+")

        print("")
        print("")

        go=input("\tGO BACK TO SUB-MENU ? (Y/N) : ")
        if go.upper()=='Y':
            acc_menu()
        else:
            quit()    


        cur.close()
        db.close()

    
    except Exception as f:
        print("error in displaying subscriber details", 'REASON', f)
        pass 

    


def update_acc(c):
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        q="SELECT * FROM Subscriber WHERE Subscriber_ID={} ".format(c,)
        print("")
        print("")
        name=input("\tEnter Name : ")
        print("")
        phone=input("\tEnter Phone number : ")
          

        

        cur.execute(q)
        r=cur.fetchone()
        n=name.title()
        p=phone
        sql1="UPDATE Subscriber SET Name ='{}' WHERE Subscriber_ID ={}".format(n,c)
        sql2="UPDATE Subscriber SET Phone_Number ='{}' WHERE Subscriber_ID ={}".format(p,c)
        cur.execute(sql1)
        cur.execute(sql2)

        print("")
        new=input("\tSubscribed New OTT Platform (Y/N) : ")
        if new.upper()=='Y':
            sql="UPDATE Subscriber SET No_Of_Subscribed_OTT_Platforms ={} WHERE Subscriber_ID ={}".format((r[3]+1),c)
            cur.execute(sql)


        print("")
        d=input("\tDeleted Subscription (Y/N) : ")
        if d.upper()=='Y':
            sql="UPDATE Subscriber SET No_Of_Subscribed_OTT_Platforms ={} WHERE Subscriber_ID ={}".format((r[3]-1),c)
            cur.execute(sql)

        db.commit()

        
        print("")
        print("\tSUCCESSFULLY UPDATED.")
        display_details(c)


        acc_menu()

    except Exception as f:
        print("error update subscriber details", 'REASON', f)
        pass  
        

def acc_menu():
    try:
        db = x.connect(host="localhost",user = "root",password = "",db="OTT_DBMS")
        cur = db.cursor()
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                     <<<<<<<<<       ACCOUNT DETAILS       >>>>>>>>")
        print("")
        print("")
        print("")
        print("")
        print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("")
        print("")
        print("\t1.  Show My Details")
        print("")
        print("\t2.  Create new account")
        print("")
        print("\t3.  Delete account")
        print("")
        print("\t4.  Update profile")
        print("")
        print("\t5.  Back to Main Menu")
        print("")
        print("")
        print("")

        chsub = int(input("\t ENTER CHOICE: "))
        print("")
        print("")
        print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("")
        print("")
        print("")

        if chsub==1:
            c=int(input("\tEnter Subscriber-ID : "))
            display_details(c)

        if chsub==2:
            add_acc()  

        if chsub==3:
            c=int(input("\tEnter Subscriber-ID : "))
            delete_acc(c)

        elif chsub==4:
            c=int(input("\tEnter Subscriber-ID : "))
            update_acc(c)

        else:
            menu()              

        cur.close()
        db.close()


    except Exception as f:
        print("error account details menu", 'REASON', f)
        pass    


def menu():
    try:
        print("")
        print("_________________________________________________________________________________________________________________________________________________________________________________________")
        print("")
        print("                                                                                       StreamSage")
        print("                                                                      For a perfect viewing experience every time.")
        print("")
        print("_________________________________________________________________________________________________________________________________________________________________________________________")
        print("")
        print("")
        print(z.ctime())
        print("")
        print("")
        print("")
        print("                                                                        <<<<<<<<<         MENU         >>>>>>>>")
        print("")
        print("")
        print("\t1.  Display All Shows")
        print("")
        print("\t2.  Display All Movies")
        print("")
        print("\t3.  Search Web-series")
        print("")
        print("\t4.  Search Movies")
        print("")
        print("\t5.  Show Account Details")
        print("")
        print("\t6.  EXIT")
        print("")
        print("")

        ch = int(input("\t ENTER CHOICE: "))
        print("")
        print("")
        print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
        print("")
        print("")
        print("")

        if ch == 1:
            display_shows()

        elif ch == 2:
            display_movies()

        elif ch == 3:
            search_shows()        

        elif ch == 4:
            search_movies()

        elif ch == 5:
            acc_menu()

        else:
            quit()

        
    except:
        print("ERROR MENU")






menu()
