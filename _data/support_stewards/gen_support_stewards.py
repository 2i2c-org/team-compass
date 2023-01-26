import os
from collections import OrderedDict
from pathlib import Path
from textwrap import dedent, indent

from slack_sdk import WebClient


class SlackUsergroupMembers:
    """Find the members of a given Slack usergroup"""

    def __init__(self):
        token = os.environ.get("SLACK_BOT_TOKEN", None)
        if token is None:
            print("SLACK_BOT_TOKEN does not exist. Skipping Support Steward table generation...")

        self.client = WebClient(token=token)

    def _get_usergroup_id(self, usergroup_name):
        """Retrieve the ID of a named Slack usergroup
        
        Args:
            usergroup_name (str): The display name of the desired Slack
                usergroup
        """
        # List all usergroups in the workspace
        response = self.client.api_call(api_method="usergroups.list")

        # Find ID for the given usergroup
        index = next(
            idx
            for (idx, usergroup) in enumerate(response["usergroups"])
            if usergroup["handle"] == usergroup_name
        )

        self.usergroup_id = response["usergroups"][index]["id"]

    def _get_user_ids(self, usergroup_name):
        """
        Retrieve the user IDs of the members of a given usergroup
        """
        self._get_usergroup_id(usergroup_name)

        # Find all user IDs in the usergroup
        response = self.client.api_call(
            api_method="usergroups.users.list",
            params={"usergroup": self.usergroup_id},
        )
        self.user_ids = response["users"]
        return self.user_ids

    def _retrieve_users_names_and_pics(self, user_id):
        """For a given user ID, retrieve their 'real name', or display name if
        available, and their profile picture

        Args:
            user_id (str): A Slack user ID

        Returns:
            username (str): The 'real name' or display name associated with the
                given user ID
            avatar_url (str): A URL to the Slack avatar of a given user ID
        """
        # Convert user IDs to 'real names', or 'display names' if available
        response = self.client.api_call(
            api_method="users.info",
            params={"user": user_id},
        )

        username = response["user"]["profile"]["real_name"]
        if username == "":
            username = response["user"]["profile"]["display_name"]
        
        avatar_url = response["user"]["profile"]["image_512"]

        return username, avatar_url

    def get_users_in_usergroup(self, usergroup_name):
        """Retrieve the members of a Slack usergroup

        Returns:
            dict: A dictionary of members of a Slack usergroup. Keys are the
                Slack users' 'real names', or display names if available, and
                values are a URL pointing to the user's avatar
        """
        self._get_user_ids(usergroup_name)

        usernames_and_avatars = {}
        for user_id in self.user_ids:
            username, avatar_url = self._retrieve_users_names_and_pics(user_id)
            usernames_and_avatars[username] = avatar_url

        # Sort the dictionary alphabetically by key, i.e., display names
        usernames_and_avatars = OrderedDict(sorted(usernames_and_avatars.items()))

        return usernames_and_avatars


def main():
    # Get support stewards usernames and avatars
    slack = SlackUsergroupMembers()
    usernames_and_avatars = slack.get_users_in_usergroup("support-stewards")

    # Set filepaths
    data_path = Path(__file__).parent
    support_stewards_file = data_path.joinpath("support-stewards.txt")

    # Begin rST definition of grid with cards
    grid_md = dedent("""
        `````{grid} 1 2 3 3
        :gutter: 3
        :class-container: contributor-grid

        {card_md}
        `````
        """)

    # Add cards for the support stewards to the grid
    card_md = ""
    for user, avatar_url in usernames_and_avatars.items():
        # Create the card rST. Needs to be indented underneath its parent
        card_md += indent(
            dedent(f"""
        ````{{grid-item-card}}
        :class-header: bg-light
        :text-align: center

        **{user}**

        ^^^

        ```{{image}} {avatar_url}
        ```
        ````
        """))

    # Add the md for the sphinx design cards inside
    final_md = grid_md.format(card_md=card_md)

    # Write an rST snippet to include in the docs
    support_stewards_file.write_text(final_md + "\n")


if __name__ == "__main__":
    main()
