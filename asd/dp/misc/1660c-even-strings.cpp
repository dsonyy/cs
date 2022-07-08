#include <bits/stdc++.h>
using namespace std;

bool is_even(string str) {
  if (str.size() % 2 == 1)
    return false;
  for (int i = 1; i < str.size(); i += 2) {
    if (str[i] != str[i - 1])
      return false;
  }
  return true;
}

int find_next(const string& str, int i) {
  for (int j = i + 1; j < str.size(); j++) {
    if (str[i] == str[j])
      return j;
  }
  return -1;
}

int solution(vector<int>& dp, const string& str, int i) {
  if (i >= str.size())
    return 0;
  if (dp[i] != -1)
    return dp[i];

  int j = find_next(str, i);
  if (j == -1)
    dp[i] = solution(dp, str, i + 1) + 1;
  else if (j == i + 1)
    dp[i] = solution(dp, str, i + 2);
  else
    dp[i] = min(solution(dp, str, j + 1) + (j - i - 1),
                solution(dp, str, i + 1) + 1);
  return dp[i];
}

int main(int argc, char** argv) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.precision(10);

  int n;
  string str;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> str;
    vector<int> dp(str.size(), -1);
    cout << solution(dp, str, 0) << "\n";
  }

  return 0;
}