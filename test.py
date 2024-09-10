jobs_data = [
    {'job_title': 'Data Scientist', 'job_skills': ['Python', 'Machine Learning'], 'remote': True},
    {'job_title': 'Data Analyst', 'job_skills': ['Excel', 'SQL'], 'remote': False},
    {'job_title': 'Data Engineer', 'job_skills': ['Python', 'SQL'], 'remote': True},
    {'job_title': 'Data Architect', 'job_skills': ['Python', 'SQL', 'ETL'], 'remote': False},
    {'job_title': 'Machine Learning Engineer', 'job_skills': ['Machine Learning'], 'remote': True}
]

filtered_data = list(filter(lambda job: job['remote'] and "Python" in job['job_skills'], jobs_data))
for job in filtered_data:
    print(f"Job Title: {job['job_title']}")
    print(f"Job Skills: {', '.join(job['job_skills'])}")
    print("Remote: Yes\n" if job['remote'] else "Remote: No\n")