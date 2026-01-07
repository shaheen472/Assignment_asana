class Team:
    def __init__(
        self,
        team_id: str,
        org_id: str,
        name: str,
        description: str,
        function: str,
        created_at
    ):
        self.team_id = team_id
        self.org_id = org_id
        self.name = name
        self.description = description
        self.function = function
        self.created_at = created_at
