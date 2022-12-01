from tkinter import *
from cell import Cell
import settings
import utilities


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utilities.height_percentage(10)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper Game",
    font=("", 48)
)
game_title.place(
    x=utilities.width_percentage(0), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=200,
    height=utilities.height_percentage(90)
)
left_frame.place(x=0, y=72)

center_frame = Frame(
    root,
    bg='black',
    width=utilities.width_percentage(75),
    height=utilities.height_percentage(90)
)
center_frame.place(
    x=utilities.width_percentage(28),
    y=utilities.height_percentage(10),
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

# Run the window
root.mainloop()
