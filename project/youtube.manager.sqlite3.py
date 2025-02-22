import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        duration_time TEXT NOT NULL
    )
''')
conn.close()

def list_all_videos():
    with sqlite3.connect("youtube_videos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos")
        videos = cursor.fetchall()
    
    if not videos:
        print("No videos available")
    else:
        print("\nList of YouTube videos")
        for video in videos:
            print(f"{video[0]}. Title: {video[1]}, Duration: {video[2]}")

def add_video():
    title = input("Enter your video title: ").strip()
    duration = input("Enter the video duration: ").strip()

    if not title or not duration:
        print("Title and duration cannot be empty")
        return

    with sqlite3.connect("youtube_videos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO videos (title, duration_time) VALUES(?, ?)", (title, duration))
        conn.commit()
        print("Video added successfully!")

def update_video():
    video_id = input("Enter the video ID to update: ").strip()
    new_title = input("Enter the new title (press Enter to keep the same): ").strip()
    new_duration = input("Enter the new duration (press Enter to keep the same): ").strip()

    if not video_id.isdigit():
        print("Invalid ID. Please enter a number.")
        return

    with sqlite3.connect("youtube_videos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
        if not cursor.fetchone():
            print("Video ID not found.")
            return

        if new_title and new_duration:
            cursor.execute("UPDATE videos SET title = ?, duration_time = ? WHERE id = ?", (new_title, new_duration, video_id))
        elif new_title:
            cursor.execute("UPDATE videos SET title = ? WHERE id = ?", (new_title, video_id))
        elif new_duration:
            cursor.execute("UPDATE videos SET duration_time = ? WHERE id = ?", (new_duration, video_id))
        else:
            print("No changes made.")
            return

        conn.commit()
        print("Video updated successfully!")

def delete_video():
    video_id = input("Enter the video ID to delete: ").strip()

    if not video_id.isdigit():
        print("Invalid ID. Please enter a number.")
        return

    with sqlite3.connect("youtube_videos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
        if not cursor.fetchone():
            print("Video ID not found.")
            return

        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        print("Video deleted successfully!")

def count_video():
    with sqlite3.connect("youtube_videos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM videos")
        count = cursor.fetchone()[0]
        print(f"\nTotal number of videos: {count}")

def main():
    while True:
        print("\nYouTube Manager with DB")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Count total YouTube videos")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            update_video()
        elif choice == '4':
            delete_video()
        elif choice == '5':
            count_video()
        elif choice == '6':
            print("Exiting from app")
            exit()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
