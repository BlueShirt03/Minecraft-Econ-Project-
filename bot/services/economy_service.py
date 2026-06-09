from bot.repositories.player_repository import PlayerRepository

class EconomySerivce():

    def __init__(self):
        self.player_repository = PlayerRepository()
        
    
    def register_player(self,discord_id, minecraft_username):

        if self.player_repository.player_exist(minecraft_username):
            return False
        else:
            self.player_repository.create_player(discord_id, minecraft_username)
            return True

economy_service = EconomySerivce()

success = economy_service.register_player(discord_id = 987654321, minecraft_username = "BubbleGum25")

if success:
    print("Player was able to be registered.")
else:
    print("Player was a not able to be registered.")