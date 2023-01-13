from abc import ABC, abstractmethod

class User:
    def __init__(self) -> None:
        self.fn = None
        self.ln = None
        self.age = None
        self.phone_numbers = None
        self.add = []
        
class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass
    
    @abstractmethod
    def add_fn(self, firstname): pass
    
    @abstractmethod
    def add_ls(self, lastname): pass
    
    @abstractmethod
    def add_age(self, age): pass
    
    @abstractmethod
    def add_phone(self, phone): pass
    
    @abstractmethod
    def add_address(self, address): pass
    
        
class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._result = User()
    
    @property
    def result(self): 
        return_data = self._result
        self.reset()
        return return_data
    
    def add_fn(self, firstname): 
        self._result.fn = firstname
    
    def add_ls(self, lastname):
        self._result.ln = lastname
    
    
    def add_age(self, age): 
        self._result.age = age
    
    def add_phone(self, phone): 
        self._result.phone_numbers.append(phone)
    
    def add_address(self, address): 
        self._result.add.append(address)
        
        
