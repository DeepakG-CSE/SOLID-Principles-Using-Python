'''
Dependency Inversion Principle

Dependency should be on abstractions not concretions:
 A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
 B. Abstractions should not depend on details. Details should depend upon abstractions.

There comes a point in software development where our app will be largely
composed of modules.  When this happens, we have to clear things up by using
dependency injection.  High-level components depending on low-level components
to function.

If our code follows OCP and LSP, then it will implicitly aligned to be compliant to the DIP
'''

from enum import Enum
from abc import ABCMeta , abstractmethod

class teams(Enum):
    blue_team = 1
    Red_team = 2
    Green_team = 3

class TeamMembershipLookup():
    @abstractmethod
    def find_all_students_of_team(self,team):
        pass
class Student:
    def __init__(self,name):
        self.name = name
class TeamMemberships(TeamMembershipLookup):
    def __init__(self):
        self.team_memberships = []
    def add_team_memebrships(self,student,team):
        self.team_memberships.append((student,team))
    def find_all_students_of_team(self,team):
        for members in self.team_memberships:
            if members[1]==team:
                yield members[0].name
class Analysis():
    def __init__(self , team_membership_lookup):
        for student in team_membership_lookup.find_all_students_of_team(teams.Red_team):
            print(f'{student} is in RED TEAM')
student1=Student('Ravi')
student2=Student('Harry')
student3=Student('Zayn')

team_memberships = TeamMemberships()
team_memberships.add_team_memebrships(student1 , teams.blue_team)
team_memberships.add_team_memebrships(student2 , teams.Red_team)
team_memberships.add_team_memebrships(student3 , teams.Green_team)

Analysis(team_memberships)


"""
To comply with the Dependency Inversion Principle, we need to ensure that high-level class Analysis should not depend on the concrete implementation of low-level class TeamMemberships.
Instead, it should depend on some abstraction.
So, we create an interface TeamMembershipLookup that contains an abstract method find_all_students_of_team which is passed to any class that inherits from this interface. We make our TeamMembership class inherit from this interface and hence now TeamMembership class needs to provide an implementation of the find_all_students_of_team function.
This function then yields the results to any other calling entity. We moved the processing that was done in the high-level Analysis class to TeamMemberships class through the interface TeamMembershipLookup.
So, by doing this we have removed the dependency of high-level class Analysis from low-level class TeamMemberships and transferred this dependency to interface TeamMembershipLookup. Now the high-level class doesn’t depend on the implementation details of the low-level class.
Any changes to the implementation details of the low-level class don’t impact the high-level class.
"""
