from .jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)

    all_types = set()

    for job in all_jobs:
        all_types.add(job["job_type"])

    return all_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    all_jobs = read(path)

    all_industries = set()

    for job in all_jobs:
        if (job["industry"] != ""):
            all_industries.add(job["industry"])

    return all_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    all_jobs = read(path)

    max_salary = 0

    for job in all_jobs:
        if (
            job["max_salary"].isnumeric() and
            int(job["max_salary"]) > int(max_salary)
        ):
            max_salary = job["max_salary"]

    return max_salary


def get_min_salary(path):
    all_jobs = read(path)

    min_salary = 999999999999999999

    for job in all_jobs:
        if (
            job["max_salary"].isnumeric() and
            int(job["max_salary"]) < int(min_salary)
        ):
            min_salary = int(job["max_salary"])

    return min_salary


def salary_range_valid(job, salary):
    if (
        type(job["max_salary"]) != int or type(job["min_salary"]) != int or
        type(salary) != int
    ):
        return True
    if job["min_salary"] > job["max_salary"]:
        return True


def matches_salary_range(job, salary):
    try:
        salary_max = job["max_salary"]
        salary_min = job["min_salary"]
    except KeyError:
        raise ValueError
    if salary_range_valid(job, salary):
        raise ValueError
    return (salary_min <= salary <= salary_max)


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
