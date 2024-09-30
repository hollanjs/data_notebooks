from collections import Counter


class FriendData:
    def update_friendship(self, user_id1: int, user_id2: int):
        self.friendships[user_id1].append(user_id2)
        self.friendships[user_id2].append(user_id1)

    def add_user(self, name: str):
        new_id = len(self.users)
        self.users.append({"id": new_id, "name": name})
        self.friendships[new_id] = []

    def add_friend(self, user_id1: int, user_id2: int):
        if(user_id2 in self.friendships[user_id1]):
            return

        new_friendship = (user_id1, user_id2)
        self.friendship_pairs.append(new_friendship)
        self.update_friendships(new_friendship)

    def add_friend(self, name1: str, name2: str):
        # if more than 1 user has the same name, throw
        try:
            users_with_name1 = [user for user in self.users if user["name"] == name1]
            assert len(users_with_name1) == 1
            
            users_with_name2 = [user for user in self.users if user["name"] == name2]
            assert len(users_with_name2) == 1

            # DRY:: Get IDs and run the ID version of self.make_friends()
            name1_id = users_with_name1[0]["id"]
            name2_id = users_with_name2[0]["id"]
            self.make_friends(name1_id, name2_id)
        except Exception as e:
            non_unique_names = ", ".join([x 
                                          for x in [((len(users_with_name1)-1) * name1), 
                                                    ((len(users_with_name2)-1) * name2)]
                                          if x != ''])
            raise Exception(f"""
                The following names are not unique: {non_unique_names}
                Please try again either with IDs, or more make names more specific...
            """)


    def number_of_friends(self, user):
        """How many friends a user has"""
        user_id = user["id"]
        friend_ids = self.friendships[user_id]
        return len(friend_ids)
    

    def number_of_friends_by_id(self, sort_descending: bool = False):
        friend_count = [(user["id"], self.number_of_friends(user)) for user in self.users]
        if(sort_descending):
            friend_count.sort(
                key=lambda id_and_friends: id_and_friends[1],
                reverse=True
            )
        return friend_count
    

    def print_friend_status(self, sort_descending: bool = False):
        for user in self.number_of_friends_by_id(sort_descending):
            print(f'{self.users[user[0]]["name"]} has {user[1]} friends')


    def friends_of_friends(self, user):
        return Counter(
            foaf_id
            for friend_id in self.friendships[user["id"]]        # foreach of my friends
            for foaf_id in self.friendships[friend_id]        # get their friends 
            if foaf_id != user["id"]                        # only if that friend is not me
            and foaf_id not in self.friendships[user["id"]]      # and i'm not already friends with them
        )
    

    def total_connections(self):
        return sum(self.number_of_friends(user) for user in self.users)
    
    
    def __init__(self):
        # Pre-loaded sample data
        self.users = [
            { "id": 0, "name": "Hero" },
            { "id": 1, "name": "Dunn" },
            { "id": 2, "name": "Sue" },
            { "id": 3, "name": "Chi" },
            { "id": 4, "name": "Thor" },
            { "id": 5, "name": "Clive" },
            { "id": 6, "name": "Hicks" },
            { "id": 7, "name": "Devin" },
            { "id": 8, "name": "Kate" },
            { "id": 9, "name": "Klein" }
        ]

        # Pre-loaded sample data
        self.friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                            (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

        self.friendships = {}

        self.friendships = {user["id"]: [] for user in self.users}
        for i, j in self.friendship_pairs:
            self.update_friendship(i, j)