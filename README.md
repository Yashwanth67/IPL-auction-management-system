# IPL-auction-management-system

> ***Introduction -***
>
> The mini-world that we have chosen is the database of all the teams,
> participants and the matches that were played in a particular year in
> the IPL. The IPL database is used to update and maintain information
> on the various things required about players and their teams. It can
> be accessed by the organisers as well as the players and fans with
> varying degrees of access.
>
> ***Purpose -***
>
> The database stores all information regarding teams, players, stadiums
> and matches of a particular year. This helps quick retrieval of any
> data regarding match-ups, venue, and players in the team. It also
> enables organisers to directly match teams in matches by applying
> various algorithms upon it.
>
> ***Users -***
>
> The organisers can use the database to keep track of matches, players
> and other information about teams. Fans can access the database to see
> which teams are playing on a particular day and stadium
> information(for booking tickets). Fans can also access data of
> previous matches to see how their favourite team had performed in
> them. The commentators can use it to see how different scenarios have
> led to different outcomes.
>
> ***Applications -***
>
> It can be used by fans to either get the venue of a match to book
> tickets or to find out the statistics of a particular team and find
> how they fared in their matches against another team.
>
> It can be used by organisers to keep track of all the information of
> players in one place so that they can be accessed easily in case of
> emergency.
>
> 
> **2. Coached by**\
> a. 2-degree relationship\
> b. Relationship between Team and Coach\
> c. N coaches can coach to 1 team so it is N:1 cardinality
> (Coaches:Team) This relationship connects the coach with a particular
> team. d.
>
> **3. Umpired by**\
> a. 2-degree relation\
> b. The relationship is between entities Match and Umpire .
>
> c\. 3 umpires can umpire 1 match so it is 3:1 cardinality
> (umpires:match) d. This relationship connects the matches with the
> umpires who umpired them.
>
> **4. Awarded**\
> a. 2-degree relation\
> b. The relationship is between entities Match and Award .
>
> c\. 1 match can have n awards so it is 1:n(match:awards)\
> d. This relationship connects the matches with the awards given for
> that particular match.
>
> ***n\>3 Relationships:***
>
> ★ **Game**\
> ○ 4-degree relationship\
> ○ The relationship is between Team,Players,Matches and Stadiums. ○ 2
> teams play in 1 match with n players in 1 stadium so, the ratio is
> 2:1:n:1 (teams:match:players:stadium).
>
> ○ This relationship connects the 2 teams which have played in a
> particular match with the players who played in that match and the
> stadium where the match was played.
>
> ***Functional Requirements***
>
> ***Modifications***
>
> **1. Insert:**\
> a. Event organisers can insert data into the database. Rest all types
> of users can only retrieve data.
>
> b\. Insert Team when a new team is added into the IPL season.
>
> c\. Insert Player when a new player is added to the season. The user
> has to ensure that the constraints are fulfilled or else, it may be
> not added.
>
> **2. Delete:**\
> a. Event organisers can delete data from the database. Rest all types
> of users cannot delete data.
>
> b\. Matches which are cancelled are deleted from the database by event
> organisers.
>
> c\. Delete Player, if he is no longer in the season in the present
> year.
>
> **3. Update:**\
> a. The Winner of a match can be updated with the winning team\'s id or
> 0 for a draw only after the end of match by Event organisers.
>
> b\. The dates of matches can be updated in case of rain or any other
> cause by Event Organisers.
>
> c\. The players of a match can be updated before the match if any
> player is injured or unable to play for some reason.This also is
> restricted to Event organisers.
>
> ***Retrievals***
>
> **1. Selection:**\
> a. "Retrieve all the players belonging to Team XXXX".
>
> b\. "Retrieve all the Umpires who umpired the match XXXX".
>
> **2. Projection:**\
> a. "Name all the stadiums with capacity \>= 2500".
>
> b\. "Name all the Players whose age \>= 35"\
> **3. Aggregate:**\
> a. "Maximum age of a participating player".
>
> b\. "Average capacity of all the stadiums".
>
> **4. Search:**\
> a. \"Team that won the match on 9/8/21 in xxx stadium\"\
> b. \"Third umpire in final match of season\"\
> **5. Analysis:**\
> a. "Number of players whose age is below average in Team X". b.
> \"Ratio of batsmen to bowlers in all winning teams".
