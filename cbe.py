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
use_anonymous = True