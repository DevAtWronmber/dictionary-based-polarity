# Takes Reviews and calculate the amount of emotion in it
# #! Imports pultchiksWheel

import numpy as np
from plutchiksWheel import *


emSet = [0, 0, 0, 0]
modifier = 1
lastEmSet = [0, 0]
wordNum = 0
emTotal = 0
emPer = 0


def checkEmotion(word):

    global modifier
    global emSet
    global lastEmSet

    l = emotionsDict.get(word, [9, 9])
    mag = 0

    if word == 'of':
        return
    elif word in {'.', '?', '!', ';'} and modifier > 1:
        mag = modifier * lastEmSet[1]
        modifier = 1
        emSet[lastEmSet[0]] += mag
    elif 0 <= l[0] <= 3:
        mag = modifier*l[1]
        lastEmSet = l[:]
        modifier = 1
        emSet[l[0]] += mag
    elif l[0] == 4:
        modifier *= l[1]


if __name__ == "__main__":

    # The movie is really great. The action and comedy were at it's peak. I was really sad when the hero nearly died. The suspence it create is just beautiful. At the end it was really exciting and surprising.
    print('\n\n\n')
    
    inp = """After Avengers Infinity War, we waited for the Avengers Endgame. We wondered how the story would go on, how our heroes would turn back, what would be the end of Thanos. Many theories related to this have been put forward. Avengers Endgame was undoubtedly the most anticipated film of recent years. Normally, the higher the expectation, the higher the probability of disappointment. But this is not the case for Endgame. Whatever you're expecting, you find much more in the film. This means that the biggest concern about the film has disappeared.

On the other hand, another comparison comes up. Is Endgame more successful than Infinity War? We can comfortably say it Avengers Infinity War is just the beginning of the story. Endgame was the finale of the story. So we shouldn't think of these two films as two separate stories. There is only one story divided into two parts.

Avengers Endgame is, above all, a great homage to the ten-year history of the Marvel Cinematic Universe. The story highlights the original Avengers team. Iron Man, Captain America, Thor, Hulk, Black Widow and Hawkeye are at the center of events. No character comes in front of them. Of course there are many characters that play an important role in the story outside the original Avengers team. Everyone's concern was that Captain Marvel, who was included in the Marvel world, overshadowed other heroes. We can say that this certainly did not happen. What is important in this struggle is not how strong you are, but how good you are. This comes to the fore in all areas. It gives good message about being a hero and a family.

Of course, Avengers Endgame has some critical aspects. For example, is the three-hour period necessary in terms of the story? It can be discussed. The head of the story moves much slower than the rest. It also drags the heroes into an emotional predicament. Then the tempo is rising and the heavy scenes we are watching are getting more meaningful. The last 45 minutes of the movie is fully action packed. But the last 45 minutes goes so fast that you don't even realize it. Action and battle scenes are really successful. There is not even a slight distress about visual effects. There are also slight logic errors in the film, but in general the story is so successful that these details become meaningless and insignificant after a certain point.

Lastly, Avengers Endgame doesn't have a movie end scene. Because after the film's final, there is no need for another scene. The Marvel legend Stan Lee appears with a small stage. But this is the last surprise scene in the Marvel Cinematic Universe. Moreover, there is no clue about Marvel's future. This makes us wonder more about Spider-Man: Far from Home. """
    # inp = "The movie is action packed and funny at the same time. Its really exciting and some scenes are really funny. Its the best film i hsvr=e ever seen."
    
    print('Give Review:-\n\n',inp)

    inp = inp + ' *'

    text = inp.lower()

    # em1 = 0 # *Joy and Sad
    # em2 = 0 # *Trust and Disgust
    # em3 = 0 # *Fear and Anger
    # em4 = 0 # *Surprise and Anticipation

    # extract words from text
    c = ''

    for i in text:
        if i.isalpha() and i != ' ':
            c = c + i
        elif len(c) > 0:
            checkEmotion(c)
            c = ''
            wordNum += 1
        else:
            c = ''
        if i in {'.', '?', '!', ';'}:
            checkEmotion(i)


    emTotal = sum(emSet)            #Total emotion value
    emPer = emTotal/wordNum         #Emotion value per word

    print('\n')
    print('Avarage Emotion:',emPer)
    print('Total Emotion:',emTotal)

    totalETanh = np.tanh(emTotal)       # tanh ( totalEm )
    E = emTotal * 0.1
    totalETanh01 = np.tanh(E)           # tanh ( 0.1 * totalEm )
    totalETanh10 = 10 * totalETanh01    # 10 * tanh ( 0.1 * totalEm )
    
    print('tanh value:', totalETanh10)
    print('\n\n',emSet)                 # [joy/sad, trust/disgust, fear/anger, surprise/anticipation]
    print()
