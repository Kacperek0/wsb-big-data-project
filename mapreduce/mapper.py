#!/usr/bin/env python3

import sys

def get_victim_type(victims):

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

    return injury_type

def map():

    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')

        try:
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

            sum_injured = victims['pedestrians_injured'] + \
                victims['motorist_injured'] + victims['pedestrians_injured']
            sum_killed = victims['pedestrians_killed'] + \
                victims['cyclists_killed'] + victims['motorist_killed']

            injury_types = (sum_injured, sum_killed)
            injury = get_injury_type(injury_types)

            zip_code = int(line[2])
            if zip_code > 0 and int(date[2]) > 2012:
                for item in incident_street:
                    for person in victim_type:
                        for type in injury:
                            if type == 'injured':
                                number_of_victims = sum_injured
                            elif type == 'killed':
                                number_of_victims = sum_killed
                            print(
                                f'{item},{zip_code},{person},{type}\t{number_of_victims}')
        except ValueError:
            continue

if __name__ == '__main__':
    map()
