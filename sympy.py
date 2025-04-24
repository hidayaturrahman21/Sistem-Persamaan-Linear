from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')

eq1 = Eq(2*x + 3*y, 7)
eq2 = Eq(x - y, 1)

solusi1 = solve((eq1, eq2), (x, y))
print("Solusi untuk soal 1:")
print(solusi1)

eq3 = Eq(x + 2*y + z, 10)
eq4 = Eq(3*x - y + 2*z, 5)
eq5 = Eq(-2*x + 3*y - z, -9)

solusi2 = solve((eq3, eq4, eq5), (x, y, z))
print("\nSolusi untuk soal 2:")
print(solusi2)
