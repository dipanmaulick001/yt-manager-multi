import sqlite3
conn = sqlite3.connect("youtube-vid.db")
cursor = conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
               ''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name, time))
    conn.commit()
def update_video(video_id , new_name , new_time):
    cursor.execute("UPDATE videos SET name=? , time=? WHERE id =?",(new_name,new_time,video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id))
    conn.commit()



def main():
    while True :
        print("Welcome to the YT Manager App")
        print("1. List all the videos")
        print("2.Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print('5 . Exit the app')
        
        choice = input("Enter your choice please : ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter name of the video:  ")
            time = input("Enter time of the video:  ")
            add_video(name,time)
        elif choice =="3":
            video_id = input("Enter video ID of the vdo to be updated: ")
            name = input("Enter name of the video:  ")
            time = input("Enter time of the video:  ")
            update_video(video_id,name,time)
        elif choice =="4":
            video_id = input("Enter video ID of the video to be deleted: ")
            delete_video(video_id)
        elif choice =="5":
            print("Goodbye! Thanks")
            break
        else :
            print("INVALID CHOICE !")




if __name__ == "__main__":
    main()