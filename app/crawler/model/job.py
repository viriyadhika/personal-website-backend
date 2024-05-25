from .company import Company

JOB_TABLE = "job"


class JobColumn:
    id = "id"
    job_id = "job_posting_id"
    company = "company"
    name = "job_name"
    link = "link"
    description = "description"


class Job:
    def __init__(
        self,
        id: str,
        title: str = "",
        company: Company = Company(""),
        link: str = "",
        description: str = "",
    ) -> None:
        self.id = id
        self.title = title
        self.link = link
        self.company = company
        self.description = description

    def get_dictionary(self):
        dictionary = {
            JobColumn.job_id: self.id,
            JobColumn.name: self.title,
            JobColumn.link: self.link,
            JobColumn.company: self.company.id,
            JobColumn.description: self.description,
        }
        return dictionary

    def __str__(self):
        dictionary = self.get_dictionary()
        return f"""
      {dictionary}
      company: {self.company}
    """
