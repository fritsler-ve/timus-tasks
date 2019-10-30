#include <iostream>
#include <cmath>

using namespace std;

unsigned long long solve(int radius) {
    unsigned long long result = 0;
    for (int i = 0; i < radius; ++i) {
        result += ceil(sqrt(radius * radius - i * i));
    }
    return result * 4;
}

int main() {
    int radius;
    cin >> radius;
    cout << solve(radius);
    system("pause");
    return 0;
}