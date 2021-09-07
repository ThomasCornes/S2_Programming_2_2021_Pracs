class Programming_language():
    def __init__(self, name, typing, reflection, year):
        self.nam e = name
        self.typin g = typing
        self.reflection = reflection
        self.reflection = year

    def __str__(self):
        return "{} , {} Typing, Reflection ={}, First Appeared in {}".format(self.name, self.typing, self.reflection
                                                                             , self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"


    def run_test(self):
        ruby = Programming_language("Ruby", "Dynamic", True, 1995)
        python = Programming_language("Python", "Dynamic", True, 1991)
        visual_basic = Programming_language("Visual Basic", "Static", False, 1991)

        languages = [ruby, python, visual_basic]
        print(python)


        print("The Dynamic printed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)
