TipoPizza = input("¿Quiere una pizza vegetariana o normal? ")
if TipoPizza == "vegetariana":
    print("Ingredientes vegetarianos: Pimiento y Tofu")
    print("como ingretientes extras tienes: mozzarella y el tomate")
    Extra = input("¿Cual es la que vas a elegir?")
    PizzaTotal = "Pimiento, tofu"+ Extra
    print("Prefecto pues tu pizza sera",TipoPizza,"y los topins que tendra son: ",PizzaTotal,)

elif TipoPizza == "normal":
    print("Ingredientes normal: Peperoni, Jamon y Salmon")
    print("como ingretientes extras tienes: mozzarella y el tomate")
    Extra = input("¿Cual es la que vas a elegir? ")
    PizzaTotal = "Peperoni, Jamon y Salmon "+ Extra
    print("Prefecto pues tu pizza sera: ",TipoPizza," y los topins que tendra son: ",PizzaTotal,)

