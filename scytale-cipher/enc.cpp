#include <iostream>
#include <string>
#include <random>

using namespace std;


char random_alphabet();  // return one random alphabet
string encode(int key, string text);


int main() {
    cout << "=== scytale-cipher ===" << endl;

    int key;
    cout << "Input key: ";
    cin >> key;

    string text;
    cout << "Input plain text: ";
    cin >> text;

    return 0;
}


char random_alphabet() {
    random_device rnd;
    mt19937 mt(rnd());
    uniform_int_distribution<> rand(0, 25);

    int shift = rand(mt);
    return 'a' + shift;
}


string encode(int key, string text) {
    int n = (key + text.size() - 1) / key;

    return sample;
}
