from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "src/jobs.csv"
    jobs = read_brazilian_file(path)

    for job in jobs:
        assert 'title' in job
        assert 'titulo' not in job
        assert 'salary' in job
        assert 'salario' not in job
        assert 'type' in job
        assert 'tipo' not in job
