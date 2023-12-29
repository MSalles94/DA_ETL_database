class query_sql():
    def __init__(self) -> None:
        self.DB_path='./comercial_database.db'
        import pandas
        self.pandas=pandas

    def __connect(self):
        import sqlite3
        self.conn=sqlite3.connect(self.DB_path)
        self.cursor=self.conn.cursor()
        print('-connected')

    def __disconnect(self):
        self.conn.close()
        print('-disconected')
    
    def clients(self):
        self.__connect()
        command=f""" SELECT * FROM CLIENTS"""
        self.cursor.execute(command)
        answer=self.pandas.read_sql_query(command,self.conn)
        self.__disconnect()
        return answer
    
    def order(self,dt_i='',dt_f=''):

        #create the "WHERE" command
        filter=[]
        if dt_i=='' and dt_f=='':
            pass
        else:
            if dt_i!='':
                filter.append(f'ORDER_DATE >= {dt_i}')
                pass
            if dt_f!='':
                filter.append(f'ORDER_DATE <= {dt_f}')
        comand_filter=''
        if filter!=[]:
            comand_filter='\n WHERE '+filter[0]
            for i in filter[1:]:
                comand_filter=comand_filter+' AND '+i

        #build the comand
        command = """SELECT * 
             FROM ORDER_MAIN AS M
             LEFT JOIN ORDER_ITEM AS I
             ON I.order_n = M.ORDER_NUMBER
             LEFT JOIN PRODUCTS AS P
             ON P.ID_PRODUCTS = I.ID_products
          """+comand_filter
        
        #Execute        
        self.__connect()
        answer=self.pandas.read_sql_query(command,self.conn)
        self.__disconnect()
        return answer


