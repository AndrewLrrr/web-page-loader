import os
import re
from typing import Optional
from urllib.parse import urlsplit, urlunsplit

SAFE_PATH_CHARS = re.compile(r'[^A-Za-z0-9]+')


def to_file_name(url: str, extension: Optional[str] = None) -> str:
    url_obj = urlsplit(url)

    paths = os.path.splitext(url_obj.path)

    if len(paths) == 2 and extension is None:
        extension = paths[1].lstrip('.')
        url_obj = url_obj._replace(path=paths[0])
        url = urlunsplit(url_obj)

    if url_obj.scheme:
        url = url.split('//')[-1]

    name = SAFE_PATH_CHARS.sub('-', url.strip('/'))

    if extension:
        name = '{}.{}'.format(name, extension)

    return name


def to_dir_name(url: str) -> str:
    name = '{}_files'.format(to_file_name(url, extension='').split('.')[0])
    return name