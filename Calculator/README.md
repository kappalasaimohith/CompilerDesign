# Calculator Lexer and Parser

This project includes a simple lexer and parser for arithmetic expressions using the `sly` library in Python. The lexer tokenizes arithmetic expressions, while the parser evaluates them based on defined rules.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. This project requires the `sly` library, which can be installed using `pip`.

### Installation

1. **Clone the Repository**

   Clone the repository to your local machine:
   ```sh
   git clone https://github.com/kappalasaimohith/CompilerDesign.git
   cd CompilerDesign/Calculator
   ```

2. **Install Dependencies**

   Install the required Python package:
   ```sh
   pip install sly
   ```

### Running the Lexer and Parser

You will work with two main files:

- `Lexer1.py`: Defines the lexer to tokenize input expressions.
- `Parser1.py`: Defines the parser to evaluate the tokenized expressions.

#### 1. Create an Input File

Create a file named `input.txt` (or any other name you prefer) with the arithmetic expression you want to evaluate. For example:

```txt
3 + 4 * (2 - 1)
```

#### 2. Run the Lexer and Parser

Use the `Parser1.py` script to parse and evaluate the expression in the input file. You can also choose to display tokens.

**Basic Command**

To parse and evaluate the expression:
```sh
python Parser1.py input.txt
```

**Show Tokens**

To display the tokens and then parse the expression:
```sh
python Parser1.py input.txt -t
```

### Command-Line Arguments

- `-i`: Specifies the input file containing the arithmetic expression.
- `-t` (optional): Shows tokens extracted from the input file.

**Example Usage:**

1. **Without Showing Tokens**
   ```sh
   python Parser1.py input.txt
   ```

2. **With Showing Tokens**
   ```sh
   python Parser1.py input.txt -t
   ```

### Example

1. **Create `input.txt` with the following content:**
   ```
   3 + 4 * (2 - 1)
   ```

2. **Run the script without the `-t` flag:**
   ```sh
   python Parser1.py input.txt
   ```
   Output:
   ```
   Result:
   7
   ```

3. **Run the script with the `-t` flag:**
   ```sh
   python Parser1.py input.txt -t
   ```
   Output:
   ```
   Tokens:
   type=INTEGER value=3 lineno=1
   type=+ value=+ lineno=1
   type=INTEGER value=4 lineno=1
   type=* value=* lineno=1
   type=( value=( lineno=1
   type=INTEGER value=2 lineno=1
   type=- value=- lineno=1
   type=INTEGER value=1 lineno=1
   type=) value=) lineno=1
   type=NEWLINE value= lineno=1

   Result:
   7
   ```

## Troubleshooting

If you encounter errors:

1. **Check Token Definitions**: Ensure tokens in `Lexer1.py` match those expected in `Parser1.py`.
2. **Verify Parsing Rules**: Make sure the parsing rules and action methods in `Parser1.py` are correctly defined and match the tokens.
3. **Debug with Print Statements**: Add print statements to debug token values and parsing results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Feel free to customize this `README.md` based on your specific needs and project details.