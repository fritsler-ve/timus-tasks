#include <iostream>
#include <vector>

using namespace std;

const int max_size = 40001;
int timer = 0;
vector<pair<int, int>> time(max_size);
vector<vector<int>> tree (max_size, vector<int>());

int is_ancestor(pair<int, int> first, pair<int, int> second) {
    if (first.first < second.first && second.second < first.second) {
        return 1;
    }
    if (second.first < first.first && first.second < second.second) {
        return 2;
    }
    return 0;
}

void dfs(int current_id) {
    ++timer;
    time[current_id].first = timer;
    for (int i : tree[current_id]) {
        if (tree[i].size() == 0) {
            time[i].first = timer + 1;
            time[i].second = timer + 2;
            timer += 3;
        } else {
            dfs(i);
        }
    }
    ++timer;
    time[current_id].second = timer;
}

int main() {
    int n;
    cin >> n;

    int grandpa;
    int curr_id, parent_id;
    for (int i = 0; i < n; ++i) {
        cin >> curr_id >> parent_id;
        if (parent_id == -1) {
            grandpa = curr_id;
            continue;
        }
        tree[parent_id].push_back(curr_id);
    }

    dfs(grandpa);

    cin >> n;
    vector<int> result;

    int a, b;
    for (int i = 0; i < n; ++i) {
        cin >> a >> b;
        result.push_back(is_ancestor(time[a], time[b]));
    }
    for (auto i : result) {
        cout << i << endl;
    }
    return 0;
}
