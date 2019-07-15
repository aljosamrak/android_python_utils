import os
import re


def get_package_from_apk_info(apk):
    raw_data = os.popen("aapt dump badging %s | grep package:\ name" % apk).read()

    regex = "package: name='(?P<package_name>[\w.]+)' versionCode='(?P<version_code>\d+)' versionName='(?P<version_name>[\w.]+)'"
    matches = re.search(regex, raw_data)

    return {
        "package": matches.group(1),
        "code": matches.group(1),
        "name": matches.group(1)
    }
