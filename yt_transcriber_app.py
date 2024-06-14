# import re
# from io import BytesIO
# import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

# # Function to get video ID from URL
# def get_video_id(youtube_url):
#     # Regular expression to extract video ID from YouTube URL
#     pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)'
#     match = re.match(pattern, youtube_url)
#     if match:
#         return match.group(1)
#     else:
#         return None

# # Function to format transcript with questions, answers, and proper spacing
# def format_transcript(transcript):
#     formatted_transcript = ""
#     prev_speaker = None
#     for text in transcript:
#         speaker = text.get('speaker', None)
#         if speaker != prev_speaker:
#             # Add a newline before a new speaker
#             if formatted_transcript and formatted_transcript[-1] != '\n':
#                 formatted_transcript += '\n'
#         if text['text'].endswith(('?', '.', '!')):
#             # Add a newline after each sentence
#             formatted_transcript += text['text'] + '\n\n'
#         else:
#             formatted_transcript += text['text'] + ' '
#         prev_speaker = speaker
#     return formatted_transcript.strip()

# # Function to transcribe YouTube video
# def transcribe_youtube_video(youtube_url):
#     video_id = get_video_id(youtube_url)
#     if video_id:
#         try:
#             # Retrieve transcript from YouTube Data API
#             transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'te', 'hi', 'es', 'fr', 'ja', 'ko', 'de', 'ml', 'gu'])
            
#             if transcript:
#                 # Format transcript with questions, answers, and proper spacing
#                 formatted_transcript = format_transcript(transcript)
#                 return formatted_transcript
#             else:
#                 st.error("No transcript available for the video.")
#                 return None

#         except NoTranscriptFound:
#             st.error("No transcript found for the video.")
#             return None
#         except TranscriptsDisabled:
#             st.error("Transcripts are disabled for this video.")
#             return None
#         except Exception as e:
#             st.error(f"Error: {e}")
#             return None
#     else:
#         st.error("Invalid YouTube URL.")
#         return None

# # Streamlit app
# st.title("Multilingual YouTube Video Transcriber")

# youtube_url = st.text_input("Enter YouTube URL")

# if st.button("Generate Transcript"):
#     if youtube_url:
#         transcript = transcribe_youtube_video(youtube_url)
#         if transcript:
#             st.success("Transcript generated successfully!")
#             st.text_area("Transcript", transcript, height=300)
            
#             # Creating a downloadable text file in bytes
#             transcript_file = BytesIO(transcript.encode('utf-8'))

#             st.download_button(
#                 label="Download Transcript",
#                 data=transcript_file,
#                 file_name="transcript.txt",
#                 mime="text/plain"
#             )
#     else:
#         st.warning("Please enter a valid YouTube URL.")




# import re
# from io import BytesIO
# import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

# # Function to get video ID from URL
# def get_video_id(youtube_url):
#     pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)'
#     match = re.match(pattern, youtube_url)
#     if match:
#         return match.group(1)
#     else:
#         return None

# # Function to format transcript with questions, answers, and proper spacing
# def format_transcript(transcript):
#     formatted_transcript = ""
#     prev_speaker = None
#     for text in transcript:
#         speaker = text.get('speaker', None)
#         if speaker != prev_speaker:
#             if formatted_transcript and formatted_transcript[-1] != '\n':
#                 formatted_transcript += '\n'
#         if text['text'].endswith(('?', '.', '!')):
#             formatted_transcript += text['text'] + '\n\n'
#         else:
#             formatted_transcript += text['text'] + ' '
#         prev_speaker = speaker
#     return formatted_transcript.strip()

# # Function to transcribe YouTube video
# def transcribe_youtube_video(youtube_url):
#     video_id = get_video_id(youtube_url)
#     if video_id:
#         try:
#             transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
#             if transcript:
#                 formatted_transcript = format_transcript(transcript)
#                 return formatted_transcript
#             else:
#                 st.error("No transcript available for the video.")
#                 return None
#         except NoTranscriptFound:
#             st.error("No transcript found for the video.")
#             return None
#         except TranscriptsDisabled:
#             st.error("Transcripts are disabled for this video.")
#             return None
#         except Exception as e:
#             st.error(f"Error: {e}")
#             return None
#     else:
#         st.error("Invalid YouTube URL.")
#         return None

# # Streamlit app
# st.title("Multilingual YouTube Video Transcriber")

# youtube_url = st.text_input("Enter YouTube URL")

# if st.button("Generate Transcript"):
#     if youtube_url:
#         transcript = transcribe_youtube_video(youtube_url)
#         if transcript:
#             st.success("Transcript generated successfully!")
#             st.text_area("Transcript", transcript, height=300)
            
#             # Creating a downloadable text file in bytes
#             transcript_file = BytesIO(transcript.encode('utf-8'))

#             st.download_button(
#                 label="Download Transcript",
#                 data=transcript_file,
#                 file_name="transcript.txt",
#                 mime="text/plain"
#             )
#     else:
#         st.warning("Please enter a valid YouTube URL.")


import re
from io import BytesIO
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

# Function to get video ID from URL
def get_video_id(youtube_url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)'
    match = re.match(pattern, youtube_url)
    if match:
        return match.group(1)
    else:
        return None

# Function to format transcript with questions, answers, and proper spacing
def format_transcript(transcript):
    formatted_transcript = ""
    prev_speaker = None
    for text in transcript:
        speaker = text.get('speaker', None)
        if speaker != prev_speaker:
            if formatted_transcript and formatted_transcript[-1] != '\n':
                formatted_transcript += '\n'
        if text['text'].endswith(('?', '.', '!')):
            formatted_transcript += text['text'] + '\n\n'
        else:
            formatted_transcript += text['text'] + ' '
        prev_speaker = speaker
    return formatted_transcript.strip()

# Function to transcribe YouTube video
def transcribe_youtube_video(youtube_url):
    video_id = get_video_id(youtube_url)
    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            if transcript:
                formatted_transcript = format_transcript(transcript)
                return formatted_transcript
            else:
                st.error("No transcript available for the video.")
                return None
        except NoTranscriptFound:
            st.error("No transcript found for the video.")
            return None
        except TranscriptsDisabled:
            st.error("Transcripts are disabled for this video. Please try another video.")
            return None
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None
    else:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
        return None

# Streamlit app
st.title("Multilingual YouTube Video Transcriber")

youtube_url = st.text_input("Enter YouTube URL")

if st.button("Generate Transcript"):
    if youtube_url:
        transcript = transcribe_youtube_video(youtube_url)
        if transcript:
            st.success("Transcript generated successfully!")
            st.text_area("Transcript", transcript, height=300)
            
            # Creating a downloadable text file in bytes
            transcript_file = BytesIO(transcript.encode('utf-8'))

            st.download_button(
                label="Download Transcript",
                data=transcript_file,
                file_name="transcript.txt",
                mime="text/plain"
            )
    else:
        st.warning("Please enter a valid YouTube URL.")
