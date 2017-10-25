# Base Class of a game Unit
class Unit:
    def __init__(self, name):
        self.Name = name
        self.HitPoints = 1
        self.Strength = 1
        self.Agility = 1
        self.Intelligence = 1
        self.Charisma = 1
        self.Alignment = 1
        self.Luk = 1
        # Requirements: Base Unit
        self.Size = ""
        self.Terrain = ""
        # Leader      : No
        # Recruit     : None
        # Front Row   : 2 Slices (P)
        # Back Row    : 1 Slice (P)
        # Hit Points  : 5-7 per Level Up
        # Strength    : 2-4 per Level Up
        # Agility     : 2-4 per Level Up
        # Intelligence: 1-3 per Level Up
        self.Physical = 1
        self.Fire = 1
        self.Cold = 1
        self.Thunder = 1
        self.Black = 1
        self.White = 1
        # Deployment  : 80 + (20 X level)



class Fighter(Unit):
    def __init__(self, name):
        self.Name = name
        self.HitPoints = 77
        self.Strength = 45
        self.Agility = 47
        self.Intelligence = 40
        self.Charisma = 46
        self.Alignment = 50
        self.Luk = 48
        # Requirements: Base Unit
        self.Size = "Small"
        self.Terrain = "Plains"
        # Leader      : No
        # Recruit     : None
        # Front Row   : 2 Slices (P)
        # Back Row    : 1 Slice (P)
        # Hit Points  : 5-7 per Level Up
        # Strength    : 2-4 per Level Up
        # Agility     : 2-4 per Level Up
        # Intelligence: 1-3 per Level Up
        self.Physical = 44
        self.Fire = 36
        self.Cold = 40
        self.Thunder = 34
        self.Black = 40
        self.White = 40
        # Deployment  : 80 + (20 X level)


class Amazon(Unit):
    def __init__(self, name):
        self.Name = name
        self.HitPoints = 83
        self.Strength = 42
        self.Agility = 50
        self.Intelligence = 52
        self.Charisma = 46
        self.Alignment = 50
        self.Luk = 48
        # Requirements: Base Unit
        self.Size = "Small"
        self.Terrain = "Forest"
        # Leader      : No
        # Recruit     : None
        # Front Row   : 2 Slices (P)
        # Back Row    : 1 Slice (P)
        # Hit Points  : 5-7 per Level Up
        # Strength    : 2-4 per Level Up
        # Agility     : 2-4 per Level Up
        # Intelligence: 1-3 per Level Up
        self.Physical = 38
        self.Fire = 32
        self.Cold = 36
        self.Thunder = 43
        self.Black = 38
        self.White = 42
        # Deployment  : 80 + (20 X level)



Unit1 = Fighter("Lancelot")
Unit2 = Amazon("Lancelotte")

print Unit1.Name
print Unit1.Strength
print Unit2.Name
print Unit2.Strength
