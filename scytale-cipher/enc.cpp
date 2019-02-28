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
    cin.ignore();

    string text;
    cout << "Input plain text: ";
    getline(cin, text);

    // remove white space
    text.erase(remove(text.begin(), text.end(), ' '), text.end());

    cout << endl;
    cout << "Plain text  :" << text << endl;
    cout << "Encoded text: " << encode(key, text) << endl;

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
    int r = text.size() % key;  // remainder
    int q = text.size() / key;  // quotient
    if (r) {
        q++;
        for (int i = 0; i < key - r; i++) {
            text += random_alphabet();
        }
    }

    string cipher;
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < q; j++){
            int idx = j * key + i;
            cipher += text[idx];
        }
    }

    return cipher;
}

