from app.db.migrate import ExtraScript, migrate
from app.crawler.model.job import JobColumn, JOB_TABLE
from app.crawler.model.company import CompanyColumn, COMPANY_TABLE
from app.crawler.model.batch_relationship import (
    BatchRelationshipColumn,
    BATCH_RELATIONSHIP_TABLE,
)
from app.crawler.model.batch import BatchColumn, BATCH_TABLE

TABLES = {}

TABLES[COMPANY_TABLE] = (
    f"CREATE TABLE `{COMPANY_TABLE}` ("
    f"`{CompanyColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{CompanyColumn.company_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{CompanyColumn.name}` varchar(100) NOT NULL,"
    f"`{CompanyColumn.link}` varchar(300),"
    f"`{CompanyColumn.employee}` varchar(25),"
    f"PRIMARY KEY (`{CompanyColumn.id}`)"
    f") ENGINE=InnoDB"
)

TABLES[BATCH_TABLE] = (
    f"CREATE TABLE `{BATCH_TABLE}` ("
    f"`{BatchColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{BatchColumn.batch_id}` varchar(100) UNIQUE NOT NULL,"
    f"`{BatchColumn.location}` varchar(100) NOT NULL,"
    f"`{BatchColumn.keywords}` varchar(100) NOT NULL,"
    f"`{BatchColumn.last_updated}` timestamp NOT NULL,"
    f"PRIMARY KEY (`{BatchRelationshipColumn.id}`)"
    f") ENGINE=InnoDB"
)

TABLES[JOB_TABLE] = (
    f"CREATE TABLE `{JOB_TABLE}` ("
    f"`{JobColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{JobColumn.job_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{JobColumn.name}` varchar(100) NOT NULL,"
    f"`{JobColumn.link}` varchar(300) NOT NULL,"
    f"`{JobColumn.company}` varchar(25) NOT NULL,"
    f"PRIMARY KEY (`{JobColumn.id}`), "
    f"FOREIGN KEY ({JobColumn.company}) REFERENCES {COMPANY_TABLE}({CompanyColumn.company_id}) ON DELETE CASCADE"
    f") ENGINE=InnoDB"
)


TABLES[BATCH_RELATIONSHIP_TABLE] = (
    f"CREATE TABLE `{BATCH_RELATIONSHIP_TABLE}` ("
    f"`{BatchRelationshipColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{BatchRelationshipColumn.batch_id}` varchar(100) NOT NULL,"
    f"`{BatchRelationshipColumn.job_id}` varchar(25) NOT NULL,"
    f"`{BatchRelationshipColumn.timestamp}` timestamp NOT NULL,"
    f"PRIMARY KEY (`{BatchRelationshipColumn.id}`), "
    f"FOREIGN KEY ({BatchRelationshipColumn.job_id}) REFERENCES {JOB_TABLE}({JobColumn.job_id}) ON DELETE CASCADE, "
    f"FOREIGN KEY ({BatchRelationshipColumn.batch_id}) REFERENCES {BATCH_TABLE}({BatchColumn.batch_id}) ON DELETE CASCADE"
    f") ENGINE=InnoDB"
)

EXTRA = [
    ExtraScript(
        "Create batch relationship unique index",
        (
            f"ALTER TABLE `{BATCH_RELATIONSHIP_TABLE}` "
            f"ADD UNIQUE `unique_index` (`{BatchRelationshipColumn.batch_id}`, `{BatchRelationshipColumn.job_id}`, `{BatchRelationshipColumn.timestamp}`);"
        ),
    ),
    ExtraScript(
        "Add description column to company table",
        (
            f"ALTER TABLE `{JOB_TABLE}` "
            f"ADD COLUMN {JobColumn.description} varchar(3000) "
        ),
    ),
]


def migrate_crawler():
    migrate(TABLES=TABLES, EXTRA=EXTRA)
