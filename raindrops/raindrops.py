def convert(number: int):
    output = ''
    rain = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    drops = [s for f, s in rain.items() if number % f == 0]
    return "".join(drops) if drops else str(number)

if __name__ == "__main__":
    print(convert(105))
