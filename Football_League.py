"""
Football League


Football League Table Statement : All major football leagues have big league tables. Whenever a new match is played, the league table is updated to show the current rankings (based on Scores, Goals For (GF), Goals Against (GA)). Given the results of a few matches among teams, write a program to print all the names of the teams in ascending order (Leader at the top and Laggard at the bottom) based on their rankings.



Rules: A win results in 2 points, a draw results in 1 point and a loss is worth 0 points. The team with the most goals in a match wins the match. Goal Difference (GD) is calculated as Goals For (GF) Goals Against (GA). Teams can play a maximum of two matches against each other Home and Away matches respectively.

The ranking is decided as follows: Team with maximum points is ranked 1 and minimum points is placed last Ties are broken as follows Teams with same points are ranked according to Goal Difference(GD).

If Goal Difference(GD) is the same, the team with higher Goals For is ranked ahead

If GF is same, the teams should be at the same rank but they should be printed in case-insensitive alphabetic according to the team names. More than 2 matches of same teams, should be considered as Invalid Input.

A team can’t play matches against itself, hence if team names are same for a given match, it should be considered Invalid Input



Input Format: First line of input will contain number of teams (N) Second line contains names of the teams (Na) delimited by a whitespace character Third line contains number of matches (M) for which results are available Next M lines contain a match information tuple {T1 T2 S1 S2}, where tuple is comprised of the following information

T1 Name of the first team
T2 Name of the second team
S1 Goals scored by the first team
S2 Goals scored by the second team


Output Format: Team names in order of their rankings, one team per line OR Print “Invalid Input” where appropriate.



Constraints: 0< N <=10,000 0<=S1,S2



Example: Consider 5 teams Spain, England, France, Italy and Germany with the following fixtures:

Match 1: Spain vs. England (3-0) (Spain gets 2 points, England gets 0)
Match 2: England vs. France (1-1) (England gets 1 point, France gets 1)
Match 3: Spain vs. France (0-2) (Spain gets 0 points, France gets 2)


Table 1. Points Table after 3 matches

5
Spain England France Italy Germany
3
Spain England 3 0
England France 1 1
Spain France 0 2

Output :
 
France
Spain
England
Germany
Italy

Since, Italy and Germany are tied for points, goals difference is checked. Both have same, so, Goals For is checked. Since both are same. Germany and Italy share the 4th rank. Since Germany appears alphabetically before Italy, Germany should be printed before Italy. Then the final result is: France Spain England Germany Italy



Sample:

tcs codevita questions sample input and output
"""
def func(matchdetails):
    goalfor=dict()
    goalag=dict()
    goaldif=dict()
    point=dict()

    #create goalFor,Goal against dict
    for i in range(len(matchdetails)):
        if matchdetails[i][0] in goalfor:
            goalfor[matchdetails[i][0]]+=matchdetails[i][2]
            goalag[matchdetails[i][0]]+=matchdetails[i][3]
        else:
            goalfor[matchdetails[i][0]]=matchdetails[i][2]
            goalag[matchdetails[i][0]]=matchdetails[i][3]

        if matchdetails[i][1] in goalfor:
            goalfor[matchdetails[i][1]]+=matchdetails[i][3]
            goalag[matchdetails[i][1]]+=matchdetails[i][2]
        else:
            goalfor[matchdetails[i][1]]=matchdetails[i][3]
            goalag[matchdetails[i][1]]=matchdetails[i][2]

        if(matchdetails[i][2] ==matchdetails[i][3]):
            if matchdetails[i][0] in point:
                point[matchdetails[i][0]]+=1
            else:
                point[matchdetails[i][0]]=1

            if matchdetails[i][1] in point:
                point[matchdetails[i][1]]+=1
            else:
                point[matchdetails[i][1]]=1

        #create a point dict

        elif(matchdetails[i][2] >matchdetails[i][3]):
            if matchdetails[i][0] in point:
                point[matchdetails[i][0]]+=2
            else:
                point[matchdetails[i][0]]=2
        elif(matchdetails[i][2] <matchdetails[i][3]):
            if matchdetails[i][1] in point:
                point[matchdetails[i][1]]+=2
            else:
                point[matchdetails[i][1]]=2
    #create a goal diff dict
    for i in goalfor:
        goaldif[i]=goalfor[i]-goalag[i]
        if i not in point:
        	point[i]=0

    res={k: v for k, v in sorted(point.items(), key=lambda item: item[1])}
    
    final=[]
    values=res.values()

    if(len(set(values))==len(values)):
        final.extend(list(res.keys()))
    else:
        count=0
        
        temp=0
        for i in res:
            count+=1
            
            if(count==1):
                temp=i
                
            if(count !=1 and count<=len(res)):
                if(res[temp]==res[i]):
                	
                	if(goaldif[i]>goaldif[temp]):
                		final.append(i)
                		
     
                	elif(goaldif[i]<goaldif[temp]):
                		final.append(temp)
                		temp=i
                	else:
                		if(goalfor[i]>goalfor[temp]):
                			final.append(i)
                			
                			
                		elif(goalfor[i]<goalfor[temp]):
                			final.append(temp)
                			temp=i
                			
                		else:
                			a=sorted([i,temp])
                			final.extend(a)
                			temp=i
                else:
                	if(res[temp]>res[i]):
                		final.append(temp)
                		temp=i
                	elif(res[temp]<res[i]):
                		final.append(i)
        final.append(temp)
        final=final[::-1]
    
    return final




n=int(input("Enter the  team size : "))
l=list(input("Enter the  team : ").split(" "))
match=int(input())
matchdetails=[]
same=False
for i in range(match):
    matchlist=list(input("Enter the match details : ").split(" "))
    matchlist[2]=int(matchlist[2])
    matchlist[3]=int(matchlist[3])
    matchdetails.append(matchlist)
    if(matchlist[0]==matchlist[1]):
    	same=True

if(same):
	print("Invalid Input")
else:
	final=func(matchdetails)
	final=final[::-1]
	for i in final:
		if i in l:
			l.remove(i)
	sorted(l)

	final.extend(l[::-1])
	for i in final:
		print(i)







n=int(input("Enter the chakravyuha : "))
x=0
y=0
r=n
c=n

t=1
l=[[0 for i in range(n)] for j in range(n)]

while(x<=r and y<=c):
    for i in range(y,c,+1):
        l[y][i]=t
        t+=1
    x+=1
    for i in range(x,r,-1):
        l[i][c-1]=t
        t+=1
    c-=1

    for i in range(c,y,-1):
        l[i-1][c]=t
        t+=1
    r-=1
    for i in range(,x,+1):
        l[i-1][r]=t
        t+=1
    y+=1





for  i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
