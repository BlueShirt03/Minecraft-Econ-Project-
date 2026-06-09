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

    def get_player_balance(self,minecraft_username):


        if self.player_repository.player_exist(minecraft_username):
            return False
        else:
            balance = self.player_repository.get_balance(minecraft_username)
            return balance





economy_service = EconomySerivce()

success = economy_service.register_player(discord_id = 987654321, minecraft_username = "BubbleGum25")

success2 = economy_service.get_player_balance(minecraft_username="BlockMaster29")

if success2:
    print("Could find balance.")
else:
    print("Could not find balance.")