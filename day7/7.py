
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
            })


def find_name_in_list(name):
    for tree in list_of_names:
        if tree['name'] == name:
            tree['already_pinned_somewhere'] = True
            return tree

for tree in list_of_names:
    for child_name in tree['children_to_find']:
        tree['children'].append(find_name_in_list(child_name))

for tree in list_of_names:
    if not tree['already_pinned_somewhere']:
        print(tree['name'], tree['children_to_find'])
