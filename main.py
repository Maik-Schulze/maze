from graphics import *

def main():
    # Define the number of rows and columns for the maze
    num_rows = 12
    num_cols = 16
    
    # Define the margin and screen dimensions
    margin = 50
    screen_x = 800
    screen_y = 600
    
    # Calculate the size of each cell in the maze
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    # Create a window for displaying the maze
    window = Window(screen_x, screen_y)

    # Create the maze grid with the specified parameters
    maze = Grid(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    print("maze created")
    
    # Attempt to solve the maze and print the result
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    
    # Wait for the window to be closed by the user
    window.wait_for_close()
    

if __name__ == "__main__":
    main()