from calcFunctions import *

upperScoreList = [
    'Aces', 'Twos', 'Threes', 
    'Fours', 'Fives', 'Sixes', 
]

lowerScoreList = [
    'Choice', '3card', '4card', 
    'Full house', 'S.Straight', 'L.Straight', 
    'Yatcht', 
]

functionMap = {
    'Aces': aces, 'Twos': twos, 'Threes': threes, 
    'Fours': fours, 'Fives': fives, 'Sixes': sixes, 
    'Choice':choice, '3card': tcard, '4card': fcard, 
    'Full house': fhouse, 'S.Straight': s_straight, 'L.Straight': l_straight, 
    'Yatcht': yatcht, 
}