def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""

    while unprinted_designs:
        current_printing = unprinted_designs.pop()
        print(f'Printing model: {current_printing}')
        completed_models.append(current_printing)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    
    print('\nThe following models have been printed:')

    for model in completed_models:
        print(model)

