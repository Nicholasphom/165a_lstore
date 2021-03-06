from table import Table

"""
# optional: Indexes the specified column of the specified table to speed up select queries
# This data structure is usually a B-Tree
"""


class Index:

    def __init__(self, table):
        self.table = table
        self.idx = {}
        pass

    """
    # returns the location of all records with the given value
    """

    def locate(self, value): 
        try:
            return self.idx[value]
        except KeyError:
            return []
            pass
        pass

    """
    # optional: Create index on specific column
    """

    def create_index(self, column_number):
        if column_number >= self.table.num_columns:
            print('error: cannot create index on column that does not exist')
        for rid in self.table.page_directory:
            # obtain page-related information for given rid:
            rid_tuple = self.table.page_directory[rid]
            # obtain id of page containing key value
            page_id = rid_tuple[0] + column_number
            # obtain page containing key value
            page = self.table.pages[self.table.page_index[page_id]]
            # read key value from page
            key_value = page.read(rid_tuple[2])
            if key_value in self.idx.keys() and rid not in self.idx[key_value]:
                self.idx[key_value].append(rid)
            else:
                self.idx[key_value] = [rid]
        pass

    """
    # optional: Drop index of specific column
    """

    def update_index(self, rid, column_number):
        rid_tuple = self.table.page_directory[rid]
        page_id = rid_tuple[0] + column_number
        page = self.table.pages[self.table.page_index[page_id]]
        key_value = page.read(rid_tuple[2])
        try:
            if rid not in self.idx[key_value]:
                self.idx[key_value].append(rid)
        except KeyError:
            self.idx[key_value] = [rid]



    def drop_index(self, table, column_number):
        pass

    def print_index(self):
        print(self.idx)
