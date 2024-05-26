import tkinter as tk
import colours as c
import random
 class game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(self, bg= c.Color_grid, bd = 3 , width=600, 
height = 400)
        self.main_grid.grid(pady=(150,1))
        self.make_GUI()
        self.start_game()
        self.master.bind("<Left>",self.left)
        self.master.bind("<Right>",self.right)
        self.master.bind("<Up>",self.up)
        self.master.bind("<Down>",self.down)
        self.mainloop()
    def make_GUI(self):
        #making the grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(self.main_grid, bg = c.Color_EmptyCell, 
width= 150,height=150)
                cell_frame.grid(row=i,column=j,padx= 5,pady= 5)
                cell_number = tk.Label(self.main_grid, bg=c.Color_EmptyCell)
                cell_number.grid(row =i, column=j)
                cell_data = {"frame": cell_frame, "number":cell_number}
                row.append(cell_data)
            self.cells.append(row)
        #Score header
        score_frame = tk.Frame(self)
        score_frame.place(relx= 0.5, y = 55, anchor="center")
        tk.Label(score_frame, text = "Score", font= c.Font_ScoreLabel).grid(row = 
0)
 # game()
        self.score_label = tk.Label(score_frame, text = "0", font= c.Font_Score)
        self.score_label.grid(row= 1)
    def start_game(self):
        #creating matrix of zeros
        self.matrix = [[0]*4 for _ in range(4)]
        #fill any 2 random cells with 2s
        row = random.randint(0,3)
        col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg= c.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg = c.Color_Cells[2],
            fg=c.Color_CellNumber[2],
            font = c.Fonts_CellNumebr[2],
            text = "2"
        )
        while(self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg= c.Color_Cells[2])
        self.cells[row][col]["number"].configure(bg = 
c.Color_Cells[2],fg=c.Color_CellNumber[2],font = c.Fonts_CellNumebr[2],text = "2")
        self.score = 0
        #matrix manuipulation
    def stack(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range (4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix
    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i]
 [j+1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] =0
                    self.score += self.matrix[i][j] ########score update
    def reverse(self):
        new_matrix = []
        for i in range (4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix = new_matrix
    def transpose(self):
        new_matrix = [[0]*4 for _ in range(4)] #
        for i in range (4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix
    # adding a new tile randomly
    def add_new_tile(self):
        row = random.randint(0,3)
        col = random.randint(0,3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = random.choice([2])
 #updating the GUI with all the changes
    def update_GUI(self):
        for i in range (4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg= c.Color_EmptyCell)
                    self.cells[i][j]["number"].configure(bg= c.Color_EmptyCell,text
 = "")
                else:
                    self.cells[i][j]["frame"].configure(bg= 
c.Color_Cells[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg= c.Color_Cells[cell_value],
                        fg = c.Color_CellNumber[cell_value],
                        font =c.Fonts_CellNumebr[cell_value],
                        text = str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()
 # arrow functions
    def left (self,event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()
    def right (self,event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()
    def up (self,event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()
    def down (self,event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()
 #Game OVERRR
    def horizontal_move_exists(self):
        for i in range (4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False
    def verticle_move_exists(self):
        for i in range (3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth = 2)
            game_over_frame.place(relx = 0.5, rely = 0.5, anchor= "center")
            tk.Label(game_over_frame,text = "YOU WIN",bg = c.Winner_BG,fg = 
c.Font_Color_GameOver,font = c.Font_GameOver).pack()
        elif not any(0 in row for row in self.matrix) and not 
self.horizontal_move_exists() and not self.verticle_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwigth = 2)
            game_over_frame.place (relx = 0.5, rely = 0.5, anchor= "center")
            tk.Label(game_over_frame,text = "Game Over TT",bg = c.Loser_BG,fg = 
c.Font_Color_GameOver,font = c.Font_GameOver).pack()
        else:
            if self.horizontal_move_exists() or self.verticle_move_exists():
                pass
 def main():
    game()
 if __name__ == '__main__':
    main()

