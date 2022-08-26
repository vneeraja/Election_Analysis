#print("Hello World!")

#create a list of counties
counties = ["Arapahoe","Denver","Jefferson"]

# add a county to the list
counties.append("Harris")

print(counties)

# add a county to a specific location
counties.insert(1,"El Paso")

print(counties)

# remove a county based on name 
counties.remove("Denver")

print(counties)

# removal based on index
x = counties.pop(0)
print(x)
#print(counties)

counties[2] = "Denver"
print(counties)

my_dictionary = {"A":1,"B":2,"C":3}
print(my_dictionary)
x = my_dictionary.clear()
print(x)
print(my_dictionary)

voting_data = []
voting_data.append({"County":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(len(voting_data))
voting_data.insert(1,{"County":"El Paso", "registered_voters":461149})
#print(voting_data)
voting_data.pop(0)

x = voting_data.pop(1)
voting_data.append(x)
voting_data.append({"County":"Arapahoe", "registered_voters": 422829})
print(voting_data)


# temperature = input("what is the temperature outside?")
# print(temperature)

# if int(temperature) > 80:
#     print("Turn on the AC")
# else:
#     print("Open the windows")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# While loop
# x = 0
# while x <= 5:
#     print(x)
#     x = x+1

for county in counties:
    print(county)

for num in range(5):
    print(num)

# for i in len(counties):
#     print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county_key in counties_dict.keys():
    print(county_key)

for values in counties_dict.values():
    print(values)

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key + " county has "+ str(value) +" registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
    for voters in county_dict:
        print(county_dict["registered_voters"])
        #print(county_dict['registered voters'])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

for county,voters in counties_dict.items():
    print(f"The {county} has {voters} registered voters")


# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
    for county in counties_dict:
        print(f"{counties_dict['county']} county has registered voters")

