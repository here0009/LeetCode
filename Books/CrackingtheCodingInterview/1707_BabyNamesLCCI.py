"""
Each year, the government releases a list of the 10000 most common baby names and their frequencies (the number of babies with that name). The only problem with this is that some names have multiple spellings. For example,"John" and ''Jon" are essentially the same name but would be listed separately in the list. Given two lists, one of names/frequencies and the other of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and Johnny are synonyms. (It is both transitive and symmetric.) In the final list, choose the name that are lexicographically smallest as the "real" name.

Example:

Input: names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
Output: ["John(27)","Chris(36)"]
Note:

names.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/baby-names-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import Counter
import re
class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:

        def find(name):
            if name not in root:
                root[name] = name
            if root[name] == name:
                return name
            r_name = find(root[name])
            root[name] = r_name
            return root[name]

        def union(n1, n2):
            r_n1, r_n2 = find(n1), find(n2)
            if r_n1 == r_n2:  # do not miss that
                return False
            if r_n1 > r_n2:
                r_n1, r_n2 = r_n2, r_n1
            root[r_n2] = r_n1
            name_counts[r_n1] += name_counts[r_n2]
            name_counts[r_n2] = 0
            return True

        name_counts = Counter()
        pattern = re.compile(r'(\w+)\((\d+)\)')
        syn_pattern = re.compile(r'\((\w+),(\w+)\)')
        root = dict()
        for name in names:
            tmp = pattern.match(name)
            _n, _c = tmp[1], int(tmp[2])
            name_counts[_n] += _c
        for syn in synonyms:
            tmp = syn_pattern.match(syn)
            _n1, _n2 = tmp[1], tmp[2]
            union(_n1, _n2)
        res = []
        for key, val in name_counts.items():
            if val > 0:
                res.append("{}({})".format(key, val))
        return res



S = Solution()
names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"]
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
print(S.trulyMostPopular(names, synonyms))

names = ["Pwsuo(71)","Prf(48)","Rgbu(49)","Zvzm(31)","Xxcl(25)","Bbcpth(42)","Padz(70)","Jmqqsj(19)","Uwy(26)","Jylbla(65)","Xioal(11)","Npbu(62)","Jpftyg(96)","Tal(46)","Hnc(100)","Yldu(85)","Alqw(45)","Wbcxi(34)","Kxjw(36)","Clplqf(8)","Fayxe(66)","Slfwyo(48)","Xbesji(70)","Pmbz(22)","Oip(2)","Fzoe(63)","Qync(79)","Utc(11)","Sqwejn(19)","Ngi(8)","Gsiiyo(60)","Bcs(73)","Icsvku(1)","Yzwm(92)","Vaakt(21)","Uvt(70)","Axaqkm(100)","Gyhh(84)","Gaoo(98)","Ghlj(35)","Umt(13)","Nfimij(52)","Zmeop(77)","Vje(29)","Rqa(47)","Upn(89)","Zhc(44)","Slh(66)","Orpqim(69)","Vxs(85)","Gql(19)","Sfjdjc(62)","Ccqunq(93)","Oyo(32)","Bvnkk(52)","Pxzfjg(45)","Kaaht(28)","Arrugl(57)","Vqnjg(50)","Dbufek(63)","Fshi(62)","Lvaaz(63)","Phlto(41)","Lnow(70)","Mqgga(31)","Adlue(82)","Zqiqe(27)","Mgs(46)","Zboes(56)","Dma(70)","Jnij(57)","Ghk(14)","Mrqlne(39)","Ljkzhs(35)","Rmlbnj(42)","Qszsny(93)","Aasipa(26)","Wzt(41)","Xuzubb(90)","Maeb(56)","Mlo(18)","Rttg(4)","Kmrev(31)","Kqjl(39)","Iggrg(47)","Mork(88)","Lwyfn(50)","Lcp(42)","Zpm(5)","Qlvglt(36)","Liyd(48)","Jxv(67)","Xaq(70)","Tkbn(81)","Rgd(85)","Ttj(28)","Ndc(62)","Bjfkzo(54)","Lqrmqh(50)","Vhdmab(41)"]
synonyms = ["(Uvt,Rqa)","(Qync,Kqjl)","(Fayxe,Upn)","(Maeb,Xaq)","(Pmbz,Vje)","(Hnc,Dma)","(Pwsuo,Gyhh)","(Gyhh,Aasipa)","(Fzoe,Lcp)","(Mgs,Vhdmab)","(Qync,Rgd)","(Gql,Liyd)","(Gyhh,Tkbn)","(Arrugl,Adlue)","(Wbcxi,Slfwyo)","(Yzwm,Vqnjg)","(Lnow,Vhdmab)","(Lvaaz,Rttg)","(Nfimij,Iggrg)","(Vje,Lqrmqh)","(Jylbla,Ljkzhs)","(Jnij,Mlo)","(Adlue,Zqiqe)","(Qync,Rttg)","(Gsiiyo,Vxs)","(Xxcl,Fzoe)","(Dbufek,Xaq)","(Ccqunq,Qszsny)","(Zmeop,Mork)","(Qync,Ngi)","(Zboes,Rmlbnj)","(Yldu,Jxv)","(Padz,Gsiiyo)","(Oip,Utc)","(Tal,Pxzfjg)","(Adlue,Zpm)","(Bbcpth,Mork)","(Qync,Lvaaz)","(Pmbz,Qync)","(Alqw,Ngi)","(Bcs,Maeb)","(Rgbu,Zmeop)"]
print(S.trulyMostPopular(names, synonyms))
out = ["Prf(48)","Zvzm(31)","Bbcpth(256)","Jmqqsj(19)","Uwy(26)","Jylbla(100)","Xioal(11)","Npbu(62)","Jpftyg(96)","Alqw(146)","Kxjw(36)","Clplqf(8)","Fayxe(155)","Slfwyo(82)","Xbesji(70)","Oip(13)","Fzoe(130)","Sqwejn(19)","Gsiiyo(215)","Bcs(262)","Icsvku(1)","Vaakt(21)","Axaqkm(100)","Gaoo(98)","Ghlj(35)","Umt(13)","Rqa(117)","Zhc(44)","Slh(66)","Orpqim(69)","Gql(67)","Sfjdjc(62)","Ccqunq(186)","Oyo(32)","Bvnkk(52)","Pxzfjg(91)","Kaaht(28)","Vqnjg(142)","Fshi(62)","Phlto(41)","Lnow(157)","Mqgga(31)","Adlue(171)","Dma(170)","Jnij(75)","Ghk(14)","Mrqlne(39)","Rmlbnj(98)","Aasipa(262)","Wzt(41)","Xuzubb(90)","Kmrev(31)","Iggrg(99)","Lwyfn(50)","Qlvglt(36)","Jxv(152)","Ttj(28)","Ndc(62)","Bjfkzo(54)"]

exp = ["Gsiiyo(215)","Adlue(171)","Iggrg(99)","Umt(13)","Bbcpth(256)","Jxv(152)","Vqnjg(142)","Bvnkk(52)","Bcs(262)","Alqw(424)","Kmrev(31)","Bjfkzo(54)","Oip(13)","Qlvglt(36)","Clplqf(8)","Aasipa(262)","Sfjdjc(62)","Ccqunq(186)","Oyo(32)","Zhc(44)","Fayxe(155)","Ndc(62)","Wzt(41)","Xioal(11)","Mqgga(31)","Jpftyg(96)","Fshi(62)","Lnow(157)","Rmlbnj(98)","Ghk(14)","Jylbla(100)","Fzoe(130)","Orpqim(69)","Jnij(75)","Jmqqsj(19)","Kaaht(28)","Ttj(28)","Xuzubb(90)","Dma(170)","Slfwyo(82)","Gaoo(98)","Lwyfn(50)","Pxzfjg(91)","Gql(67)","Sqwejn(19)","Xbesji(70)","Mrqlne(39)","Ghlj(35)","Rqa(117)","Uwy(26)","Prf(48)","Axaqkm(100)","Npbu(62)","Kxjw(36)","Zvzm(31)","Icsvku(1)","Phlto(41)","Vaakt(21)","Slh(66)"]
pattern = re.compile(r'(\w+)\((\d+)\)')
out_counts, exp_counts = Counter(), Counter()
for name in out:
    tmp = pattern.match(name)
    _n, _c = tmp[1], int(tmp[2])
    out_counts[_n] += _c
for name in exp:
    tmp = pattern.match(name)
    _n, _c = tmp[1], int(tmp[2])
    exp_counts[_n] += _c
for k in set(set(out_counts.keys()) | set(exp_counts.keys())):
    if out_counts[k] != exp_counts[k]:
        print(k, out_counts[k], exp_counts[k])