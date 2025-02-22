import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []    

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file) 

def list_all_videos(videos):
    if not videos:
        print('No videos available')
    else:
        print('\n--- List of Youtube Videos  ---')
        for idx, video in enumerate(videos, start=1):
            print(f"{idx}. Title: {video['title']}, Views: {video['views']}, Likes: {video['likes']}, URL: {video['url']}")

def add_video(videos):
    title = input("Enter your video title: ")
    url = input("Enter video URL: ")
    likes = input("Enter number of likes: ")
    views = input("Enter number of views: ")

    try:
        video = {
            'title': title,
            'url': url,
            'likes': int(likes),
            'views': int(views),
        }
        videos.append(video)
        save_data_helper(videos)
        print('\nVideo added successfully')
    except ValueError:
        print('\nInvalid input! Likes and views must be numbers. Video not added.')    

def update_video(videos):
    list_all_videos(videos)
    try:
        videos_index = int(input("Enter the video number to update: ")) - 1
        if 0 <= videos_index < len(videos):
            videos[videos_index]['title'] = input("Enter new title: ")
            videos[videos_index]['url'] = input("Enter new URL: ")
            videos[videos_index]['likes'] = int(input("Enter new number of likes: "))
            videos[videos_index]['views'] = int(input("Enter new number of views: "))
            save_data_helper(videos)
            print("\nVideo updated successfully")
        else:
            print("\nInvalid video number.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

def delete_video(videos):
    list_all_videos(videos)
    try:
        delete_video_index = int(input("\nEnter the video number to delete: ")) - 1
        if 0 <= delete_video_index < len(videos):
            del videos[delete_video_index]  
            save_data_helper(videos)
            print("\nVideo deleted successfully")
        else:
            print("\nInvalid video number.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option ")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app.")
                exit()  
            case _:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
