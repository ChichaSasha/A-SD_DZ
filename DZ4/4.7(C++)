#include <iostream>
#include <set>
#include <climits>
using namespace std;

int inf = INT_MAX;

int main() {
    cin.sync_with_stdio(false);
    int n;
    cin >> n;
    int na;
    cin >> na;
    multiset<pair<int, int> > s;
    int a[na];
    int resa[n];
    for(int i=0; i<na; i++)
    {
        cin >> a[i];
        s.insert({a[i], a[i]});
    }
    for(int i=0; i<n; i++)
    {
        auto it=s.begin();
        int val=it->first;
        int t=it->second;
        s.erase(it);
        s.insert({val+t, t});
        resa[i]=val;
    }
    int nb;
    cin >> nb;
    int b[nb];
    for(int i=0; i<nb; i++)
    {
        cin >> b[i];
    }
    multiset<pair<int, int> > q;
    long long l=resa[n-1], r=10000100;
    while(l<r)
    {
        int w=0;
        int m=(l+r)/2;
        for(int i=0; i<nb; i++)
        {
            q.insert({b[i], b[i]});
        }
        q.insert({inf, inf});
        for(int i=n-1; i>=0; i--)
        {
            int y=m-resa[i];
            auto x=q.begin();
            if(y<(x->first))
            {
                w++;
                break;
            }
            else{
                auto it=q.lower_bound({y, -1});
                int z=it->first;
                if(z>y)
                    it--;
                int val=it->first;
                int t=it->second;
                q.erase(it);
                q.insert({val+t, t});
            }
        }
        if(w==0)
            r=m;
        else
            l=m+1;
        q.clear();
    }
    cout << l;
    return 0;
}