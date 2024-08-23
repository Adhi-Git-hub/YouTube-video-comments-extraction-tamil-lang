import googleapiclient.discovery
import csv
import os
import re

def get_youtube_comments(api_key, video_id):
    """Fetches all YouTube comments for a given video ID."""
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    comments = []
    next_page_token = None
    
    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            maxResults=100,  # Maximum allowed per request
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            top_level_comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(top_level_comment)
            if 'replies' in item and 'comments' in item['replies']:
                for reply in item['replies']['comments']:
                    reply_text = reply['snippet']['textDisplay']
                    comments.append(reply_text)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break  # No more pages, exit the loop

    return comments

def is_tamil(text):
    """Check if the given text contains Tamil characters."""
    tamil_regex = re.compile("[\u0B80-\u0BFF]+")   # unicode for tamil language 
    """replace unicode for your need"""
    return tamil_regex.search(text) is not None

def extract_and_save_comments(api_key, video_urls):
    """Extracts comments from a list of YouTube video URLs and saves them to individual CSV and text files."""
    # Create directory if it doesn't exist
    folder_nametxt = "folderName"
    folder_namecsv = "folderName"
    os.makedirs(folder_nametxt, exist_ok=True)
    os.makedirs(folder_namecsv, exist_ok=True)
    i=175

    for  url in video_urls:
        try:
            video_id = url.split("/")[-1].split("?")[0]  # Extract video ID
        except IndexError:
            print(f"Error parsing URL: {url}")
            continue  # Skip URLs with parsing errors

        comments = get_youtube_comments(api_key, video_id)
        tamil_comments = [comment for comment in comments if is_tamil(comment)]

        if tamil_comments:
            csv_filename = os.path.join(folder_namecsv, f"YT_dataset_V{i}.csv")
            text_filename = os.path.join(folder_nametxt, f"YT_dataset_V{i}.txt")
            write_comments_to_csv(tamil_comments, csv_filename)
            write_comments_to_text(tamil_comments, text_filename)
            print(f"Tamil comments for video {video_id} written to {csv_filename} and {text_filename}")
            i+=1

def write_comments_to_csv(comments, filename):
    """Writes comments to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Comment"])  # Header row
        for comment in comments:
            writer.writerow([comment])

def write_comments_to_text(comments, filename):
    """Writes comments to a text file."""
    with open(filename, 'w', encoding='utf-8') as textfile:
        for comment in comments:
            textfile.write(comment + "\n")

# Example usage
api_key = "AIza*****sample api key****mfUvo"
video_urls = [
#youtube videos -> video id
    "1sIeYPhR-Bg",   #sample video id 
    "PNuJCezNlIw",
]

extract_and_save_comments(api_key, video_urls)
