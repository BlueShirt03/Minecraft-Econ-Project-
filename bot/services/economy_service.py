from bot.repositories.player_repository import PlayerRepository

class EconomySerivce():

    def __init__(self):
        self.player_repository = PlayerRepository()
        
    
    def register_player(self,discord_id, minecraft_username):

        if self.player_repository.player_exist(discord_id):
            return False
        else:
            self.player_repository.create_player(discord_id, minecraft_username)
            return True

