import re


class ExpressionSyntaxError(Exception):
    pass


class ArithmeticOperatorError(ExpressionSyntaxError):
    pass


class BracketOrderError(ExpressionSyntaxError):
    pass


class ConstantError(ExpressionSyntaxError):
    pass


class VariableNameError(ExpressionSyntaxError):
    pass


class UnsupportedSymbolError(ExpressionSyntaxError):
    pass

class ExpressionEndError(ExpressionSyntaxError):
    pass


class ExpressionValidator:
    def __init__(self):
        self._state = "start"
        self._bracket_deep = 0
        self._point = False
        self._function = False
        self._expression_status = True

    def _start_check(self, char):
        if char == "-":
            self._state = "operator"
        elif char == "(":
            self._state = "open_bracket"
        elif re.match(r"[a-zA-Z_]", char) is not None:
            self._state = "variable"
        elif re.match(r"[0-9]", char) is not None:
            self._state = "constant"
        elif char in "+*/":
            raise ArithmeticOperatorError(f"Arithmetic expression can't start by this arithmetic operator: {char}")
        elif char == ")":
            raise BracketOrderError(f"Arithmetic expression can't start by close bracket")
        else:
            raise UnsupportedSymbolError(f"Arithmetic expression can't start by: {char}")

    def _operator_check(self, char):
        if char == "(":
            self._state = "open_bracket"
        elif re.match(r"[a-zA-Z_]", char) is not None:
            self._state = "variable"
        elif re.match(r"[0-9]", char) is not None:
            self._state = "constant"
        elif char == ")":
            raise BracketOrderError("Close bracket can't be after an arithmetic operator")
        elif char in "+-*/":
            raise ArithmeticOperatorError("Can't be two arithmetic operators in a row")
        else:
            raise UnsupportedSymbolError(f"Unsupported symbol after arithmetic operator: {char}")

    def _variable_check(self, char):
        if re.match(r"[a-zA-Z0-9_]", char) is not None:
            pass
        elif char in "+-*/":
            self._state = "operator"
        elif char == ")":
            if self._bracket_deep > 0:
                self._state = "close_bracket"
            else:
                raise BracketOrderError("Extra close bracket")
        elif char == "(":
            self._state = "open_bracket"
            self._function = True
        else:
            raise VariableNameError(f"In variable name can't be: {char}")

    def _constant_check(self, char):
        if re.match(r"[0-9]", char) is not None:
            self._point = False
        elif char == "." and not self._point:
            self._point = True
        elif char in "+-*/" and not self._point:
            self._state = "operator"
            self._point = False
        elif char == ")" and not self._point:
            if self._bracket_deep > 0:
                self._state = "close_bracket"
                self._point = False
            else:
                raise BracketOrderError("Extra close bracket")
        elif char == "." and self._point:
            raise ConstantError("Fractional number can't have more than one point")
        else:
            raise ConstantError(f"In constant can't be: {char}")

    def _open_bracket_check(self, char):
        self._bracket_deep += 1
        if char == "(":
            pass
        elif char == "-":
            self._state = "operator"
        elif char == ")" and self._function:
            self._state = "close_bracket"
            self._function = False
        elif re.match(r"[a-zA-Z_]", char) is not None:
            self._state = "variable"
        elif re.match(r"[0-9]", char) is not None:
            self._state = "constant"
        elif char in "+*/":
            raise ArithmeticOperatorError(f"After open bracket can't be: {char}")
        elif char == ")" and not self._function:
            raise BracketOrderError(f"Brackets can't be empty")
        else:
            raise UnsupportedSymbolError(f"Unsupported symbol after open bracket: {char}")

    def _close_bracket_check(self, char):
        self._bracket_deep -= 1
        if char in "+-*/":
            self._state = "operator"
        elif char == ")":
            if self._bracket_deep > 0:
                self._state = "close_bracket"
            else:
                self._bracket_deep += 1
                raise BracketOrderError("Extra close bracket")
        else:
            raise UnsupportedSymbolError(f"Unsupported symbol after close bracket: {char}")

    def validation(self, expression):
        # print(self._state, end="\n-------------------------------\n")
        for char_i, char in enumerate(expression):
            # print(char_i, char)
            try:
                if self._state == "start":
                    self._start_check(char)
                elif self._state == "operator":
                    self._operator_check(char)
                elif self._state == "variable":
                    self._variable_check(char)
                elif self._state == "constant":
                    self._constant_check(char)
                elif self._state == "open_bracket":
                    self._open_bracket_check(char)
                elif self._state == "close_bracket":
                    self._close_bracket_check(char)
            except Exception as e:
                self._expression_status = False
                print(f"Position {char_i}: {e}")
            # print(self._state, end="\n-------------------------------\n")
        if self._state == "close_bracket":
            self._bracket_deep -= 1
        try:
            if self._bracket_deep:
                raise BracketOrderError("Not all open brackets are closed")
            if self._state not in ("variable", "constant", "close_bracket"):
                raise ExpressionEndError(f"Expression can't end by this symbol: {expression[-1]}")
        except Exception as e:
            self._expression_status = False
            print(e)
        return self._expression_status
        # print(self._bracket_deep)


if __name__ == "__main__":
    """
    a+b*(c*cos(t-a*x)-d*sin(t+a*x)/(4.81*k-q*t))/(d*cos(t+a*y/f1(5.616*x-t))+c*sin(t-a*y*(u-v*i)))
    +5+1c*d+e-d*f3/cd_2*cos(g)*a
    -(b+c)+func1((1a*baa+1bj_ko2*(j-e))
    -a+b2*0
    g1+(a+10.3))+(6-sin(5)
    -((245.01+312,2)*b)+1b
    """
    expression = "a+b*(c*cos(t-a*x)-d*sin(t+a*x)/(4.81*k-q*t))/(d*cos(t+a*y/f1(5.616*x-t))+c*sin(t-a*y*(u-v*i)))"
    expression_validator = ExpressionValidator()
    if expression_validator.validation(expression):
        print("Expression is correct")
