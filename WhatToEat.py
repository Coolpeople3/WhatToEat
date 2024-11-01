import json

# File to store food ideas
FILE_NAME = "food_ideas.json"


# Load food ideas from file, or create a new list if the file doesn't exist
def load_food_ideas():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save food ideas to file
def save_food_ideas(ideas):
    with open(FILE_NAME, "w") as file:
        json.dump(ideas, file)


# Add a new food idea to the list
def input_new_food_idea():
    name = input("Enter the name of the food: ")
    time_required = int(input("Enter the time required to make it (in minutes): "))
    ideas = load_food_ideas()
    ideas.append({"name": name, "time_required": time_required})
    save_food_ideas(ideas)
    print(f"Food idea '{name}' added!")


# List food ideas within the time range
def list_food_ideas_within_range():
    time_available = int(input("Enter the amount of time you have (in minutes): "))
    ideas = load_food_ideas()

    # Print all ideas to confirm they're being loaded
    #print("Loaded food ideas:", ideas)

    # Filter food ideas within the time range
    matching_ideas = [
        idea for idea in ideas if abs(idea["time_required"] - time_available) <= 15
    ]

    if matching_ideas:
        print("Here are the food ideas you can make within your time range:")
        for idea in matching_ideas:
            print(f"- {idea['name']} (takes {idea['time_required']} minutes)")
    else:
        print("No matching food ideas found within your time range.")


# Main menu loop
def main():
    try:
        while True:
            print("\n--- Food Idea Generator ---")
            print("1. Input new food idea")
            print("2. List food ideas within time range")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                input_new_food_idea()
            elif choice == "2":
                list_food_ideas_within_range()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")  # Keep the window open until the user presses Enter
