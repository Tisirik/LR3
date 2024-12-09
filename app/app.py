if name == "main":
    Shape.about()

    try:
        radius = float(input("Введите радиус шара: "))
        sphere = Sphere(radius)

        volume = sphere.calculate_volume()
        print(f"Объем шара с радиусом {sphere.radius} равен {volume:.2f}")
    except ValueError as e:
        print(f"Ошибка: {e}")