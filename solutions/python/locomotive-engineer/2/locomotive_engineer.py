"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # IMPROVEMENT: Could add validation to ensure all args are valid wagon IDs
    # (e.g., integers or strings)
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # Unpack: first two wagons, rest go to 'last' variable
    f_w, s_w, *last = each_wagons_id
    # Reorder: put locomotive (1) first, then missing wagons, then remaining
    # IMPROVEMENT: Could validate that first_wagon is the locomotive (1)
    return [1, *missing_wagons, *last[1:], f_w, s_w]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # Collect all stop values from kwargs into a list
    # IMPROVEMENT: Could use list(kwargs.values()) for more concise code
    additional_stops = []
    for x in kwargs.values():
        additional_stops.append(x)
    # Create stops dictionary and merge with original route using unpacking
    additional_dict = {"stops": additional_stops}
    return {**route, **additional_dict}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    # Merge two dictionaries using unpacking (Python 3.5+)
    # IMPROVEMENT: Could use route | more_route_information for Python 3.9+
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Unpack 3x3 grid: each row has 3 wagon tuples
    [[a, b, c], [e, f, g], [h, i, j]] = wagons_rows
    # Transpose: convert rows to columns (3x3 matrix transpose)
    # IMPROVEMENT: Could use zip(*wagons_rows) for dynamic sizing
    #              e.g., [list(row) for row in zip(*wagons_rows)]
    return [[a, e, h], [b, f, i], [c, g, j]]
