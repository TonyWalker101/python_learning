#codewars kata => https://www.codewars.com/kata/5bb904724c47249b10000131/python

def points(games):
  my_team_score = 0

  for match in games:
    teams_points = match.split(":")
    my_team = teams_points[0]
    opp_team = teams_points[1]

    if my_team > opp_team:
      my_team_score += 3

    if my_team == opp_team:
      my_team_score += 1

  return my_team_score


#tests

#should print 30
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
#should print 10
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))
#should print 0
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))
#should print 15
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))
#should print 12
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']))