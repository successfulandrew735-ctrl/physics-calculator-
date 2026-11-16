
def speed(distance, time):
    return distance / time

def force(mass, acceleration):
    return mass * acceleration

def density(mass, volume):
    return mass / volume

def weight(mass):
    return mass * 9.8

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


while True:
    print("\nPHYSICS CALCULATOR")
    print("1. Speed")
    print("2. Force")
    print("3. Density")
    print("4. Weight")
    print("5. Kinetic Energy")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        d = float(input("Enter distance: "))
        t = float(input("Enter time: "))
        print("Speed:", speed(d, t))

    elif choice == "2":
        m = float(input("Enter mass: "))
        a = float(input("Enter acceleration: "))
        print("Force:", force(m, a))

    elif choice == "3":
        m = float(input("Enter mass: "))
        v = float(input("Enter volume: "))
        print("Density:", density(m, v))

    elif choice == "4":
        m = float(input("Enter mass: "))
        print("Weight:", weight(m))

    elif choice == "5":
        m = float(input("Enter mass: "))
        v = float(input("Enter velocity: "))
        print("Kinetic Energy:", kinetic_energy(m, v))

    else:
        print("Invalid choice")

    answer = input("Do you want to continue? (YES/NO): ")

    if answer.upper() == "NO":
        print("Physics Calculator stopped.")
        break
