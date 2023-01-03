#include <iostream>
#include <vector>
#include<algorithm>
#include <unordered_set>
#include <utility>
#include <stack>
#include<queue>

// алгоритм дейкстры за O(n^2)

using namespace std;

const int maxn = 1e5, inf = 1e9;
vector< vector< pair<int, int> >> g;
int n, m;

vector<int> dijkstra(int s) {

	vector<int> dist(n, inf), a(n, 0);
	dist[s] = 0;

	for (int i = 0; i < n; i++) {

		// находим вершину с минимальным d[v] из ещё не помеченных
		int v = -1;
		for (int u = 0; u < n; u++)
			if (!a[u] && (v == -1 || dist[u] < dist[v]))
				v = u;

		// помечаем её и проводим релаксации вдоль всех исходящих ребер
		
		
		a[v] = true;

		for (auto elem : g[v]) {
			dist[elem.first] = min(dist[elem.first], dist[v] + elem.second);
		}
		
	}
	return dist;
}



int main() {


	cin >> n >> m;
	g.resize(n);

	for (int i = 0; i < m; ++i) {
		int v, u, w; cin >> v >> u >> w;
		g[v - 1].push_back({ u - 1, w });
	}

	vector<int> answer = dijkstra(0);

	for (int i = 0; i < n; ++i) {
		cout << i + 1 << " - " << answer[i] << '\n';
	}


	
}