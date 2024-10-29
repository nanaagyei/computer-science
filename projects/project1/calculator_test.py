import pytest
from calculator import Calculator
from tkinter import Tk
import time

@pytest.fixture
def calculator():
    root = Tk()
    calc = Calculator(root)
    yield calc
    root.destroy()

def test_addition(calculator):
    # Input numbers using GUI buttons
    calculator.button_click('2')
    calculator.button_click('+')
    calculator.button_click('3')
    calculator.button_click('=')
    assert calculator.display_var.get() == '5'
    
    # Clear for next operation
    calculator.button_click('C')
    
    # Test negative numbers
    calculator.button_click('-')
    calculator.button_click('1')
    calculator.button_click('+')
    calculator.button_click('1')
    calculator.button_click('=')
    assert calculator.display_var.get() == '0'

def test_subtraction(calculator):
    calculator.button_click('5')
    calculator.button_click('-')
    calculator.button_click('3')
    calculator.button_click('=')
    assert calculator.display_var.get() == '2'
    
    calculator.button_click('C')
    calculator.button_click('1')
    calculator.button_click('-')
    calculator.button_click('1')
    calculator.button_click('=')
    assert calculator.display_var.get() == '0'

def test_multiplication(calculator):
    calculator.button_click('2')
    calculator.button_click('*')
    calculator.button_click('3')
    calculator.button_click('=')
    assert calculator.display_var.get() == '6'
    
    calculator.button_click('C')
    calculator.button_click('-')
    calculator.button_click('2')
    calculator.button_click('*')
    calculator.button_click('3')
    calculator.button_click('=')
    assert calculator.display_var.get() == '-6'

def test_division(calculator):
    calculator.button_click('6')
    calculator.button_click('/')
    calculator.button_click('2')
    calculator.button_click('=')
    assert calculator.display_var.get() == '3'
    
    calculator.button_click('C')
    calculator.button_click('5')
    calculator.button_click('/')
    calculator.button_click('2')
    calculator.button_click('=')
    assert calculator.display_var.get() == '2.5'

def test_division_by_zero(calculator):
    calculator.button_click('5')
    calculator.button_click('/')
    calculator.button_click('0')
    calculator.button_click('=')
    assert calculator.display_var.get() == 'Error'

def test_decimal_operations(calculator):
    calculator.button_click('0')
    calculator.button_click('.')
    calculator.button_click('1')
    calculator.button_click('+')
    calculator.button_click('0')
    calculator.button_click('.')
    calculator.button_click('2')
    calculator.button_click('=')
    assert float(calculator.display_var.get()) == pytest.approx(0.3)

def test_clear_functionality(calculator):
    calculator.button_click('1')
    calculator.button_click('2')
    calculator.button_click('3')
    calculator.button_click('C')
    assert calculator.display_var.get() == '0'

def test_consecutive_operations(calculator):
    calculator.button_click('2')
    calculator.button_click('+')
    calculator.button_click('3')
    calculator.button_click('=')
    calculator.button_click('+')
    calculator.button_click('4')
    calculator.button_click('=')
    assert calculator.display_var.get() == '9'

def test_keyboard_input(calculator):
    # Simulate keyboard input
    calculator.handle_keypress(type('Event', (), {'char': '2', 'keysym': '2'}))
    calculator.handle_keypress(type('Event', (), {'char': '+', 'keysym': 'plus'}))
    calculator.handle_keypress(type('Event', (), {'char': '3', 'keysym': '3'}))
    calculator.handle_keypress(type('Event', (), {'char': '', 'keysym': 'Return'}))
    assert calculator.display_var.get() == '5'

def test_keyboard_backspace(calculator):
    calculator.handle_keypress(type('Event', (), {'char': '1', 'keysym': '1'}))
    calculator.handle_keypress(type('Event', (), {'char': '2', 'keysym': '2'}))
    calculator.handle_keypress(type('Event', (), {'char': '3', 'keysym': '3'}))
    calculator.handle_keypress(type('Event', (), {'char': '', 'keysym': 'BackSpace'}))
    assert calculator.display_var.get() == '12'

def test_invalid_keyboard_input(calculator):
    original_value = calculator.display_var.get()
    calculator.handle_keypress(type('Event', (), {'char': 'a', 'keysym': 'a'}))
    assert calculator.display_var.get() == 'Invalid Input'
    # Wait for error message to clear
    calculator.root.after(1100)
    assert calculator.display_var.get() == original_value
