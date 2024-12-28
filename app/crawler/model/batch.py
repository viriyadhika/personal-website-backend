class BatchColumn:
    id = "id"
    keywords = "keywords"
    location = "job_location"
    batch_id = "batch_id"
    last_updated = "last_updated"


class BatchDto:
    def __init__(
        self, batch_id="", keywords="", location="", last_updated=None
    ) -> None:
        self.batch_id = batch_id
        self.location = location
        self.keywords = keywords
        self.last_updated = last_updated

    def get_dictionary(self):
        if self.last_updated == None:
            return {
                BatchColumn.batch_id: self.batch_id,
                BatchColumn.location: self.location,
                BatchColumn.keywords: self.keywords,
            }
        return {
            BatchColumn.batch_id: self.batch_id,
            BatchColumn.keywords: self.keywords,
            BatchColumn.location: self.location,
            BatchColumn.last_updated: self.last_updated,
        }

    def __str__(self) -> str:
        dictionary = {
            BatchColumn.batch_id: self.batch_id,
        }
        return dictionary.__str__()
