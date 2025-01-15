class AdvancedNumber:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an integer or float.")
        self.value = value

    def __str__(self):
        return f"Value: {self.value}"

    def __repr__(self):
        return f"AdvancedNumber({self.value})"

    def __add__(self, other):
        return AdvancedNumber(self.value + self._get_other_value(other))

    def __sub__(self, other):
        return AdvancedNumber(self.value - self._get_other_value(other))

    def __mul__(self, other):
        return AdvancedNumber(self.value * self._get_other_value(other))

    def __truediv__(self, other):
        return AdvancedNumber(self.value / self._get_other_value(other))

    def __mod__(self, other):
        return AdvancedNumber(self.value % self._get_other_value(other))

    def __lt__(self, other):
        return self.value < self._get_other_value(other)

    def __le__(self, other):
        return self.value <= self._get_other_value(other)

    def __gt__(self, other):
        return self.value > self._get_other_value(other)

    def __ge__(self, other):
        return self.value >= self._get_other_value(other)

    def __eq__(self, other):
        return self.value == self._get_other_value(other)

    def __ne__(self, other):
        return self.value != self._get_other_value(other)

    def __hash__(self):
        return hash(self.value)

    def __bool__(self):
        return self.value != 0

    def __call__(self):
        return self.value ** 2

    def __format__(self, format_spec):
        if format_spec == "#x" and isinstance(self.value, int):
            return hex(self.value)
        return format(self.value, format_spec)

    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed")

    def _get_other_value(self, other):
        if isinstance(other, AdvancedNumber):
            return other.value
        elif isinstance(other, (int, float)):
            return other
        else:
            raise ValueError("Operand must be an AdvancedNumber, int, or float.")

if __name__ == "__main__":
    import pytest

    pytest.main(["-q", "--disable-warnings", "-v", __file__])
