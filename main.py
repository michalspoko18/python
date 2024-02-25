import time

def write_current_time_to_file(filename):
    while True:
        current_time = time.strftime("%H:%M:%S")  # Pobranie aktualnej godziny w formacie HH:MM:SS
        print(current_time)
        with open(filename, 'a') as file:  # Otwarcie pliku w trybie dopisywania
            file.write(current_time + '\n')  # Dopisanie aktualnej godziny do pliku
        time.sleep(10)  # Poczekanie 10 sekund

if __name__ == "__main__":
    filename = "current_time.txt"
    write_current_time_to_file(filename)
