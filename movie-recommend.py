import math
Genre = ("Action" , "Comedy", "Horror")  #immutable tuple of genres 
#watched 
# Action comedy horror
Avenger = [8,6,2]
Dark_knight = [7,4,3]
Conjuring = [5,1,9]
#watched


#Avenger #Dark_knight #Conjuring
User_liking = [8,7,3] #extracted sentiment from reviews 
Pos_Action = (User_liking[0]*Avenger[0] + User_liking[1]*Dark_knight[0] + User_liking[2]*Conjuring[0])/sum(User_liking)
Pos_Comedy = (User_liking[0]*Avenger[1] + User_liking[1]*Dark_knight[1] + User_liking[2]*Conjuring[1])/sum(User_liking)
Pos_Horror = (User_liking[0]*Avenger[2] + User_liking[1]*Dark_knight[2] + User_liking[2]*Conjuring[2])/sum(User_liking)

User_position = [Pos_Action, Pos_Comedy, Pos_Horror]
c = 0
for i in range(len(User_position)):
    c +=1
    print("Position of " + Genre[i] + " is " + str(User_position[i]))

#not watched     
Lucy = [7,3,5]
parasite = [3,2,6]
tenet = [8,4,3]
paranormal = [3,1,9]
#not watched 


pA = User_position[0]
pC = User_position[1]
pH = User_position[2]


d_lucy = math.sqrt(((Lucy[0]-pA)**2) + ((Lucy[1]-pC)**2) + (Lucy[2]-pH)**2)
d_parasite = math.sqrt(((parasite[0]-pA)**2) + ((parasite[1]-pC)**2) + (parasite[2]-pH)**2)
d_tenet = math.sqrt(((tenet[0]-pA)**2) + ((tenet[1]-pC)**2) + (tenet[2]-pH)**2)
d_paranormal = math.sqrt(((paranormal[0]-pA)**2) + ((paranormal[1]-pC)**2) + (paranormal[2]-pH)**2)

#distances from the user 
print("distance from lucy: " +  str(d_lucy))
print("distance from parasite: " + str(d_parasite))
print("distance from tenet: "  + str(d_tenet))
print("distance from paranormal: " + str(d_paranormal))
#distances from the user 

Set_notwatched = {
    "Lucy": d_lucy,
    "Parasite": d_parasite,
    "Tenet": d_tenet,
    "Paranormal": d_paranormal}

the_names = list(Set_notwatched.keys())
the_distance = [d_lucy, d_parasite, d_tenet, d_paranormal]
to_recommend = min(the_distance)
pos = the_distance.index(to_recommend)
MOVIE_NAME = the_names[pos] 

print("I would like to recommend to you: " + MOVIE_NAME)
