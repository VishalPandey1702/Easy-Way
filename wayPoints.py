# {location: "Old Bus Stand, Ghaziabad", stopover: true}
def wayPoints(waypoint):
    newStr = ""
    for i in waypoint:
        tempStr = "{{location: '{}', stopover: true}},\n".format(i)
        newStr+=tempStr
    return newStr
if __name__ == "__main__":
    print(wayPoints(["RKGIT","RDC","Ramleela"]))