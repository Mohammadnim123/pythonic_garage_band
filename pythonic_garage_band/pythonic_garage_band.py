from abc import abstractmethod, ABC


class Band():
    member_list = []
    band_list = []

    def __init__(self,name):
        self.name=name
        Band.band_list.append(self)

    def add_members(self,member_name):
        self.member_name=member_name
        Band.member_list.append(self.member_name)

    def play_solos(self):
        result =''
        for i in Band.member_list:
            result+= f'{i.play_solos()}\n'
        return result
    
    @classmethod
    def to_list(cls):
        return cls.member_list

    def __repr__(self):
        return f"please dont write {self.name} like this use print to see more details"
    
    def __str__(self):
        return f"welcome in  {self.name} band which consest of {Band.member_list}"




class Musician():
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def __str__(self):
        return f"Musician <{self.name}>"

    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "

    def play_solo(self):
        return f'Musician {self.name} Play solo'




class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"welcome Guitarist {self.name}"

    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self):
        return 'Guitar'



class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"welcome Bassist {self.name}"

    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self):
        return 'Bas'



class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"welcome Drummer {self.name}"

    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self):
        return 'Drum'



if __name__ == "__main__":
#   mohammad = Drummer('mohammad')
#   print(mohammad.name)
  nemrawi = Band('nemrawi')
#   ali = Band('ali')
  nemrawi.add_members('jafar')
  nemrawi.add_members('9ob7y')
  print(nemrawi.__repr__())
  print(nemrawi)
#   print(Band.band_list)
#   abo_anwar = Musician('abo_anwar')
#   print(abo_anwar.play_solo())
#   shareef = Guitarist('shareef')
#   print(shareef)
#   print(nemrawi.play_solos())
  
  

