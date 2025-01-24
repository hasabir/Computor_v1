from fractions import Fraction

class AdvancedPolynomialSolver:
    def __init__(self, equation):
        self.equation = equation.strip()
        self.stock = {}
        self.variable = self._parse_equation()
        stock = self._get_reduced_form(self.equation.split("=")[0], 'left')
        print(f"stock after change :\n{stock}")
    
    def get_stock(self):
        return self.stock


# if equation_list[i]  == '^' and (equation_list[i + 1] == '' or equation_list[i + 1].isdigit() == False):
#                 raise SyntaxError("Error: Incorrect format")


    def _get_reduced_form(self, equation, equation_parts, stoclk={}):
        equation = "".join(equation.split(" "))
        const_holder = []
        
        print(equation)
        for i in range(len(equation)):
            print(f"************************ i: {i} | equation[i]: {equation[i]} *************************")
            if equation[i].isdigit():
                print(f"var is digit -->  {equation[i]}",end=" | ")
                # if const_holder:
                #         const_holder.append(str(-1 * float(equation[i])))
                #     else:
                #         const_holder.append(float(equation[i]))
                # print(f"const_holder : {const_holder}")
            
            
            elif equation[i] == '*':
                if equation[i + 1].isdigit():
                    print(f"the var is not * --> {equation[i]} | const_holder: {const_holder}")
                    const_holder.append(float(const_holder.pop()) * float(equation[i + 1]))
                    i += 1
            
            elif equation[i] == '/':
                if equation[i] == '/' and equation[i + 1] and (equation[i + 1] == '0' \
                    or equation[i + 1].isdigit() == False):
                    raise SyntaxError("Error: Incorrect format")
                const_holder.append(float(const_holder.pop()) / float(equation[i + 1]))
                i += 1
            
            elif equation[i] == self.variable:
                print(f"var is {equation[i]}, const_holder: {const_holder}")
                if equation[i + 1] == '^':
                    
                    if equation[i + 2].isdigit():
                        stock[int(equation[i + 2])] = equation[i + 2]
                        i += 2
                else:
                    stock[1] = const_holder.pop()
            
            
            elif len(const_holder) != 0 and  equation[i] in ('+', '-'):
                stock[0] = const_holder.pop()
                const_holder.append(equation[i])
        return stock


    def _parse_equation(self):
        if self.equation == '':
            raise SyntaxError(("Error: Invalid equation, empty equation"))

        variables = ''.join([c for c in set(self.equation) if c.isalpha()])
        if len(variables) > 1:
            raise SyntaxError(("Error: Invalid equation, only one variable is allowed"))
        for var in self.equation:
            if var not in ('*', '+', '-', '^', variables, ' ', '=') and not var.isdigit():
                raise SyntaxError(("Error: Syntax error"))
        if self.equation.count('=') != 1:
            raise SyntaxError(("Error: Invalid equation, only one equal sign is allowed"))
        if (not self.equation[0].isalnum() or self.equation[0] not in '+-') \
                and not self.equation[-1].isalnum():
            raise SyntaxError(("Error: Invalid equation"))
        return variables