#include <iostream>
#include <string>

using namespace std;

const int mod = 26;  // number of alphabet

string decode(string text, int key) {
    /*
    === parameters ===
    text(stirng): encrypted text
    key(int)    : key to shift (1 ~ 25)

    === return ===
    text(string): plain text
    */

    for (int i = 0; i < text.size(); i++) {
        int diff;
        int shift;
        if ('a' <= text[i] and text[i] <= 'z') {
            diff = text[i] - 'a';
            shift = (diff + (mod - key)) % mod;
            text[i] = 'a' + shift;
        }
        else if ('A' <= text[i] and text[i] <= 'Z') {
            diff = text[i] - 'A';
            shift = (diff + (mod - key)) % mod;
            text[i] = 'A' + shift;
        }
        else {
            text[i];
        }
    }

    return text;
}


int main() {
    cout << "--- caeser cipher ---" << endl;

    int key;
    cout << "Choose the key (1 ~ 25): ";
    cin >> key;
    cin.ignore();
    string text;
    cout << "Encrypted text: ";
    getline(cin, text);

    cout << decode(text, key) << endl;

    return 0;
}
