library(dplyr)
library(ggplot2)
#BATTING

batting <- read.csv('Batting.csv')
# head(batting)
# str(batting)
# head(batting$AB)
# head(batting$X2B) # OR head(batting[,8]) since col no=8

#Batting Average = Hits/AtBall
batting$BA <- batting$H/batting$AB
tail(batting$BA,5)

#On Base Percentage =  (Hits + BasesonBalls + HitByPitch)/(AtBall + BasesonBalls + HitByPitch + SacrificeFly)
batting$OBP <- (batting$H + batting$BB + batting$HBP)/(batting$AB + batting$BB + batting$HBP + batting$SF)

#Singles = Hits - Doubles - Triples - HomeRuns
batting$X1B <- batting$H - (batting$X2B + batting$X3B + batting$HR)

#SLugging averaGe = ((Singles) + (2 x Doubles) + (3 x Triples) + (4 x HomeRuns))/AtBall
batting$SLG <- (batting$X1B + (2 * batting$X2B) + (3 * batting$X3B) + (4 * batting$HR))/batting$AB


#SALARY

sal <- read.csv('Salaries.csv')

#summary(batting) #Min yearID = 1871
#summary(sal) #Min yearID = 1085

batting <- subset(batting,batting$yearID > 1984)
#summary(batting)  #Now MIN yearID = 1985

#MERGING batting and sal data frames by playerID and yearID
combo <- merge(batting,sal,by = c('playerID','yearID'))
#str(batting)

#damonjo01 giambja01 saenzol01 LEFT
lost_players <- subset(combo,playerID %in% c('giambja01','damonjo01','saenzol01'))

#left in 2001 
lost_players <- subset(lost_players,yearID == 2001,select = c(playerID,H,X2B,X3B,HR,OBP,SLG,BA,AB))


#REPLACEMENT ALGO
#TotalSAl < = 15mil
#totalAB  > = Lostplayers()  1469
#mean(OBP) >= mean(OBP(lostplayers)) 0.3638687

avail.players <- filter(combo,yearID==2001)

#ggplot(avail.players,aes(x=OBP,y= salary)) + geom_point()
avail.players <- filter(avail.players,salary<8000000,OBP>0)

avail.players <- filter(avail.players,AB > 480)

possible <- head(arrange(avail.players,desc(OBP)),10)
possible <- select(possible,playerID,OBP,AB,salary)

replacement <- slice(possible, 2:4)#AS No,1 is giambja01 who left the team

print(paste0("Replacement for : ", lost_players$playerID))
