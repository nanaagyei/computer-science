# Advanced Calculator

A Python-based calculator application with a graphical user interface built using tkinter.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Advanced operations (square root, exponentiation)
- Error handling for invalid operations
- Backspace functionality
- Clear function
- Decimal point support

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nanaagyei/computer-science.git
   cd projects/project1
   ```

2. No additional dependencies needed as tkinter comes with Python!

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the following command:
   ```bash
   python calculator.py
   ```

## Usage

### Basic Operations
- Use the number pad to input numbers
- Click on operation buttons to perform calculations
- '=' button evaluates the expression
- 'C' button clears the display
- '←' button acts as backspace

### Advanced Operations
- '√' button calculates square root
- '^' button is used for exponentiation

### Examples
```
Input: 5 + 3
Output: 8

Input: 16 √
Output: 4

Input: 2 ^ 3
Output: 8

Input: 10 / 2
Output: 5
```

## Error Handling

The calculator handles various errors including:
- Division by zero
- Invalid mathematical operations
- Syntax errors

## Contributing

We welcome contributions to improve the Advanced Calculator! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests to ensure everything works
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add appropriate comments and documentation
- Include unit tests for new features
- Update the README.md if adding new functionality

### Adding New Operations
To add a new mathematical operation:
1. Add the operation button in `calculator.py`
2. Implement the operation logic
3. Add error handling for the new operation
4. Include tests in `calculator_test.py`

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.
