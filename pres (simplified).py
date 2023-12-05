# Function to parse a single instruction
def parse_instruction(instruction):
    # Define the actions and initialize a dictionary to store the details
    actions = ['Chop', 'Mix', 'Bake', 'Add', 'Stir', 'Cook', 'Boil', 'Fry', 'Grill', 'Roast', 'Steam', 'Divide', 'Toast', 'Assemble', 'Preheat', 'Saute', 'Simmer', 'Marinate', 'Whisk', 'Knead', 'Blend', 'Drizzle', 'Garnish', 'Melt', 'Peel', 'Dice', 'Mince']
    details = {action: [] for action in actions}

    # Function to convert fractions into decimals
    def convert_fraction(fraction):
        try:
            numerator, denominator = fraction.split('/')
            result = float(numerator) / float(denominator)
            return str(int(result)) if result.is_integer() else str(result)
        except ValueError:
            return fraction

    # Convert all fractions in the instruction
    instruction = ' '.join(convert_fraction(word) if '/' in word else word for word in instruction.split(' '))

    # Split the instruction into sentences and iterate over each sentence
    sentences = instruction.split('. ')
    for sentence in sentences:
        words = sentence.split(' ')
        action = words[0]

        # Check if the action is in the list of actions
        if action in actions:
            try:
                # Handle different actions
                if action in ['Chop', 'Add', 'Saute', 'Simmer', 'Marinate', 'Whisk', 'Knead', 'Blend', 'Drizzle', 'Garnish', 'Melt', 'Peel', 'Dice', 'Mince']:
                    # Check if the first word after the action is a number
                    if words[1].replace('.', '', 1).isdigit():
                        quantity = float(words[1])
                        quantity = int(quantity) if quantity.is_integer() else quantity
                        details[action].append(f"{quantity} {' '.join(words[2:])}")
                    else:
                        details[action].append(' '.join(words[1:]))
                elif action == 'Mix':
                    items = ' '.join(words[1:]).split(', ')
                    for item in items:
                        parts = item.split(' ')
                        if parts[0].replace('.', '', 1).isdigit():
                            quantity = float(parts[0])
                            quantity = int(quantity) if quantity.is_integer() else quantity
                            details[action].append(f"{quantity} {' '.join(parts[1:])}")
                        else:
                            details[action].append(item)
                elif action == 'Bake':
                    temp_details = ' '.join(words[1:]).split(' for ')
                    temp_parts = temp_details[0].split(' ')
                    if temp_parts[0].replace('.', '', 1).isdigit():
                        temp = float(temp_parts[0])
                        temp = int(temp) if temp.is_integer() else temp
                        details[action].append(f"at {temp} degrees")
                    else:
                        details[action].append(temp_details[0])
                    time_parts = temp_details[1].split(' ')
                    if time_parts[0].replace('.', '', 1).isdigit():
                        time = float(time_parts[0])
                        time = int(time) if time.is_integer() else time
                        details[action].append(f"for {time} minutes")
                    else:
                        details[action].append(temp_details[1])
                elif action == 'Preheat':
                    appliance, *temp = words[1:]
                    details[action].append(f"{appliance} to {' '.join(temp)}")
                else:
                    details[action].append(' '.join(words[1:]))
            except ValueError:
                print(f"Error: Invalid value in '{sentence}'. Please check your input.")
                return None
        else:
            print(f"Error: Unknown action '{action}' in '{sentence}'. Please check your input.")
            return None
    return details

# Function to print the output
def print_output(details):
    if details is not None:
        for action, items in details.items():
            if items:
                print(action + ':')
                for item in items:
                    print('  - ' + item)

# Function to parse a whole recipe
def parse_recipe():
    # Get the recipe from the user
    recipe = input("Enter your cooking recipe: ")
    # Split the recipe into individual instructions
    instructions = recipe.split('. ')
    # Parse each instruction and print the output
    for instruction in instructions:
        details = parse_instruction(instruction)
        print_output(details)

# Call the function to start parsing the recipe
parse_recipe()