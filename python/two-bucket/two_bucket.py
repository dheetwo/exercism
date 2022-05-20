def measure(bucket_one, bucket_two, goal, start_bucket):
    known_nodes = [root(bucket_one, bucket_two, start_bucket)]
    FORBIDDEN_NODES = forbidden_nodes(bucket_one, bucket_two, start_bucket)
    previous_layer = known_nodes
    layer_number = 0
    while not goal_node_found(known_nodes, goal):
        children_nodes = []
        layer_number += 1
        for node in previous_layer:
            children_nodes = pour_nodes(node, bucket_one, bucket_two, known_nodes, FORBIDDEN_NODES) + \
                             empty_nodes(node, known_nodes, FORBIDDEN_NODES) + \
                             fill_nodes(node, bucket_one, bucket_two, known_nodes, FORBIDDEN_NODES)
        for node in set(children_nodes):
            known_nodes.append(node)
        previous_layer = children_nodes
        layer_number += 1



def pour_nodes(input, bucket_one, bucket_two, known, forbidden):
    total = sum(input)
    pour_nodes = []
    if input[0] < bucket_one and total <= bucket_one:
        pour_nodes.append((total, 0))
    elif input[0] < bucket_one and total > bucket_two:
        pour_nodes.append((bucket_one, total - bucket_one))
    if input[1] < bucket_two and total <= bucket_two:
        pour_nodes.append((0, total))
    elif input[1] < bucket_two < total:
        pour_nodes.append((total - bucket_two, bucket_two))
    return list(set(pour_nodes) - set(known) - set(forbidden))


def empty_nodes(input, known, forbidden):
    return list({(input[0], 0), (0, input[1])} - set(known) - set(forbidden))


def fill_nodes(input, bucket_one, bucket_two, known, forbidden):
    return list({(input[0], bucket_two), (bucket_one, input[1])} - set(known) - set(forbidden))


def root(bucket_one, bucket_two, start_bucket):
    if start_bucket == "one":
        return bucket_one, 0
    elif start_bucket == "two:":
        return 0, bucket_two


def forbidden_nodes(bucket_one, bucket_two, start_bucket):
    if start_bucket == "one":
        return [(0, 0), (0, bucket_two)]
    elif start_bucket == "two":
        return [(0, 0), (bucket_one, 0)]


def goal_node_found(node_list, goal):
    for node in node_list:
        if goal in node:
            return True
    return False


measure(3, 5, 1, "one")
