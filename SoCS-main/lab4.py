import re

from lab2 import ExpressionOptimizer, ExpressionError


class AssociativeTransformer:
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
    def _associative_transformations(tokens):
        terms = []

        for token in tokens:
            if token in ["+", "-"]:
                terms.append([])
            if not terms:
                terms.append(["+"])
            terms[-1].append(token)

        division_operands = []
        multiplication_operands = []

        for term in terms:
            division_operands.append([])
            multiplication_operands.append([])
            for token_i, token in enumerate(term):
                if token not in ["+", "-", "*", "/"]:
                    if term[token_i - 1] == "/":
                        if token not in division_operands[-1]:
                            division_operands[-1].append(token)
                    else:
                        if token not in multiplication_operands[-1]:
                            multiplication_operands[-1].append(token)

        division_operands = [operand for term in division_operands for operand in term]
        multiplication_operands = [operand for term in multiplication_operands for operand in term if operand != "1"]

        def counter(lst, find_elem):
            count = 0
            for elem in lst:
                if find_elem == elem:
                    count += 1
            return count

        non_unique_division_operands = []
        non_unique_multiplication_operands = []

        for operand in division_operands:
            if operand not in non_unique_division_operands and counter(division_operands, operand) > 1:
                non_unique_division_operands.append(operand)

        for operand in multiplication_operands:
            if operand not in non_unique_multiplication_operands and counter(multiplication_operands, operand) > 1:
                non_unique_multiplication_operands.append(operand)

        forms = []

        for division_operand in non_unique_division_operands:
            new_form = [[], "/", division_operand]
            for term_i, term in enumerate(terms):
                for token_i, token in enumerate(term):
                    if token == division_operand and term[token_i - 1] == "/":
                        new_term = term[:token_i - 1] + term[token_i + 1:]
                        new_form[0].extend(new_term)
                        break
                else:
                    new_form.extend(term)
            forms.append(new_form)

        for multiplication_operand in non_unique_multiplication_operands:
            new_form = [multiplication_operand, "*", []]
            for term_i, term in enumerate(terms):
                for token_i, token in enumerate(term):
                    if token == multiplication_operand and term[token_i - 1] != "/":
                        if token_i == len(term) - 1:
                            if len(term) == 2:
                                new_term = term[:token_i] + ["1"]
                                new_form[2].extend(new_term)
                            else:
                                new_term = term[:token_i - 1]
                                new_form[2].extend(new_term)
                        else:
                            if term[token_i + 1] == "/":
                                if term[token_i - 1] != "*":
                                    new_term = term[:token_i] + ["1"] + term[token_i + 1:]
                                    new_form[2].extend(new_term)
                                else:
                                    new_term = term[:token_i - 1] + term[token_i + 1:]
                                    new_form[2].extend(new_term)
                            else:
                                new_term = term[:token_i] + term[token_i + 2:]
                                new_form[2].extend(new_term)
                        break
                else:
                    new_form.extend(term)
            forms.append(new_form)

        def add_clearing(expression_form):
            if expression_form[0] == "+":
                expression_form = expression_form[1:]
            for token_i, token in enumerate(expression_form):
                if isinstance(token, list):
                    expression_form[token_i] = add_clearing(token)
            return expression_form

        for form_i, form in enumerate(forms):
            forms[form_i] = add_clearing(form)

        return forms

    def _expression_transformer_helper(self, tokens):
        for token_i, token in enumerate(tokens):
            if isinstance(token, list):
                new_sub_forms = self._expression_transformer_helper(token)
                if new_sub_forms:
                    new_forms = []
                    for new_sub_form in new_sub_forms:
                        new_form = tokens[:token_i] + [new_sub_form] + tokens[token_i + 1:]
                        new_forms.append(new_form)
                    return new_forms
        return self._associative_transformations(tokens)

    def expression_transformer(self):
        expression_forms_groups = [[self._tokens]]
        while expression_forms_groups[-1]:
            last_expression_forms_group = expression_forms_groups[-1]
            expression_forms_groups.append([])
            for expression_form in last_expression_forms_group:
                new_forms = self._expression_transformer_helper(expression_form)
                if new_forms:
                    expression_forms_groups[-1].extend(new_forms)
        else:
            expression_forms_groups.pop()

        return expression_forms_groups

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
        print("Expressions forms:")

        expression_forms = []

        for group_i, expression_forms_group in enumerate(self.expression_transformer(), start=1):
            for form_i, expression_form in enumerate(expression_forms_group, start=1):
                expression_string = self._expression_string_builder(expression_form)
                expression_forms.append(expression_string)
                print(f"{group_i}.{form_i}.\t{expression_string}")
            print()

        return expression_forms[1:]


if __name__ == "__main__":
    """
    a*c+a*d+a*b+b*f=a*(c+d+b)+b*f=b*(a+f)+a*c+a*d=b*(a+f)+a*(c*d)
    
    a*b+a*(b*c+b*f+c*a+a*d)
    a*b+a*(a*c+a*d+a*b+b*f)+g+h
    a*b+a*(a*b+a*(b*c+b*a+a*f))+g+h
    
    (a+b)*a*c+(a+b)*b*a+(a+b)*c*b
    (a*b+a/c)*a+(a*b+a/c)*b
    (a*b/1+0*f+a/c)*a+(a*b+a/c)*0+(0+a*b+a/c*1)*b
    (a+(b*c+c))*a*c-(a+(b*c+c))*b*a+(a+(b*c+c))*c*b
    
    v/(c3+f9)+v/(-q1+3)-v/(f1+3-5)
    a*(c+d+a*(b-c))
    a*b+a*c-a*d
    v*g-+d*q-v*q+d*p*d
    """
    expression = "(a*b/1+0*f+a/c)*a+(a*b+a/c)*0+(0+a*b+a/c*1)*b"
    print(f"Expression:\n{expression}")
    print()
    expression_optimizer = ExpressionOptimizer(expression)
    optimized_expression = expression_optimizer.optimizer()
    associative_transformator = AssociativeTransformer(optimized_expression)
    associative_transformator.expression_forms()
