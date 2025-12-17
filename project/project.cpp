#include<iostream>
using namespace std;
void swap(int& a, int& b) {
	int c;
	if (a < b) {
		c = a;
		a = b;
		b = c;
	}
}


int main() {
	int a = 4, b = 10;
	int c = 3200, d = 32323;
	swap(c, d);
	swap(a, b);
	cout << "a =" << a << ", b =" << b << endl;
	cout << "c =" << c << ", d =" << d << endl;
}