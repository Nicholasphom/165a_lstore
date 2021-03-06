from template.table import Table

class RIDspace():

    def __init__(self):
        self.rid_block = (1,512)

    def assign_space(self):
        assigned_block = self.rid_block
        new_block = ((self.rid_block[0]+512),(self.rid_block[1]+512))
        self.rid_block = new_block
        return self.assigned_block

class Database():

    def __init__(self):
        self.tables = []
        rid_space = RIDspace() 
        pass

    def open(self):
        pass

    def close(self):
        pass

    """
    # Creates a new table
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def create_table(self, name, num_columns, key):
        table = Table(name, num_columns, key, rid_space)
        tables.append(table)
        return table

    """
    # Deletes the specified table
    """
    def drop_table(self, name):
        pass
