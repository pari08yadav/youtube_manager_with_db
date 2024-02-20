import mysql.connector 

connection = mysql.connector.connect(
    host= "localhost",
    user = "parishram",
    password = "yadav08",
    database = "youtube_manager"
    )
cursor = connection.cursor()


def list_all_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print('\n')
        print('*' * 70)
        print(row)
        print('\n')
        print('*' * 70)
        
def add_videos():
    name = input("Enter the video name")
    time = input("Enter the video time")
    cursor.execute("INSERT INTO videos (name, time) VALUES (%s, %s)", (name, time))
    connection.commit()
    
def update_videos():
    video_id = input("Enter video Id to update")
    new_name = input("Enter vidoe name to update")
    new_time = input("Enter video time to update")
    cursor.execute("UPDATE videos SET name = %s, time = %s WHERE id = %s", (new_name, new_time, video_id ))
    connection.commit()
    
def delete_videos():
      video_id = input("Enter video Id to update")
      cursor.execute("DELETE FROM videos where id = %s", (video_id))
      connection.commit()
    
    

def main():
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube video")
        print("2. Add a youtube vidoe.")
        print("3. Update a youtube video details.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_videos()
            case '3':
                update_videos()
            case '4':
                delete_videos()
            case '5':
                break
            case _:
                print("Invalid Choice")
                
if __name__ == '__main__':
    main()
    