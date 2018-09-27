import logging
import sbb.tools.logger
import json
from pathlib import Path, PurePath
from pprint import pprint

from sbb.tools import input_dir

logger = logging.getLogger('APIlogger')


def parse_input_paths(input_dir: str = input_dir):

    try:
        data_dir = Path(input_dir)
        cwd = Path.cwd()
        import pdb
        pdb.set_trace()
    else:
        
    finally:
        assert data_dir.is_dir(), "input path is not a directory"
    
    return sorted([x for x in data_dir.iterdir() if x.is_file()])


def parse_json_file(f_path: str):

    assert f_path.is_file(), "path needs to be a pathlib file path"
    try:
        f = f_path.open()
        data = json.load(f)
    except Exception as e:
        print(e)
        raise Exception(
            "{} is a corrupted file or cannot be parsed as json".format(
                str(f_path)))
    finally:
        f.close()
    return data
