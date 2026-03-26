import requests
import os

API_URL = "https://fcapi.amitbala1993.workers.dev"

def fetch_and_build_m3u():
    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        m3u_content = "#EXTM3U\n"
        
        for match in data.get("matches", []):
            title = match.get("tournament", "Live Match")
            match_name = match.get("match", "")
            category = match.get("category", "Sports")
            logo = match.get("image", "")
            
            # Prefer 1080p, fallback to default stream_url
            resolutions = match.get("all_resolutions", {})
            stream_url = resolutions.get("1080p") or match.get("stream_url")
            
            if stream_url:
                m3u_content += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{category}", {match_name} - {title}\n'
                m3u_content += f'{stream_url}\n'
        
        with open("playlist.m3u", "w") as f:
            f.write(m3u_content)
            
        print("Playlist updated successfully.")
    except Exception as e:
        print(f"Error updating playlist: {e}")

if __name__ == "__main__":
    fetch_and_build_m3u()
