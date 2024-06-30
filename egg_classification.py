import json

def classify_egg(size):
    if size == 'small':
        return 'A'
    elif size == 'medium':
        return 'AA'
    elif size == 'large':
        return 'AAA'
    else:
        return 'BC'

def calculate_trays(classification):
    """
    Calculates the number of trays needed for each type of egg in the given classification.

    Args:
        classification (list): A list of dictionaries representing the classification of eggs.
            Each dictionary should have the following keys:
            - 'egg_type': The type of eggs ('A', 'AA', 'AAA', or other).
            - 'number_of_eggs': The number of eggs.

    Returns:
        None. The 'number_of_trays' key is added to each dictionary in the 'classification' list,
        representing the number of trays needed for the corresponding type of eggs.
    """
    for i in classification:
        if i['egg_type'] == 'A':
            i['number_of_trays'] = i['number_of_eggs'] // 30
        elif i['egg_type'] == 'AA':
            i['number_of_trays'] = i['number_of_eggs'] // 24
        elif i['egg_type'] == 'AAA':
            i['number_of_trays'] = i['number_of_eggs'] // 12
        else:
            i['number_of_trays'] = i['number_of_eggs'] // 30

def egg_classification(egg_data):
    classification = [
        {'egg_type': 'A', 'number_of_eggs': 0, 'number_of_trays': 0},
        {'egg_type': 'AA', 'number_of_eggs': 0, 'number_of_trays': 0},
        {'egg_type': 'AAA', 'number_of_eggs': 0, 'number_of_trays': 0},
        {'egg_type': 'BC', 'number_of_eggs': 0, 'number_of_trays': 0}
    ]
    for i in egg_data:
        if 55 <= i < 60:
            classification[0]['number_of_eggs'] += 1
        elif 60 <= i < 69:
            classification[1]['number_of_eggs'] += 1
        elif i >= 69:
            classification[2]['number_of_eggs'] += 1
        elif 43 <= i < 53:
            classification[3]['number_of_eggs'] += 1
        else:
            classification[3]['number_of_eggs'] += 1
    return classification

if __name__ == "__main__":
    egg_data = json.loads(input())
    classification = egg_classification(egg_data)
    calculate_trays(classification)

    print(classification)
