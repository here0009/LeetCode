const int INF = 0x3f3f3f3f;

class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        int n = nums.size();
        vector<unordered_map<int, int>> groups(k);
        vector<int> size(k);
        for (int i = 0; i < k; ++i) {
            for (int j = i; j < n; j += k) {
                groups[i][nums[j]]++;
                size[i]++;
            }
        }
        //异或值为random，需要操作的最小次数
        vector<int> dp(1 << 10, INF);
        dp[0] = 0;
        //从左到右，考虑K区间的index i的处理
        //即在nums中所有映射在区间k中index 为 i的集合的元素修改方法
        for (int i = 0; i < k; ++i) {
            //讨论第一种情况，即i对应集合的值都修改为一个不存在该集合中的值，那么这个集合就要修改size[i]次
            /**
            dp的涵义：在当前index前，异或一个值需要操作的最小次数
            eg: 
            1. 此时i = 3, 在操作前三个集合，即[0, 1, 2]后，会获取多个异或值，并且都是此时获取该异或值的最小操作次数
            2. 要想修改i=3的集合后，操作最小，就在之前获取异或值中最小操作次数的基础上 + size[i];
                比如dp中此时获得55需要的次数最小，那么之后就以这个为基础，在 i=3对应的集合上修改
                修改后可以为任意值， 比如为获取99，只需将i=3的区间所有值都修改为 99^55就好
            */
            int lo = *min_element(dp.begin(), dp.end());
            vector<int> ndp(1 << 10, lo + size[i]);


            // 讨论第二种情况
            /**
            1. 之前考虑的都是集合i中元素都修改为集合i中没有的数字，那么对于集合i而言，它的修改次数是固定的，
                    所以只要求之前需要修改的次数的最小值就可以获取最小值
            2. 可是存在另一种情况，即修改值存在集合i中，那么对于集合i修改的次数就是变量，为 size[i] - group[i][val]
                1. 在修改集合i的次数值为变值时，就需要枚举全部情况
                2. 以val^val`为例
                    1. 因为可能存在 之前集合操作变成 val`的次数不是最小，但是加上size[i] - group[i][val]后
                        其值比 size[i] + min(dp[random])要小
            */
            for (int j = 0; j < (1 << 10); ++j) {
                if (dp[j] == INF)
                    continue;
                for (auto [p, freq] : groups[i]) {
                    int nxt = p ^ j;
                    ndp[nxt] = min(ndp[nxt], dp[j] + size[i] - freq);
                }
            }
            // 将ndp copy给dp，表示操作完i集合后，异或得到每个可能的值需要的最小操作数
            dp = move(ndp);
        }
        //从集合0开始到集合k-1，所有集合都讨论处理后，dp[0]就是获取0需要操作的最小次数
        return dp[0];
    }
};