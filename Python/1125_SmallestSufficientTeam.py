"""
In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
"""


from typing import List
from collections import defaultdict
from functools import lru_cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        @lru_cache(None)
        def dp(status):
            # print(status)
            if status == target:
                return []
            len_res, res = float('inf'), None
            for j in range(len_skills):
                if status & (1 << j) == 0:
                    for p in skilled_people[j]:

                        s2 = status | p_skill[p]
                        tmp = dp(s2)
                        if len(tmp) < len_res:
                            len_res = len(tmp)
                            res = [p] + tmp
            return res

        
        skilled_people = defaultdict(list)  # key : index of skill, value: list of index of people who got the skill
        len_skills, len_p = len(req_skills), len(people)
        p_skill = [0] * len_p  # binary representation of people's skills
        target = (1 << len_skills) - 1
        # print(target, bin(target))
        skill_index = dict([(v, i) for i, v in enumerate(req_skills)])  # index : skill_name
        # print(skill_index, skilled_people)
        for _i, _skills in enumerate(people):
            v = 0
            for _skill in _skills:
                _j = skill_index[_skill]
                skilled_people[_j].append(_i)
                v |= (1 << _j)
            p_skill[_i] = v
        # print(skilled_people)
        # print([bin(i) for i in p_skill])
        return dp(0)


from typing import List
from collections import defaultdict
from functools import lru_cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        @lru_cache(None)
        def dp(status):
            if status == target:
                return []
            len_res, res = float('inf'), None
            for j in range(len_skills):
                if status & (1 << j) == 0:
                    for p in skilled_people[j]:
                        s2 = status | p_skill[p]
                        tmp = dp(s2)
                        if len(tmp) < len_res:
                            len_res = len(tmp)
                            res = [p] + tmp
            return res

        skilled_people = defaultdict(list)  # key : index of skill, value: list of index of people who got the skill
        len_skills, len_p = len(req_skills), len(people)
        p_skill = [0] * len_p  # binary representation of people's skills
        target = (1 << len_skills) - 1
        skill_index = dict([(v, i) for i, v in enumerate(req_skills)])  # index : skill_name
        for _i, _skills in enumerate(people):
            v = 0
            for _skill in _skills:
                _j = skill_index[_skill]
                skilled_people[_j].append(_i)
                v |= (1 << _j)
            p_skill[_i] = v
        return dp(0)

S = Solution()
req_skills = ["java","nodejs","reactjs"]
people = [["java"],["nodejs"],["nodejs","reactjs"]]
print(S.smallestSufficientTeam(req_skills, people))

req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
print(S.smallestSufficientTeam(req_skills, people))
