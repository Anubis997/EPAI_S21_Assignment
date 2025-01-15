# EPAI_S21_Assignment

AdvancedNumber Class
The AdvancedNumber class is a custom wrapper for numeric types (int and float) that enhances their behavior with additional functionalities and customizations. Below is a concise overview of its key features:

Key Features
Initialization and Validation:

Ensures value is either an int or float. Raises a ValueError otherwise.
String Representation:

__str__: Returns a user-friendly string (Value: <value>).
__repr__: Returns a developer-friendly representation (AdvancedNumber(<value>)).
Arithmetic Operations:

Supports addition (+), subtraction (-), multiplication (*), division (/), and modulus (%) with another AdvancedNumber, int, or float.
Comparison Operators:

Implements all comparison operators (<, <=, >, >=, ==, !=).
Hashing and Boolean Conversion:

__hash__: Uses the hash of the underlying value.
__bool__: Returns True if value is non-zero, False otherwise.
Callable Behavior:

__call__: Returns the square of the value when the instance is called.
Custom Formatting:

__format__: Supports standard formatting for numeric types. For integers, the custom format "#x" returns the hexadecimal representation.
Destructor:

__del__: Prints a message when an AdvancedNumber instance is destroyed.
Private Helper Method:

_get_other_value: Ensures compatibility with operations by extracting the numeric value from an AdvancedNumber, int, or float.


