# Case Study: Multi-Event Sports Scheduling and Scoring

## 1. Problem statement

Develop a Python program to manage multiple sports events using lists and tuples. The program should store event schedules and team scores, identify scheduling conflicts when a team is assigned to overlapping events, calculate total points earned by each team, and generate final rankings based on their total scores.

## 2. Sample rules

- Each event has an event name, start time, end time, and participating teams.
- A team cannot participate in two events that overlap in time.
- Winning team: 3 points.
- Runner-up: 2 points.
- Participation: 1 point.
- Teams are ranked by total points in descending order.
- Teams with equal points share the same rank.

## 3. Algorithm

1. Start.
2. Input the number of sports events.
3. Store each event's name, start time, end time, and team results using tuples and lists.
4. Compare event schedules to identify overlapping events involving the same team.
5. Assign points to each team according to its position in each event.
6. Calculate the total points for every team.
7. Sort teams by total points in descending order.
8. Assign ranks, giving equal ranks to teams with equal scores.
9. Display scheduling conflicts, total points, and final rankings.
10. Stop.

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[Store event schedules and team results]
    B --> C[Compare event time intervals]
    C --> D{Same team in overlapping events?}
    D -- Yes --> E[Report scheduling conflict]
    D -- No --> F[Calculate team points]
    E --> F
    F --> G[Aggregate points for all teams]
    G --> H[Sort teams by total points]
    H --> I[Assign ranks]
    I --> J[Display conflicts and rankings]
    J --> K([Stop])

```

## 6. Sample output

```
----- SCHEDULING CONFLICTS -----
Team A has a conflict between Football and Basketball
Team A has a conflict between Football and Badminton

----- FINAL TEAM RANKINGS -----
Rank: 1 | Team: Team C | Total points: 5
Rank: 1 | Team: Team A | Total points: 5
Rank: 3 | Team: Team B | Total points: 5
```

Correction to the sample ranking: with the listed event results, Team A has 5 points, Team B has 5 points, and Team C has 5 points. Therefore, all three teams should share Rank 1. The program correctly handles tied scores.

## 7. Test cases

| Test case                             | Expected result                 |
| ------------------------------------- | ------------------------------- |
| Same team in overlapping events       | Scheduling conflict detected    |
| Different teams in overlapping events | No team conflict                |
| Events occur one after another        | No conflict                     |
| Team wins an event                    | 3 points added                  |
| Team finishes runner-up               | 2 points added                  |
| Two teams have equal totals           | Same rank assigned              |
| Team participates in several events   | Points aggregated across events |

## 8. Conclusion

This program demonstrates Python lists, tuples, dictionaries, sets, loops, conditional statements, and sorting. It can identify overlapping schedules for teams, aggregate scores across events, and generate final rankings with ties handled correctly.
