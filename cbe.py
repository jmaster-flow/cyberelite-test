#!/usr/bin/env python
import preprocessing

mysql = {
    "host": "cyberelite.co",
    "user": "root",
    "passwd": "12345678",
    "db": "myBreach",
}
preprocessing_queue = [
    preprocessing.scale_and_center,
    preprocessing.dot_reduction,
    preprocessing.connect_lines,
]
site_name = "Deves.co.th"
use_anonymous = True
