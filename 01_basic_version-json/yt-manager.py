import json

def load_data():
    try :
        with open("youtube.txt","r") as file :
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open("youtube.txt",'w') as file :
        json.dump(videos,file)

def list_all_videos(videos):
    #print("\n")
    print("*" * 60)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']} Duration :{video['time']}")
    print("*" * 60)
def add_video(videos):
    name = input("Enter name of the video: ")
    time = input("Enter time of the video : ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video to be updated : "))
    if 1<= index <= len(videos):
        name = input("Enter name of the new video : ")
        time = input("Enter time of the new video : ")
        videos[index-1] = {'name':name , 'time': time}
        save_data_helper(videos)
    else :
        print("INVALID INDEX")
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter index of the video to be deleted : "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("INVALID INDEX")

def main():
    # videos = load_data()
    while True : 
        print("YT Manager App || LESSGO")
        print("1 : List all the videos")
        print("2 : Add videos")
        print("3 : Update video")
        print("4 : Delete video")
        print("5 : Exit the app")


        print("Waiting for input...")
        choice = input("Enter your choice(1 to 5) : ")

        videos = load_data()

        match choice :
            case'1':
                list_all_videos(videos)
            case'2':
                add_video(videos)
            case'3':
                update_video(videos)
            case'4':
                delete_video(videos)
            case'5':
                print("Goodbye gng!")
                break
            case _:
                print("Invalid choice! Enter again")

if __name__=="__main__":
    main()
