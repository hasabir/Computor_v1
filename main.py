import typer
from polynomialSolver import PolynomialSolver

app = typer.Typer()

def display_equation_and_degree(solver):
    parsed_equation = solver.get_parsed_equation()

    equation_str = ''
    for key, value in parsed_equation.items():
        equation_str += f"{value.replace('-', '- ').replace('+', '+ ')} * X^{key} "
    
    print(f"Reduced form: {equation_str}= 0")
    polynomial_degree = max(parsed_equation.keys())
    print(f"Polynomial degree: {polynomial_degree}")
    if polynomial_degree > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    
    return polynomial_degree, parsed_equation



@app.command(name="computor")
def solve_equation(equation: str):
    try:
        solver = PolynomialSolver(equation)
        polynominal_degree, parsed_equation = display_equation_and_degree(solver)

        if polynominal_degree == 2:
            PolynomialSolver.solve_degree_2(parsed_equation)
        else:
            PolynomialSolver.solve_degree_1(parsed_equation)
    except Exception as e:
        print(e)

@app.command(name="computor_bonus")
def solve_equation_bonus(equation: str):
    from advanced_polynomial_solver import AdvancedPolynomialSolver

    try:
        solver = AdvancedPolynomialSolver(equation)
        polynomial_degree, parsed_equation = display_equation_and_degree(solver)
        if polynomial_degree == 2:
            solver.solve_degree_2(parsed_equation)
        else:
            solver.solve_degree_1(parsed_equation)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app()
