
class Tic_Tac_Toe():

    def __init__(self, state):
        self.cells = list(state)
        self.cell_dict = {(1,3):"_", (2,3):"_", (3,3):"_", (1,2):"_", (2,2):"_", (3,2):"_", (1,1):"_", (2,1):"_", (3,1):"_"}
        self.all_lines = []
        
    def fill_cell_dict(self):
        for key, value in self.cell_dict:
            self.cell_dict = dict(zip(self.cell_dict.keys(), self.cells))
        return self.cell_dict

    def display(self):
        i = 0
        self.fill_cell_dict()
        print("---------")
        for i in range(0, 8, 3):
            print(f"| {self.cells[i]} {self.cells[i + 1]} {self.cells[i + 2]} |")
        print("---------")       

    def whos_turn(self):
        if self.cells.count("X") > self.cells.count("O"):
            return "O"
        else:
            return "X"

    def add_entry_result(self):
        j = 0
        self.new_entry = (0, 0)
        mark = self.whos_turn()
        try:
            self.new_entry = tuple(int(x.strip()) for x in input("Enter the coordinates: > ").split(' '))
            x, y = [*self.new_entry]
            if self.new_entry in self.cell_dict.keys():
                if self.cell_dict[self.new_entry] == "_":
                    self.cell_dict[self.new_entry] = mark
                    for j, x in enumerate(self.cell_dict.values()):
                        self.cells[j] = x
                    return self.cells
                else:
                    print("This cell is occupied! Choose another one!")
                    self.add_entry_result()
            elif 1 > int(x) or int(x) > 3 or 1 > int(y) or int(y) > 3:
                print("Coordinates should be from 1 to 3!")
                self.add_entry_result()
            else:
                print("You should enter numbers!")
                self.add_entry_result()
        except ValueError:
            if self.new_entry[0] > 3 and len(self.new_entry) < 2:
                print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
            self.add_entry_result()      

    def get_win_lines(self):
        self.all_lines = self.all_entries = []
        self.all_entries = [x for x in self.cells]
        self.rows = [self.cells[:3],self.cells[3:6],self.cells[6:9]]
        self.columns = [self.cells[0:9:3],self.cells[1:9:3],self.cells[2:9:3]]
        self.diagonals = [self.cells[0:9:4]] + [self.cells[2:7:2]]
        self.all_lines = self.rows + self.columns + self.diagonals
        return self.all_lines
        

    def play_result(self):
        if self.all_lines.count(["X", "X", "X"]) == 1 and self.all_lines.count(["O", "O", "O"]) == 1:
            print("Impossible")
            return True
        if self.all_lines.count(["X", "X", "X"]) == 1:
            print("X wins")
            return True
        elif self.all_lines.count(["O", "O", "O"]) == 1:
            print("O wins")
            return True
        elif self.all_entries.count("X") != self.all_entries.count("O"):
            if self.all_entries.count("_") == 0:
                print("Draw")
                return True
            else:
                print("Game not finished")
                return True
        else:
            print("Draw")
            return True

    def play_ttt(self):
        continue_play = True
        self.display()
        while continue_play: #self.add_entry():
            self.add_entry_result()
            self.display()
            self.get_win_lines()
            if ["X", "X", "X"] in self.all_lines or ["O", "O", "O"] in self.all_lines or "_" not in self.cells:
                continue_play = False
                self.play_result()

game = Tic_Tac_Toe("_________")#input("Enter cells: "))
game.play_ttt()
