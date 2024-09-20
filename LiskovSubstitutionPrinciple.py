class Bird:
    def fly(self):
        return "Flying"

# Subclass that adheres to LSP
class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

def let_bird_fly(bird: Bird):
    print(bird.fly())

# This works for Sparrow
sparrow = Sparrow()
let_bird_fly(sparrow)  # Output: Sparrow is flying

# But violates LSP for Penguin, since Penguin cannot fly
penguin = Penguin()
let_bird_fly(penguin)  # This will raise NotImplementedError
