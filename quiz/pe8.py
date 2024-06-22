###H24126078 鄭雅云
###統計116

import re
import csv


###第一題

def is_valid_record(record):
    return re.match(r'^\d+-\d+$', record) is not None

all_data = []
with open('pe8_data.csv', 'r') as file:
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

# Function to calculate win rate
def calculate_win_rate(wins, losses):
    return wins / (wins + losses)

# List to store teams with home win rate lower than away win rate
teams_with_lower_home_win_rate = []

# Iterate over all data rows
for data in all_data[1:]:  # Skip the header
    if data[0] == "Eastern":
        team = data[1]
        home_record = data[7]
        away_record = data[8]

        # Check if both home and away records are valid
        if is_valid_record(home_record) and is_valid_record(away_record): 
            home_wins, home_losses = map(int, home_record.split("-"))
            away_wins, away_losses = map(int, away_record.split("-"))

            home_win_rate = calculate_win_rate(home_wins, home_losses)
            away_win_rate = calculate_win_rate(away_wins, away_losses)

            if home_win_rate < away_win_rate:
                teams_with_lower_home_win_rate.append((team, home_win_rate, away_win_rate))

# Output the result
print()
print("Q1:")
for team in teams_with_lower_home_win_rate:
    print(f"Team: {team[0]}, Home Win Rate: {team[1]:.2f}, Away Win Rate: {team[2]:.2f}")


###第二題
all_data = []
with open('pe8_data.csv', 'r') as file:
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

# Initialize variables to store the sum and count of PF-PA differences for each conference
eastern_pf_pa_sum = 0
eastern_count = 0
western_pf_pa_sum = 0
western_count = 0

# Iterate over all data rows
for data in all_data[1:]:  # Skip the header
    if len(data) < 7:  ###因為有IndexError所以加這個
        continue
    
    conference = data[0]
    try:
        pf = float(data[5])
        pa = float(data[6])
    except ValueError:  ###預防如果不是小數
        continue
    
    pf_pa_difference = pf - pa

    if conference == "Eastern":
        eastern_pf_pa_sum += pf_pa_difference
        eastern_count += 1
    elif conference == "Western":
        western_pf_pa_sum += pf_pa_difference
        western_count += 1

eastern_avg_pf_pa = eastern_pf_pa_sum / eastern_count if eastern_count > 0 else 0
western_avg_pf_pa = western_pf_pa_sum / western_count if western_count > 0 else 0

print()
print("Q2:")
print(f"Eastern Conference Average PF-PA Difference: {eastern_avg_pf_pa:.2f}")
print(f"Western Conference Average PF-PA Difference: {western_avg_pf_pa:.2f}")
print("##So concluse:")

if eastern_avg_pf_pa > western_avg_pf_pa:
    print("Eastern Conference had a higher average PF-PA difference.")
elif western_avg_pf_pa > eastern_avg_pf_pa:
    print("Western Conference had a higher average PF-PA difference.")
else:
    print("Both conferences had the same average PF-PA difference.")



###第三題


# Function to read the CSV file and parse the data
def read_csv(file_path):
    all_data = []
    with open("pe8_data.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            all_data.append(row)
    return all_data

# Function to extract and sort teams based on winning percentage
def rank_teams_by_win_percentage(data):
    eastern_teams = []
    western_teams = []

    for team_data in data[1:]:  # Skip the header
        if len(team_data) < 4:  # Ensure there are enough columns
            continue

        conference = team_data[0]
        team = team_data[1]
        try:
            win_percentage = float(team_data[3])  # Extract win percentage
        except ValueError:
            continue

        if conference == "Eastern":
            eastern_teams.append((team, win_percentage))
        elif conference == "Western":
            western_teams.append((team, win_percentage))

    # Sort teams by win percentage in descending order
    eastern_teams_sorted = sorted(eastern_teams, key=lambda x: x[1], reverse=True)
    western_teams_sorted = sorted(western_teams, key=lambda x: x[1], reverse=True)

    return eastern_teams_sorted, western_teams_sorted

# Read data from the CSV file
file_path = '/mnt/data/pe8_data.csv'
all_data = read_csv(file_path)

# Rank teams based on win percentage
eastern_ranking, western_ranking = rank_teams_by_win_percentage(all_data)

# Output the ranking results
print()
print("Q3:")
for rank, (team, win_percentage) in enumerate(eastern_ranking, start=1):
    print(f"{rank}. {team} - {win_percentage:.3f} win percentage")

print("\nWestern Conference Ranking Based on Win Percentage:")
for rank, (team, win_percentage) in enumerate(western_ranking, start=1):
    print(f"{rank}. {team} - {win_percentage:.3f} win percentage")