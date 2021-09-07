


from Prac_06.Programming_language import Programming_language

def main():
    ruby = Programming_language("Ruby", "Dynamic", True, 1995)
    python = Programming_language("Python", "Dynamic", True, 1991)
    visual_basic = Programming_language("Visual Basic", "Static", False, 1991)

    languages = [ruby,python,visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

            