p1 = "Haikus are easy.\nBut sometimes they don't make sense.\nRefrigerator."
p2 = "I think haikus suck.\nHas to be five seven five.\nWho came up with this?"
p3 = "Five syllables here.\nSeven more syllables here.\nAre you happy now?"

class Poem:
    obj_count = 0
    def __init__(self, title, author, haiku_variable):
        Poem.obj_count += 1
        self.title = title
        self.author = author
        self.haiku_variable = haiku_variable

    def print_text(self):
        return self.haiku_variable

    def setHaiku(self):
        if len(self.haiku_variable) >= 1:
            return True

haiku_1 = Poem("Haiku 1", "unknown", p1)
haiku_2 = Poem("Haiku 2", "unknown", p2) # Random haikus found online
haiku_3 = Poem("Haiku 3", "unknown", p3) # No title or authors found

print("The number of Poems created: ", str(Poem.obj_count), "\n")
print(haiku_1.print_text())
print("Is it a Haiku?: ", haiku_1.setHaiku(), "\n")
print(haiku_2.print_text())
print("Is it a Haiku?: ", haiku_2.setHaiku(), "\n")
print(haiku_3.print_text())
print("Is it a Haiku?: ", haiku_3.setHaiku(), "\n")






