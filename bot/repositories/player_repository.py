from bot.database.connection import get_connection

class PlayerRepository:
    def create_player(self, discord_id, minecraft_username):
        connection = get_connection()

        if connection is None:
            print("Could not connect to database.")
            return False
        
        try:
            cursor = connection.cursor()

            cursor.execute(
                """ INSERT INTO player (discord_id, minecraft_username)
                VALUES (%s, %s);
                """,
                (discord_id, minecraft_username)
            )

            connection.commit()
            return True
        except Exception as e:
            print(f"Error creating player: {e}")
            return False
        
        finally:
            cursor.close()
            connection.close()
      
    def delete_player(self,minecraft_username):
        connection = get_connection()

        if connection is None:
            print("Could not connect to database.")
            return False

        try:
            cursor = connection.cursor()

            cursor.execute(
               """Delete from player
               WHERE minecraft_username = %s
               """, (minecraft_username,)
            )
            connection.commit()
            return True
        except Exception as e:
            print(f"Error creating player: {e}")
            return False
        
        finally:
            cursor.close()
            connection.close()
    
if __name__ == "__main__":
    player_repository = PlayerRepository()

    success1 = player_repository.create_player(
        discord_id = 123456789, 
        minecraft_username = "PotatoLover25"
    )

    success2 = player_repository.create_player(
        discord_id = 8374873, 
        minecraft_username = "BlockMaster29"
    )

    success3 = player_repository.create_player(
        discord_id = 17683640, 
        minecraft_username = "YoMama67"
    )

    del_player = player_repository.delete_player(minecraft_username="YoMama67")
    print(del_player)
 