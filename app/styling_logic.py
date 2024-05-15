



# COLORS:
light_cyan = "#66FCF1"
dark_cyan = "#45A29E"
red_saturated = "#FF0000"
silver = "#C5C6C7"
dark_gray = "#0B0C10"


def load_stylesheet(filename):
    with open(filename, "r") as f:
        return f.read()
    
stylesheet = load_stylesheet("stles/styles.css")



