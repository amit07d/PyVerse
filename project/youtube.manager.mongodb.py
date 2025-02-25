from pymongo import MongoClient 
from bson import ObjectId

Client = MongoClient("mongodb+srv://youtubePy:youtubePy@cluster0.dybip.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = Client["ytmanager"]
videos_collection = db["videos"]
print(videos_collection)

def list_all_videos():
    print("\n All Videos: ")
    for video in videos_collection.find():
        print(f"ID:{video['_id']}, Name:{video['name']}, Duration:{video['duration']}")

def add_video():
    name = input("Enter your video name: ").strip()
    duration = input("Enter the video duration: ").strip()

    if not name or not duration:
        print("\nError: Name and duration cannot be empty.")
        return
    
    video = {"name": name, "duration": duration}
    
    videos_collection.insert_one(video)
    print("Video added successfully!")

def update_video():
    video_id = input("Enter your video id to Update: ").strip()
    new_title = input("Enter the new title (press enter to keep the same): ").strip()
    new_duration = input("Enter the new duration time (press enter to keep the same): ").strip()

    update_fields = {}
    if new_title:
        update_fields["name"] = new_title
    if new_duration:
        update_fields["duration"] = new_duration

    if not update_fields:
        print("\nError: At least one field (name or duration) must be provided.")
        return

    try:
        result = videos_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": update_fields}
        )
        
        if result.matched_count:
            print(f"Video updated successfully! Modified {result.modified_count} record(s).")
        else:
            print("No video found with the given ID.")
    
    except Exception as e:
        print(f"Error updating video: {e}")

def delete_video():
    video_id = input("Enter your video ID to delete: ").strip()
    
    try:
        result = videos_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("Video deleted successfully!")
        else:
            print("No video found with the given ID.")
    except Exception as e:
        print(f"Error deleting video: {e}")

def count_video():
    count = videos_collection.count_documents({})
    print(f"Total videos: {count}")

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
