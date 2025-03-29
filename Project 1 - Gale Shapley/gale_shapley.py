def gale_shapley(intern_prefs, position_prefs):
    # Number of interns/positions
    n = len(intern_prefs)

    # Initialize all positions as unmatched
    unmatched_positions = list(range(n))
    intern_matches = [-1] * n # Intern to position matches
    position_proposals = [0] * n # Track which intern each position will propose to next

    while unmatched_positions:
        # Pick an unmatched position
        position = unmatched_positions[0]

        # Propose to the next intern on the position's preference list
        intern = position_prefs[position][position_proposals[position]]
        position_proposals[position] += 1

        if intern_matches[intern] == -1: # If intern is unmatched
            intern_matches[intern] = position
            unmatched_positions.pop(0)
        else:
            # Check if the intern prefers this new position
            current_position = intern_matches[intern]
            if intern_prefs[intern].index(position) < intern_prefs[intern].index(current_position):
                # Update the match
                intern_matches[intern] = position
                unmatched_positions.pop(0)
                unmatched_positions.append(current_position) # The current position is now unmatched
    # Create a mapping of position-to-intern
    result = {intern: position for intern, position in enumerate(intern_matches)}
    return result


intern_preferences = [
    [2, 3, 1, 0], # Intern 1
    [1, 0, 3, 2], # Intern 2
    [0, 1, 2, 3], # Intern 3
    [3, 2, 0, 1] # Intern 4
]

position_preferences = [
    [3, 1, 2, 0], # Position 1
    [2, 3, 0, 1], # Position 2
    [0, 2, 1, 3], # Position 3
    [1, 0, 3, 2] # Position 4
]

matches = gale_shapley(intern_preferences, position_preferences)
print(matches)
