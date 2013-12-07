#! /usr/bin/python

import json

def load_json(filename):
    with open(filename, 'r') as f:
        raw_json_data = f.read()
    json_data = json.loads(raw_json_data)
    return json_data

def write_json(data,filename):
    with open(filename,'w') as f:
        f.write(json.dumps(data, f))

def menu():
    while True:
        print("1. Locations")
        item = input("What do you want to edit: ")
        if item == "1":
            return "json/locations.json"

def get_current_position(data):
    while True:
        try:
            raw_coordinate = input("What is your current position?: ")
            coordinate = data.get(raw_coordinate)
            title = coordinate.get("title")
        except:
            print("Coordinate doesn't exist")
            continue
        break
    return coordinate

def get_neighbors(current_position,data):
    coordinate = current_position.get("coordinate").split(',')
    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    north = data.get("%s,%s,%s" % (x,str(int(y)+1),z))
    south = data.get("%s,%s,%s" % (x,str(int(y)-1),z))
    east = data.get("%s,%s,%s" %  (str(int(x)+1),y,z))
    west = data.get("%s,%s,%s" %  (str(int(x)-1),y,z))
    return [north,south,east,west]

def intro(current_position,neighbors):
    print("%s: %s" % (current_position.get("title"),current_position.get("description")))
    try:
        print("North - %s: %s" % (neighbors[0].get("title"),neighbors[0].get("description")))
    except:
        None
    try:
        print("South - %s: %s" % (neighbors[1].get("title"),neighbors[1].get("description")))
    except:
        None
    try:
        print("East - %s: %s" % (neighbors[2].get("title"),neighbors[2].get("description")))
    except:
        None
    try:
        print("West - %s: %s" % (neighbors[3].get("title"),neighbors[3].get("description")))
    except:
        None


def go(direction,current_position,data):
    coordinate = current_position.get("coordinate").split(',')
    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    if (direction == "n"):
        new_position = data.get("%s,%s,%s" % (x,str(int(y)+1),z))
    elif (direction == "s"):
        new_position = data.get("%s,%s,%s" % (x,str(int(y)-1),z))
    elif (direction == "e"):
        new_position = data.get("%s,%s,%s" %  (str(int(x)+1),y,z))
    elif (direction == "w"):
        new_position = data.get("%s,%s,%s" %  (str(int(x)-1),y,z))
    return new_position

def createtile(current_position,data,direction):
    coordinate = current_position.get("coordinate").split(',')
    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    if (direction == "n"):
        new_coordinate = "%s,%s,%s" % (x,str(int(y)+1),z)
        try:
            new_position = data.get("%s,%s,%s" % (x,str(int(y)+1),z)).get("title")
            return []
        except:
            None
    elif (direction == "s"):
        new_coordinate = "%s,%s,%s" % (x,str(int(y)-1),z)
        try:
            new_position = data.get("%s,%s,%s" % (x,str(int(y)-1),z)).get("title")
            return []
        except:
            None
    elif (direction == "e"):
        new_coordinate = "%s,%s,%s" %  (str(int(x)+1),y,z)
        try: 
            new_position = data.get("%s,%s,%s" %  (str(int(x)+1),y,z)).get("title")
            return []
        except:
            None
    elif (direction == "w"):
        new_coordinate = "%s,%s,%s" %  (str(int(x)-1),y,z)
        try: 
            new_position = data.get("%s,%s,%s" %  (str(int(x)-1),y,z)).get("title")
            return []
        except:
            None
    title = input("What is the tile's title?: ")
    description = input("What is the tile's description?: ")
    locationtype = input("What is the tile's locationType?: ")
    new_data = { "coordinate" : new_coordinate, "title" : title, "description" : description, "locationType" : locationtype }
    data[new_coordinate] = new_data
    return data

def action(current_position,data,filename):
    while True:
        next_action = input("What do you want to do?: ")
        if (next_action.startswith("m")):
            direction = next_action[1:]
            if direction in ["n", "s", "e", "w"]:
                current_position = go(direction,current_position,data)
                neighbors = get_neighbors(current_position,data)
                intro(current_position,neighbors)
            else:
                print("Not a valid directioN")
        elif (next_action.startswith("c")):
            direction = next_action[1:]
            if direction in ["n", "s", "e", "w"]:
                data = createtile(current_position,data,direction)
                write_json(data,filename)
                neighbors = get_neighbors(current_position,data)
                intro(current_position,neighbors)
            else:
                print("Not a valid direction")

def start():
    filename = menu()
    data = load_json(filename)
    current_position = get_current_position(data)
    neighbors = get_neighbors(current_position,data)
    intro(current_position,neighbors)
    action(current_position,data,filename)

start()
