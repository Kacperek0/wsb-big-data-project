import sys

def combiner():

    last_key = None
    sum_value = 0

    for line in sys.stdin:
        line = line.strip()
        line = line.split('\t')
        key = line[0]
        value = int(line[1])

        if last_key == key:
            sum_value += value
        else:
            if last_key:
                print(f'{last_key}\t{sum_value}')
            sum_value = value
            last_key = key

    if last_key == key:
        print(f'{last_key}\t{sum_value}')

if __name__ == '__main__':
    combiner()
