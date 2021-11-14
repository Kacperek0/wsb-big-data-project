import json
import sys
import pandas as pd

# path = sys.argv[1]
path = 'NYPD_full.csv'

def get_victim_type(victims):
    # DONE: what if various type?
    victim_type = []
    pedestrians = victims['pedestrians_injured'] + victims['pedestrians_killed']
    cyclists = victims['cyclists_injured'] + victims['cyclists_killed']
    motorists = victims['motorist_injured'] + victims['motorist_killed']

    if pedestrians > 0:
        victim_type.append('pedestrian')
    elif cyclists > 0:
        victim_type.append('cyclist')
    elif motorists > 0:
        victim_type.append('motorist')
    # TODO: check if for sure!
    # else:
    #     victim_type.append('none')

    return victim_type

def get_steet_name(streets):
    street = []
    for item in streets:
        if type(item) == str:
            street.append(item)

    return street

def get_injury_type(injury_types):
    injury_type = []
    if injury_types[0] > 0:
        injury_type.append('injured')
    elif injury_types[1] > 0:
        injury_type.append('killed')
    # TODO: check if for sure!
    # else:
    #     injury_type.append('none')

    return injury_type

def map():
    df = pd.read_csv(path)

    for count in df.index:

        victims = {
            'pedestrians_injured': int(df['NUMBER OF PEDESTRIANS INJURED'][count]),
            'pedestrians_killed': int(df['NUMBER OF PEDESTRIANS KILLED'][count]),
            'cyclists_injured': int(df['NUMBER OF CYCLIST INJURED'][count]),
            'cyclists_killed': int(df['NUMBER OF CYCLIST KILLED'][count]),
            'motorist_injured': int(df['NUMBER OF MOTORIST INJURED'][count]),
            'motorist_killed': int(df['NUMBER OF MOTORIST KILLED'][count])
        }

        streets = (df['ON STREET NAME'][count],
                   df['CROSS STREET NAME'][count],
                   df['OFF STREET NAME'][count])

        incident_street = get_steet_name(streets)
        date = df['DATE'][count].split('/')

        victim_type = get_victim_type(victims)

        injury_types = (int(df['NUMBER OF PERSONS INJURED'][count]),
                        int(df['NUMBER OF PERSONS KILLED'][count]))
        injury = get_injury_type(injury_types)

        zip_code = df['ZIP CODE'][count]
        if zip_code > 0 and int(date[2]) > 2012:
            for item in incident_street:
                for person in victim_type:
                    for type in injury:
                        if type == 'injured':
                            number_of_victims = injury_types[0]
                        elif type == 'killed':
                            number_of_victims = injury_types[1]
                        print(f'{item}, {zip_code}, {person}, {type}: {number_of_victims}')

if __name__ == '__main__':
    map()
