# Maze Solver

This project is a simple maze solver implemented in Python. It uses a graphical interface to display the maze and its solution.

## Features

- Generates a random maze
- Solves the maze using depth-first search
- Displays the maze and the solution graphically

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Maik-Schulze/maze.git
    cd maze
    ```

2. Ensure you have the Tkinter installed:
    ```sh
    sudo apt-get install python3-tk
    ```

## Usage

Run the main script to generate and solve a maze:
```sh
python main.py
```

## Project Structure

- `main.py`: The main script to run the maze solver.
- `graphics.py`: Contains the classes for graphical representation.
- `test_graphics.py`: Unit tests for the graphical components.

## Running Tests

To run the unit tests, use:
```sh
python -m unittest discover
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.