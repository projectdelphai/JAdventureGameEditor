#! /usr/bin/python

import json
import matplotlib.pyplot as plt

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
        file_name = "json/locations.json"
        print("1. Locations")
        print("2. Show Locations")
        item = input("What do you want to do?: ")
        if item == "1":
            data = load_json(file_name)
            current_position = get_current_position(data)
            neighbors = get_neighbors(current_position,data)
            intro(current_position,neighbors)
            action(current_position,data,file_name)
        if item == "2":
            z = input("What level do you want to show?: ")
            plot_locations(file_name,z)
        if item == "exit":
            break;

def plot_locations(file_name,z):
    data = load_json(file_name)
    underground = []
    aboveground = []
    for full_coordinate in data.keys():
        full_coordinate = full_coordinate.split(",")
        if full_coordinate[2] == "-1":
            coordinate = [ full_coordinate[0], full_coordinate[1] ]
            underground.append(coordinate)
        else:
            coordinate = [ full_coordinate[0], full_coordinate[1] ]
            aboveground.append(coordinate)
    if z == "-1":
        for (x, y) in underground:
            plt.plot(x, y, 'bo-')
    else:
        for (x, y) in aboveground:
            plt.plot(x, y, 'bo-')
    plt.grid(True)
    plt.autoscale(True)
    plt.show()

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
            return data
        except:
            None
    elif (direction == "s"):
        new_coordinate = "%s,%s,%s" % (x,str(int(y)-1),z)
        try:
            new_position = data.get("%s,%s,%s" % (x,str(int(y)-1),z)).get("title")
            return data
        except:
            None
    elif (direction == "e"):
        new_coordinate = "%s,%s,%s" %  (str(int(x)+1),y,z)
        try: 
            new_position = data.get("%s,%s,%s" %  (str(int(x)+1),y,z)).get("title")
            return data
        except:
            None
    elif (direction == "w"):
        new_coordinate = "%s,%s,%s" %  (str(int(x)-1),y,z)
        try: 
            new_position = data.get("%s,%s,%s" %  (str(int(x)-1),y,z)).get("title")
            return data
        except:
            None
    title = input("What is the tile's title?: ")
    description = input("What is the tile's description?: ")
    location_type = input("What is the tile's locationType?: ")
    danger_rating = input("What is the tiles's dangerRating?: ")
    items = [] 
    item = input("Add item to the tile? (Leave blank for no items) ")
    while item.strip() != "": 
        items.append(item)
        item = input("Add item to the tile? (Leave blank for no more items) ")
    if (len(items) != 0):
        new_data = { "coordinate" : new_coordinate, "title" : title, "description" : description, "locationType" : location_type, "danger": danger_rating, "items": items}
    else:
        new_data = { "coordinate" : new_coordinate, "title" : title, "description" : description, "locationType" : location_type, "danger": danger_rating }
    data[new_coordinate] = new_data
    return data

def deletetile(current_position,data,direction):
    coordinate = current_position.get("coordinate").split(',')
    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    if (direction == "n"):
        new_coordinate = "%s,%s,%s" % (x,str(int(y)+1),z)
        try:
            new_position = data.get("%s,%s,%s" % (x,str(int(y)+1),z)).get("title")
        except:
            return data
    elif (direction == "s"):
        new_coordinate = "%s,%s,%s" % (x,str(int(y)-1),z)
        try:
            new_position = data.get("%s,%s,%s" % (x,str(int(y)-1),z)).get("title")
        except:
            return data
    elif (direction == "e"):
        new_coordinate = "%s,%s,%s" %  (str(int(x)+1),y,z)
        try: 
            new_position = data.get("%s,%s,%s" %  (str(int(x)+1),y,z)).get("title")
        except:
            return data
    elif (direction == "w"):
        new_coordinate = "%s,%s,%s" %  (str(int(x)-1),y,z)
        try: 
            new_position = data.get("%s,%s,%s" %  (str(int(x)-1),y,z)).get("title")
        except:
            return data
    del data[new_coordinate]
    return data



def action(current_position,data,filename):
    while True:
        next_action = input("\nWhat do you want to do?: ")
        if (next_action.startswith("g")):
            direction = next_action[1:]
            if direction in ["n", "s", "e", "w"]:
                current_position = go(direction,current_position,data)
                neighbors = get_neighbors(current_position,data)
                intro(current_position,neighbors)
            else:
                print("Not a valid direction")
        elif (next_action.startswith("c")):
            direction = next_action[1:]
            if direction in ["n", "s", "e", "w"]:
                data = createtile(current_position,data,direction)
                write_json(data,filename)
                neighbors = get_neighbors(current_position,data)
                intro(current_position,neighbors)
            else:
                print("Not a valid direction")
        elif (next_action.startswith("d")):
            direction = next_action[1:]
            if direction in ["n", "s", "e", "w"]:
                data = deletetile(current_position,data,direction)
                write_json(data,filename)
                neighbors = get_neighbors(current_position,data)
                intro(current_position,neighbors)
            else:
                print("Not a valid direction")
        elif (next_action.startswith("t")):
            current_position = get_current_position(data)
            neighbors = get_neighbors(current_position,data)
            intro(current_position,neighbors)
        elif (next_action.startswith("exit")):
            break;
menu()
