import math

def gen_extension_seq(n, push_limit=12):
    seq = []

    temp = []
    num_subseqs = math.ceil(n / push_limit)
    counter = 1
    flag = True

    while flag:
        if counter < num_subseqs:
            temp.append(push_limit * counter)
        if counter == num_subseqs:
            temp.append(n)

        seq.append(temp)
        temp = [i-1 for i in temp if (i-1) != 0]
        counter += 1

        flag = len(temp) != 0 or counter <= num_subseqs

    return seq

def gen_retraction_seq(n):
    seq = []

    for i in range(n):
        temp = []

        for j in range(1, i+2):
            if i % 2 != j % 2:
                temp.append(j)

        seq.append(temp)

    seq += seq[:-1][::-1]
    return seq

def main():
    print("Extension sequence for 13-piston extender:")
    for x in gen_extension_seq(13):
        print(x)

    print("Retraction sequence for 5-piston extender:")
    for x in gen_retraction_seq(5):
        print(x)

if __name__ == '__main__':
    main()