class Solution:
    # 递归
    def main(self,s):
        s_list = list(s)
        ans = []
        def dfs(remain_list):
            if len(remain_list) == 0:
                ans.append(1)
                return
            if remain_list[0] == '0':
                return
            for i in [1,2]:
                if len(remain_list) < i:
                    continue
                if i == 2:
                    if ''.join(remain_list[:2]) >= '27':
                        continue
                dfs(remain_list[i:])
        
        dfs(s_list)
        return len(ans)
    # 动态规划
    def main1(self,s):
        ll = len(s)
        dp = [1] + [0] * ll # 空也是一种编码
        for i in range(1,ll+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i>=2 and s[i-2] != '0' and int(s[i-2:i]) <=26:
                dp[i] += dp[i-2]
        return dp[ll]

s = Solution()
string = '12'
# string = '126'
string = '06'
# string = '11106'
print(s.main1(string))