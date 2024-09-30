import pytest
import Modules.Friends

# Reload module, because of ongoing development while writing notebook
from importlib import reload 
reload(Modules.Friends)


def test_FriendsClassInitializesWithoutIssue():
    friends_obj = Modules.Friends.FriendData()
    assert type(friends_obj) is Modules.Friends.FriendData

def test_InitializedWithSampleUserbase():
    friends_obj = Modules.Friends.FriendData()
    assert friends_obj.users == [{'id': 0, 'name': 'Hero'},
                                 {'id': 1, 'name': 'Dunn'},
                                 {'id': 2, 'name': 'Sue'},
                                 {'id': 3, 'name': 'Chi'},
                                 {'id': 4, 'name': 'Thor'},
                                 {'id': 5, 'name': 'Clive'},
                                 {'id': 6, 'name': 'Hicks'},
                                 {'id': 7, 'name': 'Devin'},
                                 {'id': 8, 'name': 'Kate'},
                                 {'id': 9, 'name': 'Klein'}]