def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(input_list):
    max = input_list[0]
    for n in input_list:
        if n > max:
            max = n
    return max
