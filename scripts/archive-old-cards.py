from datetime import date
from datetime import timedelta
import pandas as pd
from ghapi.all import GhApi
from urllib.parse import quote
from rich.console import Console

console = Console()
api = GhApi()

project = "12135611"  # This is the Active board

# Iterate through cards and move them to the new column so Done is clear
done_column = "13714268"  # Done column on the Activity Board
archive_column = "14245354"  # Archive column on Activity Board
today = pd.to_datetime(date.today())

# Actually archive everything in the archive column so it's invisible
clear_archive_after_days = 28
archive_clear_cutoff = today.date() - timedelta(days=clear_archive_after_days)
archive_visible_cards = api.projects.list_cards(archive_column, archived_state="not_archived", per_page=100)
console.log("Moving visible cards to archive...")
for card in archive_visible_cards:
    # Archive entirely after 4 weeks since that is 2 cycles ago
    older_than_four_weeks = archive_clear_cutoff > pd.to_datetime(card['updated_at']).date()
    if older_than_four_weeks:
        api.projects.update_card(card['id'], archived=True)

# Move cards in "Done" to "Archive"
archive_after_days = 14
archive_cutoff = today.date() - timedelta(days=archive_after_days)
finished_cards = api.projects.list_cards(done_column, per_page=100)[::-1]
console.log("Clearning old cards in archive...")
for card in finished_cards:
    # Move from Done to Archive after 2 weeks since it's now time for a new cycle
    older_than_two_weeks = archive_cutoff > pd.to_datetime(card['updated_at']).date()
    if older_than_two_weeks:
        api.projects.move_card(card['id'], "top", int(archive_column))

console.log("Finished cleaning up activity board!")