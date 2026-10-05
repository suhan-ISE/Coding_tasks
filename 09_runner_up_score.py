# Task 9: Runner-Up Score
# Find the second-highest distinct score without using sort() or sorted().

scores = list(map(int, input("Enter scores separated by spaces: ").split()))

unique_scores = set(scores)

if len(unique_scores) < 2:
    print("At least two different scores are required.")
else:
    highest = max(unique_scores)
    unique_scores.remove(highest)
    second_highest = max(unique_scores)
    print("Second-highest score:", second_highest)
