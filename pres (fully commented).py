# Function to parse a single instruction
def parse_instruction(instruction):
    # Define the actions and initialize a dictionary to store the details
    actions = ['Chop', 'Mix', 'Bake', 'Add', 'Stir', 'Cook', 'Boil', 'Fry', 'Grill', 'Roast', 'Steam', 'Divide', 'Toast', 'Assemble', 'Preheat', 'Saute', 'Simmer', 'Marinate', 'Whisk', 'Knead', 'Blend', 'Drizzle', 'Garnish', 'Melt', 'Peel', 'Dice', 'Mince']
    details = {action: [] for action in actions}  # Initialize a dictionary with each action as a key and an empty list as a value

    # Function to convert fractions into decimals
    def convert_fraction(fraction):
        try:
            numerator, denominator = fraction.split('/')  # Split the fraction into numerator and denominator
            result = float(numerator) / float(denominator)  # Divide the numerator by the denominator to get the decimal
            return str(int(result)) if result.is_integer() else str(result)  # If the result is an integer, return it as an integer, otherwise return it as a float
        except ValueError:
            return fraction  # If the fraction can't be split into a numerator and a denominator, return it as is

    # Convert all fractions in the instruction
    instruction = ' '.join(convert_fraction(word) if '/' in word else word for word in instruction.split(' '))  # Split the instruction into words, convert each word that contains a '/' into a decimal using the convert_fraction function, and then join the words back together

    # Split the instruction into sentences and iterate over each sentence
    sentences = instruction.split('. ')
    for sentence in sentences:
        words = sentence.split(' ')  # Split the sentence into words
        action = words[0]  # The first word is the action

        # Check if the action is in the list of actions
        if action in actions:
            try:
                # Handle different actions
                if action in ['Chop', 'Add', 'Saute', 'Simmer', 'Marinate', 'Whisk', 'Knead', 'Blend', 'Drizzle', 'Garnish', 'Melt', 'Peel', 'Dice', 'Mince']:
                    # Check if the first word after the action is a number
                    if words[1].replace('.', '', 1).isdigit():
                        quantity = float(words[1])  # Convert the quantity to a float
                        quantity = int(quantity) if quantity.is_integer() else quantity  # If the quantity is an integer, convert it to an integer
                        details[action].append(f"{quantity} {' '.join(words[2:])}")  # Append the quantity and the rest of the words after the action to the list of details for the action
                    else:
                        details[action].append(' '.join(words[1:]))  # If the first word after the action is not a number, append all the words after the action to the list of details for the action
                elif action == 'Mix':
                    items = ' '.join(words[1:]).split(', ')  # Join all the words after the action into a string and split it into items at each comma
                    for item in items:
                        parts = item.split(' ')  # Split each item into parts
                        if parts[0].replace('.', '', 1).isdigit():
                            quantity = float(parts[0])  # Convert the quantity to a float
                            quantity = int(quantity) if quantity.is_integer() else quantity  # If the quantity is an integer, convert it to an integer
                            details[action].append(f"{quantity} {' '.join(parts[1:])}")  # Append the quantity and the rest of the parts to the list of details for the action
                        else:
                            details[action].append(item)  # If the first part is not a number, append the item to the list of details for the action
                elif action == 'Bake':
                    temp_details = ' '.join(words[1:]).split(' for ')  # Join all the words after the action into a string and split it into temperature details at ' for '
                    temp_parts = temp_details[0].split(' ')  # Split the first part of the temperature details into parts
                    if temp_parts[0].replace('.', '', 1).isdigit():
                        temp = float(temp_parts[0])  # Convert the temperature to a float
                        temp = int(temp) if temp.is_integer() else temp  # If the temperature is an integer, convert it to an integer
                        details[action].append(f"at {temp} degrees")  # Append the temperature to the list of details for the action
                    else:
                        details[action].append(temp_details[0])  # If the first part of the temperature details is not a number, append it to the list of details for the action
                    time_parts = temp_details[1].split(' ')  # Split the second part of the temperature details into parts
                    if time_parts[0].replace('.', '', 1).isdigit():
                        time = float(time_parts[0])  # Convert the time to a float
                        time = int(time) if time.is_integer() else time  # If the time is an integer, convert it to an integer
                        details[action].append(f"for {time} minutes")  # Append the time to the list of details for the action
                    else:
                        details[action].append(temp_details[1])  # If the first part of the time details is not a number, append it to the list of details for the action
                elif action == 'Preheat':
                    appliance, *temp = words[1:]  # The first word after the action is the appliance and the rest of the words are the temperature
                    details[action].append(f"{appliance} to {' '.join(temp)}")  # Append the appliance and temperature to the list of details for the action
                else:
                    details[action].append(' '.join(words[1:]))  # If the action is not in the list of actions, append all the words after the action to the list of details for the action
            except ValueError:
                print(f"Error: Invalid value in '{sentence}'. Please check your input.")  # Print an error message if a value can't be converted to a float or an integer
                return None
        else:
            print(f"Error: Unknown action '{action}' in '{sentence}'. Please check your input.")  # Print an error message if the action is not in the list of actions
            return None
    return details  # Return the dictionary of details

# Define a function to print the output
def print_output(details):
    # If the details are not None
    if details is not None:
        # Iterate over each action and its items
        for action, items in details.items():
            # If there are items for the action
            if items:
                # Print the action
                print(action + ':')
                # Iterate over each item
                for item in items:
                    # Print the item
                    print('  - ' + item)

def parse_recipe():
    # Ask the user to enter a cooking recipe
    recipe = input("Enter your cooking recipe: ")
    # Split the recipe into instructions
    instructions = recipe.split('. ')
    # Iterate over each instruction
    for instruction in instructions:
        # Parse the instruction
        details = parse_instruction(instruction)
        # Print the output
        print_output(details)

# Call the function to start parsing the recipe
parse_recipe()