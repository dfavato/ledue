import os
from urllib.parse import unquote

from django.conf import settings
from django.http import FileResponse, Http404


def downloads(request, path):
    path = unquote(path)
    filename = os.path.basename(path)
    path = path.replace(' ', '_')
    file_path = os.path.join(
        settings.MEDIA_ROOT, path
    )
    print(file_path)
    if os.path.exists(file_path):
        response = FileResponse(
            open(file_path, 'rb'), as_attachment=True,
            filename=filename
        )
        return response
    raise Http404
