"""
References

https://en.wikipedia.org/wiki/Polynomial_interpolation
https://en.wikipedia.org/wiki/Lagrange_polynomial#Example_1
http://scholarpedia.org/article/WENO_methods


"""

x_points = [0, 1, 2]
y_points = list(map(lambda x: x*x, x_points))

interpolation_point = 0.5

for xj in x_points:
    print(f"j: {xj}")

    coefficient = 1
    for xm in x_points:
        if xj!=xm:
            coefficient = coefficient * (interpolation_point - xm) / (xj - xm)

    print(f"Coefficient: {coefficient}")