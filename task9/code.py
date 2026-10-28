
# Multi-Event Sports Scheduling and Scoring

# Event format:
# (event_name, start_time, end_time, results)
# Each result is a tuple: (team_name, position)
# Times are represented as hours, e.g. 9 = 9 AM.

events = [
    ("Football", 9, 11, [("Team A", 1), ("Team B", 2)]),
    ("Basketball", 10, 12, [("Team A", 2), ("Team C", 1)]),
    ("Volleyball", 12, 14, [("Team B", 1), ("Team C", 2)]),
    ("Badminton", 9, 10, [("Team A", 1), ("Team C", 2)])
]

points_table = {1: 3, 2: 2, 3: 1}
scores = {}
conflicts = []

# Identify scheduling conflicts
for i in range(len(events)):
    for j in range(i + 1, len(events)):
        event1 = events[i]
        event2 = events[j]

        # Check whether event times overlap
        if event1[1] < event2[2] and event2[1] < event1[2]:

            teams1 = [team for team, position in event1[3]]
            teams2 = [team for team, position in event2[3]]

            common_teams = set(teams1) & set(teams2)

            for team in common_teams:
                conflicts.append(
                    (team, event1[0], event2[0])
                )

# Calculate total points
for event in events:
    for team, position in event[3]:
        points = points_table.get(position, 0)

        if team not in scores:
            scores[team] = 0

        scores[team] += points

# Display scheduling conflicts
print("----- SCHEDULING CONFLICTS -----")

if len(conflicts) == 0:
    print("No scheduling conflicts found.")
else:
    for team, event1, event2 in conflicts:
        print(
            team, "has a conflict between",
            event1, "and", event2
        )

# Sort teams by score in descending order
ranking = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)

# Display final rankings
print("\n----- FINAL TEAM RANKINGS -----")

rank = 0
previous_score = None

for position, (team, total) in enumerate(ranking, start=1):
    if total != previous_score:
        rank = position

    print(
        "Rank:", rank,
        "| Team:", team,
        "| Total points:", total
    )

    previous_score = total

