#include <bits/stdc++.h>

using namespace std;
const int MAX=10;
struct Trie
{
  int endOfS;
  struct Trie* child[MAX];
};
struct Trie* newNode()
{
    struct Trie* cur=new Trie;
    cur->endOfS=0;
    for(int i=0;i<MAX;i++)
    {
        cur->child[i]=NULL;
    }
    return cur;
} 
int insertTrie(struct Trie* root,string s)
{
    struct Trie* cur=root;
    for(int i=0;i<s.length();i++)
    {
        int indx=s[i]-'a';
         
        if(cur->child[indx]==NULL)
           cur->child[indx]=newNode();
        cur=cur->child[indx];
        if(cur->endOfS==1)
            return 1;
    }
    cur->endOfS=1;
    for(int i=0;i<MAX;i++)
    {
        if(cur->child[i]!=NULL)
            return 1;
    }
        
    return 0;
}

int main()
{
    int n;
    cin>>n;
    string s;
    struct Trie* root=newNode();
    int flag;
    while(n--)
    {
        cin>>s;
        flag=insertTrie(root,s);
        if(flag)
           {
            cout<<"BAD SET"<<endl;
            cout<<s;
            break;
           }
        
    }
    if(flag==0)
        cout<<"GOOD SET";
    return 0;
}