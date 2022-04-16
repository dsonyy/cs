#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

int N, J;                // N - number of stairs, J - max number of jumps
vector<vector<int>> dp;  // vector for dynamic programmig
const int UNKNOWN = -1;  // to mark yet uncomputed values

/**
 * @brief Fill the dp vector with the edge cases.
 */
void init() {
  dp.resize(N, vector<int>(J + 1, UNKNOWN));

  for (int n = 0; n < N; n++)
    dp[n][0] = 0;

  for (int j = 1; j < J + 1; j++)
    dp[N - 1][j] = 1;

  dp[N - 2][1] = 1;
  for (int j = 2; j < J + 1; j++)
    dp[N - 2][j] = 2;

  for (int n = 0; n < N - 2; n++)
    dp[n][1] = 0;
}

/**
 * @brief Compute the number of ways to reach the N-th floor.
 * @param floor - current floor
 * @param jumps - max number of jumps
 * @return number of ways
 */
int stairs(int floor, int jumps) {
  if (dp[floor][jumps] == UNKNOWN)
    dp[floor][jumps] =
        stairs(floor + 1, jumps - 1) + stairs(floor + 2, jumps - 1);
  return dp[floor][jumps];
}

int main(int argc, char** argv) {
  cin >> N >> J;
  init();
  cout << stairs(0, J) << endl;
  for (auto& p : dp) {
    for (int q : p) {
      if (q == UNKNOWN)
        cout << "---\t";
      else
        cout << setw(3) << setfill('0') << q << "\t";
    }
    cout << endl;
  }
  return 0;
}