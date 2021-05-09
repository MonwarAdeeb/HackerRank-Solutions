#include <bits/stdc++.h>
using namespace std;

int numOfElements;            // first line
int inputArray[1000011];    // inputArray second line
int leftPart[1000011];        // Left part of array
int rightPart[1000011];        // Right Part of array
std::vector<int> lookupMatrix[1000011];        // Lookup Matrix
long long int binaryIndexTree[1000011];     // Binary Index Tree matrix representation

/*
 * Update a node in Binary Index Tree (BIT) at
 * a given index in BIT. The give value 'val'
 * is added to binaryIndexTree[i] and all (maxn)
 * of its ancestors in tree.
 */
void updateBinaryIndexTree(int ind, int val, int maxn) {
    while(ind <= maxn) {
        binaryIndexTree[ind] += val;
        ind += (ind & -ind);
    }
}

/*
 * Return minimum of elements in range from
 * index to the end of binary index tree.
 */
long long int rangeMinimumQuery(int index) {
    long long int ans = 0;
    while(index > 0) {
        ans += binaryIndexTree[index];
        index -= (index & -index);
    }
    return ans;
}

/*
 * Return the index of element in Disjoint Union Set (DSU)
 * by taking the element x and size of disjointSetUnionSize
 * as a parameters.
 */
int findElementIndexInDSU(int x, vector<int> disjointSetUnionSize) {
    if(disjointSetUnionSize.back() <= x) return disjointSetUnionSize.size();
    return upper_bound(disjointSetUnionSize.begin(), disjointSetUnionSize.end(), x) - disjointSetUnionSize.begin();
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> numOfElements;
    set<int> dsu;            // Disjoint Set Union
    unordered_map<int, int> disjointSetUnionMap;

    // Construct Disjoint Set Union.
    for(int i = 1; i <= numOfElements; i++) {
        cin >> inputArray[i];
        //assert(inputArray[i] >= 1 and inputArray[i] <= 1000000000);
        dsu.insert(inputArray[i]);
    }

    // Extract and Process Set Ordered Pairs
    vector<pair<long long int,long long int>> orderedPairs;
    for(int i = 1; i <= numOfElements; i++) {
        while(orderedPairs.size() > 0 and orderedPairs.back().first < inputArray[i]) orderedPairs.pop_back();
        if(orderedPairs.size() == 0) leftPart[i] = 1;
        else {
            leftPart[i] = orderedPairs.back().second + 1;
        }
        orderedPairs.push_back(make_pair(inputArray[i], i));
    }
    orderedPairs.clear();
    for(int i = numOfElements; i >= 1; i--) {
        while(orderedPairs.size() > 0 and orderedPairs.back().first <= inputArray[i]) orderedPairs.pop_back();
        if(orderedPairs.size() == 0) rightPart[i] = numOfElements;
        else {
            rightPart[i] = orderedPairs.back().second - 1;
        }
        orderedPairs.push_back(make_pair(inputArray[i], i));
    }

    // Add entry to Lookup Matrix
    for(int i = 1; i <= numOfElements; i++) {
        if(i - leftPart[i] <= rightPart[i] - i) {
            for(int j = leftPart[i]; j < i; j++) {
                lookupMatrix[i - 1].push_back(-inputArray[i] / inputArray[j]);
                lookupMatrix[rightPart[i]].push_back(inputArray[i] / inputArray[j]);
            }

            lookupMatrix[i].push_back(-1);
            lookupMatrix[rightPart[i]].push_back(1);
        } else {

            for(int j = i + 1; j <= rightPart[i]; j++) {
                lookupMatrix[leftPart[i] - 1].push_back(-inputArray[i] / inputArray[j]);
                lookupMatrix[i].push_back(inputArray[i] / inputArray[j]);
            }
            lookupMatrix[leftPart[i] - 1].push_back(-1);
            lookupMatrix[i - 1].push_back(1);
        }
    }

    int maxn = dsu.size() + 2;
    int cnt = 1;
    for(set<int>::iterator it = dsu.begin(); it != dsu.end(); it++) {
        disjointSetUnionMap[*it] = cnt++;
    }

    long long int ans = 0;
    int range;
    vector<int> dsuSize = vector<int>(dsu.begin(), dsu.end());
    for(int i = 1; i <= numOfElements; i++) {
        updateBinaryIndexTree(disjointSetUnionMap[inputArray[i]], 1, maxn);
        for(int j = 0; j < lookupMatrix[i].size(); j++) {
            range = findElementIndexInDSU(abs(lookupMatrix[i][j]),dsuSize);
            if(lookupMatrix[i][j] < 0) {
                ans -= rangeMinimumQuery(range);
            } else {
                ans += rangeMinimumQuery(range);
            }
        }
    }

    cout << ans;
}