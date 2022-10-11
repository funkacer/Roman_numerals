def check_input(inp, lst, verb = True):
    '''
    Check if input is in the list of options.

    Args:
        (str) inp - user input to check
        (list) lst - list of options to choose from
    Returns:
        (str) out - selected option from list or None
    '''

    assert isinstance(inp, str), 'Input must be a string'
    assert len(inp) > 0, 'Input must not be an empty string'
    assert isinstance(lst, list), 'List must be a list of strings'
    assert len(lst) > 0, 'List must not be an empty list'
    for f in lst:
        assert isinstance(f, str), 'List must be a list of strings'
        assert len(f) > 0, 'List must not include empty strings'

    found_options = []
    out = None

    for inp_check in lst:
        #print(inp_check)
        if inp_check.startswith(inp):
            found_options.append(inp_check)
    if len(found_options) == 0:
        if verb: print("Your answer does not fit to any option. Please select one of these: {}.".format(", ".join("'" + o + "'" for o in lst)))
    elif len(found_options) == 1:
        out = found_options[0]
        if verb: print("OK, you have chosen '{}'.".format(out))
    else:
        if verb: print("Your answer fits to multiple options ({}). Please try again.".format(", ".join("'" + o + "'"  for o in found_options)))
    return out
