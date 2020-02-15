"""
Q1.
We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}
Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not
fixed (here they are 'match1','match2','match3'), nor are the names of the players. A player need not have a score recorded in all 
matches.

Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. 
Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, 
and topscore is an integer, the total score of playername.

The input will be such that there are never any ties for highest total score.

For instance:

  >>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 
  'player3':91}})
('player3', 100)

  >>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)
"""
d={'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}

def orangecap(d):
    players={}
    i=0
    for event in d:
        for player in d[event]:
            if not player in players.values():
                players[i]=player
                i=i+1
    netrun={}
    for player in players.values():
        netrun[player]=0
        for event in d:
            if player in d[event].keys():
                netrun[player]+=d[event][player]
    maxrun=0
    playername=""
    for player in netrun.keys():
        if maxrun < netrun[player]:
            maxrun=netrun[player]
            playername=player
        
    return ((playername,maxrun))
                
'''
Q2
Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x4 - 17x2 - 3x + 5. Each term of the 
polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:

Terms are sorted in descending order of exponent
No term has a zero cofficient
No two terms have the same exponent
Exponents are always nonnegative
For example, the polynomial introduced earlier is represented as

  [(3,4),(-17,2),(-3,1),(5,0)]
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:

  
  addpoly(p1,p2)
  multpoly(p1,p2)
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these 
functions should also obey the same constraints.

Hint: You are not restricted to writing just the two functions asked for. You can write auxiliary functions to "clean up" 
polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that 
can be combined to achieve the desired format.

You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation,
and then convert back.

Some examples:

  >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
  [(2, 1),(3, 0)]
Explanation: (4x3 + 3) + (-4x3 + 2x) = 2x + 3

  >>> addpoly([(2,1)],[(-2,1)])
  []
Explanation: 2x + (-2x) = 0
'''
p1=[(4,3),(3,0)]
p2=[(-4,3),(2,1)]
def addpoly(p1, p2):
    res=[]
    i=0
    j=0
    m=len(p1)
    n=len(p2)
    while i+j< m+n:
        if i==m:
            res+=p2[j:n]
            break
        elif j==n:
            res+=p1[i:m]
            break
        elif p1[i][1]>p2[j][1]:
            res.append(p1[i])
            i+=1
        elif p1[i][1]==p2[j][1]:
            if p1[i][0]+p2[j][0]:
                res.append((p1[i][0]+p2[j][0],p1[i][1]))
            j+=1
            i+=1
        elif p1[i][1]<p2[j][1]:
            res.append(p2[j])
            j+=1                                                      
    return(res)
'''
  >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
  [(1, 3),(-1, 0)]
Explanation: (x - 1) * (x2 + x + 1) = x3 - 1
'''
def clean(p):
    res=p
    n=0
    while 1:
        if res[n][0]==0:
            res.remove(res[n])
            n-=1
        n+=1
        if n==len(res):
            break
    return (res)

def multpoly(p1,p2):
    res=[]
    for t1 in p1:
        for t2 in p2:
            
            for n in range(0, len(res)):
                if t1[1]+t2[1]== res[n][1]:
                    res[n]=(res[n][0]+t1[0]*t2[0],res[n][1])
                    break
            else:  ## special action for normal termination| It returs 0 when break ran in loop
                res.append((t1[0]*t2[0],t1[1]+t2[1]))     
    return (clean(res))














