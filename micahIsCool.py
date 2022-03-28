'''
if this was javascript
function poopMobile(array) {


    // This function takes in an array and lower all the elements in the array
    poopMobile = array.toLowerCase()


}


const poopMobile = (array) => {


    // This function takes in an array and lower all the elements in the array
    poopMobile = array.toLowerCase()
}

telnet localhost 3000

netcat

netstat
'''

# this function is  private. no one will EVER  SEE THIS. except kai and micah. they are the engineers on this project. LOCK THIS stuff DOWN.


def poopMobile(poopMobile):

    # This function takes in an array and lowercases all the elements in the array
    lowerCasepoopMobile = []

    print(
        f"Programming is weird. the length of this array is {len(poopMobile)}, but we stop at {len(poopMobile) - 1} when we use the range function.")

    for name in range(len(poopMobile)):
        # poopMobile[name] = poopMobile[name].lower()
        lowerCasepoopMobile.append(poopMobile[name].lower())
    print(f"poopMobile is still {poopMobile}")
    print(f"butttttt lowerCasepoopMobile is modified: {lowerCasepoopMobile}")
    return lowerCasepoopMobile


coolNames = ["Micah", "Kai", "Sayo", "Marisa",
             "Totti-Botti", "SuperAwesome", "coooollLLLLLLguy"]


print(poopMobile(coolNames))


#  lol this code is going on github. hopefully i dont lose my job.
