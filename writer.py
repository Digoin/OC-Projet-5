from db_writer import Database
from config import CATEGORY_SEARCH


test=Database("")
test.delete_row()

for category in CATEGORY_SEARCH:
    test=Database(f"{category}")
    test.db_writer()

test.delete_short_category()