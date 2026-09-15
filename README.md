# Nim-game-# Nim Game AI – Game Search

## 1. Project Title

**Nim Game AI – Optimal Game-Playing Using Nim-Sum Theory**

## 2. Problem Statement

To develop an Artificial Intelligence system that plays the game of Nim optimally by analyzing pile configurations, identifying winning positions, and selecting the best possible move using Nim-sum theory.

## 3. Objectives

- To understand the rules and mathematical theory of Nim.
- To develop an AI that plays Nim optimally.
- To calculate the Nim-sum using the XOR operation.
- To identify winning and losing positions.
- To select an optimal move from every winning position.
- To demonstrate the application of game theory in Artificial Intelligence.

## 4. Technologies Used

- **Programming Language:** Python
- **Artificial Intelligence Concept:** Game Search
- **Algorithm:** Nim-Sum Strategy
- **Development Platform:** GitHub
- **Testing:** Python Test Cases

## 5. Dataset

This project does not require an external dataset.

The input consists of the number of objects present in each pile. Different pile configurations are used as sample inputs to test the AI's decision-making ability.

**Example Input:**
```text
Piles = [3, 4, 5]
```

## 6. Methodology

The AI follows these steps:

1. Accepts the pile sizes as input.
2. Calculates the Nim-sum using the XOR operation.
3. Checks whether the Nim-sum is zero.
4. If the Nim-sum is non-zero, searches for a move that makes the Nim-sum zero.
5. Selects the optimal move.
6. Displays the AI's decision.

According to Nim game theory:

- **Nim-sum = 0:** Losing position under perfect play.
- **Nim-sum ≠ 0:** Winning position.

## 7. System Architecture

```text
+----------------------+
|   Input Pile Sizes   |
+----------+-----------+
           |
           v
+----------------------+
|  Calculate Nim-Sum   |
|     Using XOR        |
+----------+-----------+
           |
           v
+----------------------+
| Check Game Position  |
+----------+-----------+
           |
     +-----+-----+
     |           |
     v           v
 Nim-sum = 0  Nim-sum ≠ 0
     |           |
     v           v
 Losing       Find Optimal
 Position        Move
                 |
                 v
          Display AI Move
```

## 8. Implementation

The project is implemented using Python.

The `nim_sum()` function calculates the XOR of all pile sizes. The `find_best_move()` function identifies a move that makes the Nim-sum zero whenever a winning move exists.

### Main Functions

- `nim_sum(piles)` – Calculates the Nim-sum.
- `find_best_move(piles)` – Finds the optimal move.
- `main()` – Executes the program and displays the result.

## 9. Results

The AI successfully calculates the Nim-sum and identifies winning and losing positions.

For winning positions, the AI selects a move that makes the Nim-sum zero, demonstrating an optimal strategy for normal-play Nim.

**Sample Result:**

```text
Welcome to Nim Game AI
Initial piles: [3, 4, 5]
Nim-sum: 2
AI removes 2 objects from pile 1
Optimal move found!
```

## 10. Screenshots

Screenshots of the following will be included in the project documentation:

- Python source code
- Program execution
- Sample output
- GitHub repository
- Test results

## 11. How to Run

### Prerequisites

- Python 3.x
- GitHub account (for accessing the repository)

### Steps

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python main.py
```

### Expected Output

```text
Welcome to Nim Game AI
Initial piles: [3, 4, 5]
Nim-sum: 2
AI removes 2 objects from pile 1
Optimal move found!
```

## 12. Future Enhancement

- Develop a graphical user interface.
- Add human-versus-AI gameplay.
- Implement Minimax for comparison.
- Add difficulty levels.
- Add more automated test cases.
- Visualize the piles and AI decisions.

## 13. Team Members

| S.No | Name | Role |
|------|------|------|
| 1 | Pavithra | Project Development |
| 2 | __________ | __________ |
| 3 | __________ | __________ |
| 4 | __________ | __________ |

*Update the team member details according to your actual team.*

## 14. References

1. C. L. Bouton, "Nim, A Game with a Complete Mathematical Theory," Annals of Mathematics, 1901.
2. Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*.
3. Python Documentation – Bitwise XOR Operator.
4. GitHub Documentation – Repositories and Version Control.
