"""
有n只猴子，第i只猴子每过xi小时会连续吃香蕉yi小时。猴子从第二次开始每次休息结束后这只猴子连续吃香蕉的时间会增加zi小时。
给定n只猴子，每一只的xi，yi，zi，以及时间t，求在前t小时中，所有猴子共吃了多少小时。
 对于一只猴子来说是这样的：
从第1小时开始：
休息xi小时( 1 -> xi )
吃yi小时( xi + 1 -> xi + yi )
休息xi小时
吃yi+zi小时
休息xi小时
吃yi+zi+zi小时
......

输入描述：
第一行两个数n和t;

之后n行，第i+1行每行三个数xi,yi,zi.


输出描述：
一行一个数表示答案.

输入

10 100000000
1 0 0
1 0 5
1 2 2
1 2 8
1 3 0
1 5 0
1 5 2
1 5 5
1 7 0
1 8 3

输出
845787522
对于问题：查找在T时间内最大能吃，或者最小，采用二分法去查找，不断地去跟

，求每个猴子吃香蕉的区间由y和x和z三部分组成，于是可以直接枚举猴子吃香蕉的次数算出来每段区间，这里用个等差数列求和，然后判断完了之后，因为猴子是先休息再吃

#include<bits/stdc++.h>

using namespace std;

const int maxn=100005;
#define int long long
struct node {
    int x,y,z;
}mo[maxn];
int n,t;
bool check(int x,int y,int z,int mid)
{
    long long x1=mid*(x+y)+(((mid)*(mid-1))/2)*z;
    if(x1<0||x1>t) return false;
    return true;
}
signed main()
{
    int i;
    cin>>n>>t;
    for(i=0;i<n;i++)
    {
        cin>>mo[i].x>>mo[i].y>>mo[i].z;
    }
    long long ans1=0;
    for(i=0;i<n;i++)
    {
        int l=0,r=2000000005;
        while(l<r)
        {
            int mid=l+r+1ll>>1ll;
            if(check(mo[i].x,mo[i].y,mo[i].z,mid))
            {
                l=mid;
            }
            else
            {
                r=mid-1;
            }
        }
        ans1+=l*(mo[i].y)+(l*(l-1))/2*mo[i].z;
        if((t-l*(mo[i].y)-((l*(l-1))/2)*mo[i].z-(l+1)*mo[i].x)>0)
        {
            ans1+=(t-l*(mo[i].y)-((l*(l-1))/2)*mo[i].z-(l+1)*mo[i].x);
        }
    }
    cout<<ans1<<endl;
    return 0;
"""

class Solution:
    def main(self):
        n,t = map(int,input().split())

        x = []
        y = []
        z = []
        for i in range(n):
            x_i,y_i,z_i = map(int,input().split())
            x.append(x_i)
            y.append(y_i)
            z.append(z_i)

        # n个猴子的等差数列，每个猴子以z[i]的差别进行累计 sum = (x[i] + y[i]) * n + (n-1)*n/2 * z[i]
        # 二分查找，mid不断地去寻找n，使得等差和逼近t,当大于t，那么减少范围high = mid，如果小于t那么low = mid + 1

        def check(x,y,z,mid,t):
            sum_ = (x + y) * mid + (((mid-1)*mid) // 2) * z
            if sum_ < 0 or sum_ > t:
                return False
            return True

        sum_1 = 0
        m = 0
        # 其实是对于每一个猴子都要二分查找一次mid，每个猴子有自己mid，然后利用sum_1的计数器，得出最后的结果
        for i in range(n):
            if y[i] == 0 and z[i] == 0:
                continue
            low = 0
            high = 100000005
            while low < high:
                mid = (low + high) >> 1
                if check(x[i],y[i],z[i],mid,t):
                    low = mid + 1
                    m = mid
                else:
                    high = mid
            # 统计吃的时间，不算休息x
            sum_1 += (y[i]) * m + ((m - 1) * m) // 2 * z[i]
            # 计算去除下一次休息的时间，还有多长时间，这个时间就是剩余吃的时间
            sum_2 = t - ((y[i] + x[i]) * m + ((m - 1) * m) // 2 * z[i] + x[i])
            if (sum_2) > 0:
                sum_1 += sum_2
        return sum_1

s =Solution()
print(s.main())