#include <iostream>
#include <string>
using namespace std;

const int mod = 26;  // number of alphabet


string encode(string text, int key) {
    // --- parameters ---
    // text: Plain text
    // key : times of shift

    for (int i = 0; i < text.size(); i++) {
        int diff;
        int shift;
        if ('a' <= text[i] and text[i] <= 'z') {
            diff = text[i] - 'a';
            shift = (diff + key) % mod;
            text[i] = 'a' + shift;
        }
        else if ('A' <= text[i] and text[i] <= 'Z') {
            shift = (diff + key) % mod;
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
    cin  >> key;
    cin.ignore();
    string text;
    cout << "Plain text: ";
    getline(cin, text);

    cout << encode(text, key) << endl;

    return 0;
}
