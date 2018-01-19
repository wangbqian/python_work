class ImmutableDict(dict):
    """docstring for ImmutableDict"""
    # def __init__(self, Connection,Host):
    #     self.Connection = Connection
    #     self.Host = Host
    def __setitem__(self,key,value):
        raise TypeError("'ImmutableDict' objects are immuabletable")

    def __delitem__(self,key):
        raise TypeError("'ImmutableDict' objects are immuabletable")

    def popitem(self,key):
        raise TypeError("'ImmutableDict' objects are immuabletable")

    def pop(self,key):
        raise TypeError("'ImmutableDict' objects are immuabletable")

    def setdefault(self,key):
        raise TypeError("'ImmutableDict' objects are immuabletable")

    def clear(self):
        raise TypeError("'ImmutableDict' objects are immuabletable")
    def updata(self):
        raise TypeError("'ImmutableDict' objects are immuabletable")
        
    

d = ImmutableDict(Connection='kee-alive', Host='www.shiyanlou.com')
print(d)
# d['Host'] = 'ss'
print(d.get('Host'))
