#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
import json
from faker import Faker
import random

fake = Faker()


def gen_student_records(num_students: int) -> dict:
    students_db = {}

    for _ in range(num_students):
        student_id = str(fake.unique.random_int(min=10000, max=99999))
        student_record = {
            "name": fake.name(),
            "scores": {
                "math": random.randint(50, 100),
                "physics": random.randint(50, 100),
                "chemistry": random.randint(50, 100),
            },
        }

        students_db[student_id] = student_record

    return students_db


num = 1000
records = gen_student_records(num)

with open("students.json", "w") as fp:
    json.dump(records, fp, indent=2)
