import random
import turtle as Display

"""
Favorite rules
10011010 uses ["1" if i == int(Cell_length//2) else "0" for i in range(Cell_length)]
10011001
11000011
"""
rule = "01010011"
rule_conditions = ["111","110","101","100","011","010","001","000"]
Cell_size = 4
Cell_length = 241
Cell_row = ["1" if i == int(Cell_length//2) else "0" for i in range(Cell_length)]
#Cell_row = [str(random.randint(0,1)) for i in range(Cell_length)]
Cell_y = 400

def ApplyRules(Cells : list,rule : int) -> list[str]:

    New_cells = Cells.copy()
    
    for cell in range(1,Cell_length-1) :
        neighbors = "".join(Cells[cell - 1 : cell + 2])

        for index in range(8) :
            if neighbors == rule_conditions[index] :
                New_cells[cell] = rule[index]


    return New_cells

def UpdateDisplay(Drawer : Display, Update_cells : list ,start_y : int) -> None:
    
    for num in range(Cell_length) :
        
        Drawer.penup()
        Drawer.setpos(((num * Cell_size) - ((int(Cell_length//2) * Cell_size) + int(Cell_size//2)),start_y))
        Drawer.pendown()

        Drawer.begin_fill()
        Drawer.fillcolor("black")

        if Update_cells[num] == "1" :
            for _ in range(4) :
                Drawer.forward(Cell_size)
                Drawer.right(90)

        Drawer.end_fill()

while True :
    Display.title("Cellular Automata")
    Display.tracer(False)
    Display.hideturtle()

    UpdateDisplay(Display,Cell_row,Cell_y)
    Cell_row = ApplyRules(Cell_row,rule)
    Cell_y -= Cell_size
    Display.update()


