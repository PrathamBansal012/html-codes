def probability_union(a, b, all_possible_outcomes):
    prob_a = len(a) / len(all_possible_outcomes)
    prob_b = len(b) / len(all_possible_outcomes)
    intersection = a.intersection(b)
    prob_intersection = len(intersection) / len(all_possible_outcomes)
    union = a.union(b)
    prob_union = len(union) / len(all_possible_outcomes)
    return prob_union, prob_intersection
all_possible_rolls = {'F', 'E', 'D', 'C', 'B', 'A'}
even_numbers = {'I', 'H', 'G'}
numbers_greater_than_three = {'L', 'K', 'J'}
prob_union, prob_intersection = probability_union(
    even_numbers,
    numbers_greater_than_three,
    all_possible_rolls)
print("Probability of union:", prob_union)
print("Probability of intersection:", prob_intersection)