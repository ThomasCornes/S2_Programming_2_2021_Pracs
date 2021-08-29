COLOUR_CODES = {"Indianred": "#CD5C5C", "Crimson": "#DC143C",
                "DeepPink": "#551493", "Hotpink": "#ff69B4",
                "Tomato": "#FF6347", "Orange": "#FFA500",
                "Khaki": "#F0E68cC", "Moccasin": "#FFE4B5",
                "Thistle": "#E6E6FA", "Orchid": "#DA70D6",
                "Magenta": "#FF00FF", "SlateBlue": "#483D8B", "Lime": "00FF00",
                "SpringGreen": "#00FF7F", "Olive": "#556B2F"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    # Note: using the get dictionary method
    # means you will get None if the key is not found
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")