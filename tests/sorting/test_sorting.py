from src.sorting import sort_by
from src.jobs import read
import pytest


# Usar @pytest.fixture antes de uma função fora do escopo do teste
# que ira ser usado no mesmo, Não se aplica a exportações.
@pytest.fixture
def jobs():
    jobs = read("src/jobs.csv")
    return jobs


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "19857"
    assert jobs[-1]["min_salary"] == ""
    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "383416"
    assert jobs[-1]["max_salary"] == ""
    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-05-08"
    assert jobs[-1]["date_posted"] == "2020-04-05"


# sort_by(jobs, "date_posted")
# print(jobs)
