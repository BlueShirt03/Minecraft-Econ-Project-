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
               WHERE minecraft_username = %s;
               """, (minecraft_username,)
            )
            connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting player: {e}")
            return False
        
        finally:
            cursor.close()
            connection.close()
    
    def get_player_by_discord_id(self, discord_id):
        connection = get_connection()

        if connection is None:
            print("Could not connect to database.")
            return False
        
        try:
            cursor = connection.cursor()

            cursor.execute(
                """SELECT * FROM player
                    WHERE discord_id = %s;
                    """, (discord_id,)
            )
            
            connection.commit()
            found_player = cursor.fetchone()

            if found_player is None:
                print("Could not find discord id")
                return False  
            
            return found_player
        
        except Exception as e:
            print(f"Error finding discord_id: {e}")
            return False
        
        finally:
            cursor.close()
            connection.close()

    def get_player_by_username(self, minecraft_username):
        connection = get_connection()

        if connection is None:
            print("Could not connect to database")
            return False
        try:
            cursor = connection.cursor()

            cursor.execute(
                """SELECT * FROM player
                WHERE minecraft_username = %s;""",
                (minecraft_username,)
                        
            )
            connection.commit()
            found_player = cursor.fetchone()

            if found_player is None:
                print("Could not find username")
                return False
            
            return found_player
        except Exception as e:
            print(f"Error finding username: {e}")
        
        finally:
            connection.close()
            cursor.close()
        
         

    
if __name__ == "__main__":
    player_repository = PlayerRepository()

    """success1 = player_repository.create_player(
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
    )"""

    find_username = player_repository.get_player_by_username("YoMama67")
    print(find_username)

    
 