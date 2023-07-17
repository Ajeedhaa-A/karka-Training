per_details=[{"name":"Supri","Age":20,"Place":"Ganeshapuram"},{"name":"valli","Age":22,"Place":"Krishnankovil"},{"name":"Abi","Age":23,"Place":"Vattavalai"},{"name":"aji","Age":21,"Place":"Kanankulam"}]
def abv_age():
    for i in range (len(per_details)):
        if (per_details[i]["Age"])>21:
             print("name:{}  Place:{}".format(per_details[i]["name"],per_details[i]["Place"]))
abv_age()