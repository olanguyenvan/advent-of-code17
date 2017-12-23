from collections import defaultdict

list_of_names = []

if __name__ == '__main__':
    with open('input.txt') as fd:
        node_informations = fd.read().splitlines()
        for node_info in node_informations:
            names_split = node_info.split(' ')
            names_split = [name_split.replace(',', '') for name_split in names_split]
            children_to_find = names_split[3:] if len(names_split) > 2 else []
            list_of_names.append({
                'name': names_split[0],
                'children': [],
                'children_to_find': children_to_find,
                'already_pinned_somewhere': False,
                'its_weight':int(names_split[1].replace('(', '').replace(')', '')),
                'weight': int(names_split[1].replace('(', '').replace(')', '')),
            })


def find_name_in_list(name):
    for tree in list_of_names:
        if tree['name'] == name:
            tree['already_pinned_somewhere'] = True
            return tree


for tree in list_of_names:
    for child_name in tree['children_to_find']:
        tree['children'].append(find_name_in_list(child_name))


def find_root(list_of_subtrees):
    for tree in list_of_subtrees:
        if not tree['already_pinned_somewhere']:
            return tree


root = find_root(list_of_names)

print("The root is '%s'\n" % root['name'])


def find_correct_weight(tree_subtree):

    children_weights = defaultdict(list)
    for child_subtree in tree_subtree['children']:
        wrong_weight_name = find_correct_weight(child_subtree)
        if wrong_weight_name:
            return wrong_weight_name
        children_weights[child_subtree['weight']].append(child_subtree['name'])
        tree_subtree['weight'] += child_subtree['weight']

    if len(children_weights) > 1:

        weights_sorted_by_occurance = list(children_weights.items())
        weights_sorted_by_occurance.sort(key=lambda tup: len(tup[1]))
        wrong_total_weight = weights_sorted_by_occurance[0][0]
        correct_total_weight = weights_sorted_by_occurance[1][0]
        node_name_with_wrong_weight = weights_sorted_by_occurance[0][1][0]

        diff = wrong_total_weight - correct_total_weight
        for node in list_of_names:
            if node['name'] == node_name_with_wrong_weight:
                return node['its_weight'] - diff


correct_weight = find_correct_weight(root)
print("the correct weight is %s " % correct_weight)