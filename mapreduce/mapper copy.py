import json
import sys
import pandas as pd

# path = sys.argv[1]
path = 'NYPD_Motor_Vehicle_Collisions.csv'

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
        if item:
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

    with open(path, 'r') as f:
        first_line = f.readline()
        first_line = first_line.split(',')
        for line in f:
            line = line.strip()
            line = line.split(',')

            victims = {
                'pedestrians_injured': int(line[11]),
                'pedestrians_killed': int(line[12]),
                'cyclists_injured': int(line[13]),
                'cyclists_killed': int(line[14]),
                'motorist_injured': int(line[15]),
                'motorist_killed': int(line[16])
            }

            streets = (line[6], line[7], line[8])

            incident_street = get_steet_name(streets)
            date = line[0].split('/')

            victim_type = get_victim_type(victims)

            injury_types = (int(line[9]),
                            int(line[10]))
            injury = get_injury_type(injury_types)

            zip_code = line[2]
            if zip_code and int(date[2]) > 2012:
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
