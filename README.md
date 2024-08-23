# YouTube-video-comments-extraction-tamil-lang
Python tool for extracting and filtering Tamil comments from YouTube videos. Saves the extracted data in both CSV and text formats, enabling easy analysis. Ideal for projects involving web scraping, natural language processing, and sentiment analysis focused on the Tamil language.


## Overview

This project provides a Python script to extract comments from YouTube videos, filter them for Tamil language content, and save the extracted comments in both CSV and text file formats. It leverages the YouTube Data API for fetching comments and regular expressions for detecting Tamil text. This tool is particularly useful for collecting data for natural language processing tasks, such as sentiment analysis or building word embeddings specifically for the Tamil language.

## Features

- **YouTube Comment Extraction**: Fetches all comments, including replies, from specified YouTube videos.
- **Tamil Language Filtering**: Filters out comments that do not contain Tamil script.
- **Data Saving**: Saves the extracted comments in both CSV and text formats for further analysis or processing.

## Prerequisites

- **Python 3.x**: Make sure Python is installed on your system.
- **Google API Client Library**: Install the required library by running:
  ```bash
  pip install google-api-python-client

 - YouTube Data API Key: You will need a valid API key from the [Google Cloud Console.](https://console.cloud.google.com/welcome?project=reverberant-kit-431804-f1)
## Usage
Update the API Key: Replace the placeholder API key in the script (ytextract.py) with your actual YouTube Data API key.

Add YouTube Video IDs: Update the video_urls list with the YouTube video IDs from which you want to extract comments

## Comment Processing Workflow
The script processes comments in the following way:

- Top-level Comments: Extracts the main comments from each video.
- Replies: Also extracts replies to each main comment.
- Tamil Language Filtering: Only comments containing Tamil script will be saved.
## Output Files
- CSV Files: Contains the Tamil comments with one comment per row.
- Text Files: Plain text files where each line represents a single Tamil comment
