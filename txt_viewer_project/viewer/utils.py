def get_google_drive_link_map():
    # Replace with your actual Google Drive shareable links
    return {
        "test1.txt": "https://drive.google.com/file/d/1x9MNjDliStEc3qEYWVgXM-iEi-CinxuS/view?usp=drive_link",
        "test2.txt": "https://drive.google.com/file/d/1VXBAQN_t1TrjRLoV9DfRxlnxMR99RN-w/view?usp=drive_link",
        "test3.txt":"https://drive.google.com/file/d/1LeakVUNxiSl3hyFjSJuriw6XJ08Hbuqv/view?usp=drive_link",
         "test4.txt":"https://drive.google.com/file/d/1Fr9WkWXCe67NkYlpvxv-t1hsHW5vzIeM/view?usp=drive_link",
         "test5.txt":"https://drive.google.com/file/d/1yfgz6pcUCzZSA6Gcfvaqmb6mzqs4ztJN/view?usp=drive_link"
    }
import win32com.client

def search_txt_file(filename_without_extension):
    try:
        es = win32com.client.Dispatch("ES.Application")
        es.Query = f"{filename_without_extension}.txt"  # Only search .txt files
        es.MaxResults = 5  # You can increase this if needed
        es.Sort = 5  # Sort by date modified descending

        for i in range(es.NumResults):
            path = es.GetResultFullPathName(i)
            if path.lower().endswith('.txt'):
                return path  # Return first matching .txt file

        return None
    except Exception as e:
        return None