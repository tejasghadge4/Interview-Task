import os
import subprocess
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_google_drive_link_map
from django.views.decorators.csrf import csrf_exempt

LOCAL_FOLDER = settings.TEXT_FILES_DIR

def index(request):
    if not os.path.exists(LOCAL_FOLDER):
        os.makedirs(LOCAL_FOLDER)

    local_files = [f for f in os.listdir(LOCAL_FOLDER) if f.endswith('.txt')]
    all_files = list(get_google_drive_link_map().keys())
    unique_files = sorted(set(local_files + all_files))

    return render(request, 'viewer/index.html', {'files': unique_files})
# Helper function to search file in common drives (Windows example)
def find_file_on_local_system(filename):
    # You can customize these roots according to your environment
    search_roots = ['C:\\', 'D:\\', 'E:\\']  # Add drives you want to scan

    for root in search_roots:
        for dirpath, dirnames, filenames in os.walk(root):
            if filename in filenames:
                return os.path.join(dirpath, filename)
    return None

@csrf_exempt
def check_file(request):
    import json
    data = json.loads(request.body)
    filename = data.get('filename')

    file_path = find_file_on_local_system(filename)

    if file_path:
        try:
            subprocess.Popen(['notepad.exe', file_path])
            return JsonResponse({'exists': True})
        except Exception as e:
            return JsonResponse({'exists': True, 'error': str(e)})
    else:
        drive_links = get_google_drive_link_map()
        return JsonResponse({
            'exists': False,
            'download_url': drive_links.get(filename)
        })
