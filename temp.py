import numpy as np
import matplotlib.pyplot as plt

def celsius_to_other(celsius_temps):
    """
    Convert Celsius to Fahrenheit and Kelvin.
    """
    fahrenheit = celsius_temps * 9 / 5 + 32
    kelvin = celsius_temps + 273.15
    return fahrenheit, kelvin

def fahrenheit_to_other(fahrenheit_temps):
    """
    Convert Fahrenheit to Celsius and Kelvin.
    """
    celsius = (fahrenheit_temps - 32) * 5 / 9
    kelvin = celsius + 273.15
    return celsius, kelvin

def kelvin_to_other(kelvin_temps):
    """
    Convert Kelvin to Celsius and Fahrenheit.
    """
    celsius = kelvin_temps - 273.15
    fahrenheit = celsius * 9 / 5 + 32
    return celsius, fahrenheit

def plot_conversions(input_temps, converted_temps, input_scale, output_scales):
    """
    Plot the input and converted temperatures using Matplotlib.
    """
    plt.figure(figsize=(10, 5))
    x = range(len(input_temps))
    plt.plot(x, input_temps, marker='o', label=f"Input ({input_scale})")
    for i, scale in enumerate(output_scales):
        plt.plot(x, converted_temps[i], marker='o', label=f"Converted ({scale})")
    plt.xlabel("Index")
    plt.ylabel("Temperature")
    plt.title("Temperature Conversion")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """
    Main function for the temperature converter program.
    """
    print("Temperature Converter with NumPy")
    print("Choose the scale of your input temperatures:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    try:
        # User choice for temperature scale
        choice = int(input("Enter your choice (1/2/3): "))
        if choice not in [1, 2, 3]:
            raise ValueError("Invalid choice! Please enter 1, 2, or 3.")

        # User input for temperatures
        input_temps = input("Enter a list of temperatures separated by spaces: ")
        temp_array = np.array(list(map(float, input_temps.split())))

        # Perform conversion based on user choice
        if choice == 1:
            fahrenheit, kelvin = celsius_to_other(temp_array)
            print("Input Temperatures (Celsius):", temp_array)
            print("Converted to Fahrenheit:", fahrenheit)
            print("Converted to Kelvin:", kelvin)
            plot_conversions(temp_array, [fahrenheit, kelvin], "Celsius", ["Fahrenheit", "Kelvin"])
        elif choice == 2:
            celsius, kelvin = fahrenheit_to_other(temp_array)
            print("Input Temperatures (Fahrenheit):", temp_array)
            print("Converted to Celsius:", celsius)
            print("Converted to Kelvin:", kelvin)
            plot_conversions(temp_array, [celsius, kelvin], "Fahrenheit", ["Celsius", "Kelvin"])
        elif choice == 3:
            celsius, fahrenheit = kelvin_to_other(temp_array)
            print("Input Temperatures (Kelvin):", temp_array)
            print("Converted to Celsius:", celsius)
            print("Converted to Fahrenheit:", fahrenheit)
            plot_conversions(temp_array, [celsius, fahrenheit], "Kelvin", ["Celsius", "Fahrenheit"])

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
