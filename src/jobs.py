from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        file_csv = csv.reader(file, delimiter=",", quotechar='"')

        acumulator = []

        for line in file_csv:
            obj = {
                "job_title": line[0],
                "company": line[1],
                "state": line[2],
                "city": line[3],
                "min_salary": line[4],
                "max_salary": line[5],
                "job_desc": line[6],
                "industry": line[7],
                "rating": line[8],
                "date_posted": line[9],
                "valid_until": line[10],
                "job_type": line[11],
                "id": line[12],
            }
            acumulator.append(obj)

    acumulator.pop(0)
    return acumulator
