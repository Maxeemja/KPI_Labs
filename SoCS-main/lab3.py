import re
import copy

from lab2 import ExpressionOptimizer, ExpressionError


class DistributiveTransformator:
    def __init__(self, expression):
        if expression:
            self.expression = expression
            self._token_i = 0
            self._tokens = self._tokens_conversion()
        else:
            raise ExpressionError("Empty expression")

    def _tokenizer(self):
        tokens = re.findall(r"\d+\.\d+|\d+|[a-zA-Z_][a-zA-Z0-9_]*|[+\-*/()]", self.expression)
        return tokens

    def _tokens_conversion(self):
        tokens = self._tokenizer()
        new_tokens = []
        while self._token_i < len(tokens):
            if tokens[self._token_i] == "(":
                self._token_i += 1
                new_tokens.append(self._tokens_conversion())
            elif tokens[self._token_i] == ")":
                self._token_i += 1
                return new_tokens
            else:
                new_tokens.append(tokens[self._token_i])
                self._token_i += 1
        return new_tokens

    @staticmethod
    def _brackets_distributive_operation(tokens, token_i):
        if token_i > 0:
            if tokens[token_i - 1] == "*":
                if token_i < 3 or tokens[token_i - 3] != "/":
                    help_list = []
                    for sub_token in tokens[token_i]:
                        help_list.append(sub_token)
                        if sub_token in ["+", "-"]:
                            help_list.extend([tokens[token_i - 2], tokens[token_i - 1]])
                    if help_list[0] != "-":
                        help_list = [tokens[token_i - 2], tokens[token_i - 1]] + help_list
                    tokens = tokens[:token_i - 2] + [help_list] + tokens[token_i + 1:]
                    return tokens[0] if len(tokens) == 1 else tokens, False
        if 0 < token_i < len(tokens) - 1:
            if tokens[token_i - 1] == "/":
                if tokens[token_i + 1] == "/":
                    tokens = tokens[:token_i] + [[tokens[token_i], "*", tokens[token_i + 2]]] + tokens[token_i + 3:]
                    return tokens[0] if len(tokens) == 1 else tokens, False
                else:
                    return [], True
        if token_i < len(tokens) - 1:
            if tokens[token_i + 1] in ["*", "/"]:
                help_list = []
                for sub_token_i, sub_token in enumerate(tokens[token_i]):
                    if sub_token in ["+", "-"] and sub_token_i != 0:
                        help_list.extend([tokens[token_i + 1], tokens[token_i + 2]])
                    help_list.append(sub_token)
                help_list.extend([tokens[token_i + 1], tokens[token_i + 2]])
                tokens = tokens[:token_i] + [help_list] + tokens[token_i + 3:]
                return tokens[0] if len(tokens) == 1 else tokens, False
        return [], True

    def _expression_transformer_helper(self, tokens):
        for token_i, token in enumerate(tokens):
            if isinstance(token, list):
                if not any(isinstance(sub_token, list) for sub_token in token):
                    new_tokens, need_skip_stap = self._brackets_distributive_operation(tokens, token_i)
                    if need_skip_stap:
                        continue
                    return new_tokens
                else:
                    new_token = self._expression_transformer_helper(copy.deepcopy(token))
                    if new_token != token:
                        tokens[token_i] = new_token
                        return tokens
                    else:
                        new_tokens, need_skip_stap = self._brackets_distributive_operation(tokens, token_i)
                        if need_skip_stap:
                            continue
                        return new_tokens
        return tokens

    def expression_transformer(self):
        old_tokens = None
        expression_forms = []
        while self._tokens != old_tokens:
            old_tokens = copy.deepcopy(self._tokens)
            self._tokens = self._expression_transformer_helper(self._tokens)
            expression_forms.append(old_tokens)

        return expression_forms

    def _tokens_reverse_conversion(self, tokens):
        output = []
        for token in tokens:
            if isinstance(token, list):
                if not any(isinstance(sub_token, list) for sub_token in token):
                    output.extend(["("] + token + [")"])
                else:
                    output.extend(["("] + self._tokens_reverse_conversion(token) + [")"])
            else:
                output.append(token)
        return output

    def _expression_string_builder(self, tokens):
        return "".join(self._tokens_reverse_conversion(tokens))

    def expression_forms(self):
        print()
        print("Expression forms:")

        expression_forms = list(map(self._expression_string_builder, self.expression_transformer()))

        for form_i, expression_form in enumerate(expression_forms, start=1):
            print(f"{form_i}.\t{expression_form}")

        return expression_forms[1:]


if __name__ == "__main__":
    """
    ((a+b)*c)+d*(e+f)
    (-a+b)*(-c+d)
    (-a)*(b+c)
    (a+b)*(-c)
    a/(b/(c+d))/(e+f)
    
    a*(b+c)
    a/(b+c)
    (a+b)/c
    (a+b)*c
    a/(b+c)*d
    a*(b+c)*d
    a*(b+c)/d
    -a*(b+c+d)/e
    a/(b+c)/d
    a/((b+c)/d)
    (a*b)/c
    -(a+b+c)/d
    -c*(a*b)
    (b-(d9+c))*a/7
    
    a*(b+c-1)*d
    (a-c)*(b-k+1)
    (1-d)/(a+b-2)/e
    a-b*(k-t)-(f-g)*(f*5.9-q)-(f+g)/(d+q-w)
    a-b*(k-t+(f-g)*(f*5.9-q)+(w-y*(m-1))/p)-(x-3)*(x+3)/(d+q-w)
    
    a*(c+d+e+f)+a*(b-g-a-q)-a*(5+3+2)
    v/(c3+f9)+v/(-q1+3)-v/(f1+3-5)
    a*(c+d+a*(b-c))
    a*b+a*c-a*d
    v*g-+d*q-v*q+d*p*d
    """
    expression = "a-b*(k-t+(f-g)*(f*5.9-q)+(w-y*(m-1))/p)-(x-3)*(x+3)/(d+q-w)"
    print(f"Expression:\n{expression}")
    print()
    expression_optimizer = ExpressionOptimizer(expression)
    optimized_expression = expression_optimizer.optimizer()
    distributive_transformer = DistributiveTransformator(optimized_expression)
    distributive_transformer.expression_forms()
