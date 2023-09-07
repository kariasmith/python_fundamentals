
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

new_team = []

class Player:
    def __init__(self, records):
        self.name = records["name"]
        self.age = records["age"]
        self.position = records["position"]
        self.team = records["team"]

    def new_list_func(self, records):
        for i in records:
            #print(i)
            for keys, values in i.items():
                #print(keys, '-', values)
                new_team.append(values)
        print(new_team)

# player_1 = Player(players[0]["name"],players[0]["age"],players[0]["position"],players[0]["team"])
# print(player_1.name, player_1.age, player_1.position, player_1.team)

# player_jason = Player(jason["name"],jason["age"],jason["position"],jason["team"])
# print(player_jason.name,player_jason.age,player_jason.position,player_jason.team)

first_player = Player(players[0])
first_player.new_list_func(players)

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.