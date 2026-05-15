# recommendation_system.py

products = {
    "tecnologia": ["Notebook", "Mouse", "Teclado"],
    "ropa": ["Polera", "Pantalón", "Chaqueta"],
    "hogar": ["Silla", "Mesa", "Lámpara"]
}

category = input("Ingrese una categoría: tecnologia, ropa u hogar: ").lower()

if category in products:
    print("Productos recomendados:")
    
    for product in products[category]:
        print("-", product)
else:
    print("Categoría no encontrada.")