from itertools import combinations
import pandas as pd


def pair_numbers(numbers):
  pairs = []
  for i in range(len(numbers)):
    for j in range(len(numbers)):
      if i != j:
        pairs.append((numbers[i], numbers[j]))
  return pairs


def combinations_creator(team):
    names=[]
    all_teams=[]
    for item in team:
      names.append(item)
    pairs = pair_numbers(names)
    for pair in pairs:
      for player in team:
        if player not in pair:
          pair=list(pair)
          pair.append(player)
      all_teams.append(pair)
    return all_teams 



def sort_dict_list(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])


def randomness_calc(unique_teams,df): 
    randomness=[]
    totals=[]
    dict_team = {}

    for idx, team in enumerate(unique_teams, start=1):
        print(f"Team {idx}:")
        randomness_team = 0
        randomity=0
        for player in team:
            df.loc[player.Index,"no_team"] +=1
            #print(df.loc[player.Index,:])
            #print(player.Name, player.Team, player.Position, player.Points,df.loc[player.Index,"Number_Teams"])
            randomness_team = randomness_team + player.points*df.loc[player.Index,"no_team"]
            randomity *=df.loc[player.Index,"no_team"]
        #print("Total Points:", sum(player.Points for player in team))
        totals.append(sum(player.points for player in team))
        #print("Randomness:",sum(player.Points for player in team)*randomness_team*(1-((randomity/(len(unique_teams)*10))*(randomity/(len(unique_teams)*10)))))
        randomness.append(sum(player.points for player in team)*randomness_team*(1-((randomity/(len(unique_teams)*10))*(randomity/(len(unique_teams)*10)))))
    
    all_teams=[]
    dict_team={}
    for i in range(len(totals)):
        dict_team={ "team":i+1 , "Total":totals[i] , "randomness_value":randomness[i]}
        all_teams.append(dict_team) 

    final_teams= [] 
    df['storage']=df['no_team']
    sorted_dict_list = sort_dict_list(all_teams, 'randomness_value')
    for i in sorted_dict_list[:200]:
        #print(i)
        for idx, team in enumerate(unique_teams, start=1):
            if i['team'] == idx :
                print(f"Team {idx}:")
                final_teams.append(team)
                for player in team:
                    df.loc[player.Index,"no_team"] -=1 
    print(final_teams)
    return final_teams

def fixed_structure(df):
    max_total_points = 100
    max_players_per_position = {
        "Batsman": 4,
        "Bowler": 4,
        "WicketKeeper": 1,
        "AllRounder": 2
    }

# Generate unique teams
    unique_teams = set()
    for r in range(11, len(df) + 1):
        for team_combination in combinations(df.itertuples(), r):
            team_points = 0
            team_positions_count = {"Batsman": 0, "Bowler": 0, "WicketKeeper": 0, "AllRounder": 0}
            valid_team = []
            for player in team_combination:
                if team_positions_count[player.position] < max_players_per_position[player.position]:
                    valid_team.append(player)
                    team_points += player.points
                    #df['Number_Teams'][player.Index]=df['Number_Teams'][player.Index]+1
                    #print(row_id)
                    team_positions_count[player.position] += 1
            if 90<= team_points <= max_total_points and len(valid_team) == 11:
                unique_teams.add(tuple(sorted(valid_team, key=lambda x: x.name)))
    print("Number of teams: ",len(unique_teams)) 
    randomness_calc(unique_teams,df)


   
  
    
def create_df(team1,team2):
    player_data=[]
    for player in team1: 
       player_data.append(vars(player))
    for player in team2:
       player_data.append(vars(player))

    df = pd.DataFrame(player_data)
    print(df)
    fixed_structure(df)