#include <iostream>
#include <string>
using namespace std;


string encode(string text, int key) {
    // --- parameters ---
    // text: Plain text
    // key : times of shift

    for (int i = 0; i < text.size(); i++) {
            if (text[i] <= 'z' && text[i] >= 'a') {
                text[i] = char((text[i] - 'a' + key) % 26 + 'a');
            }
            else if (text[i] <= 'Z' && text[i] >= 'A') {
                text[i] = char((text[i] - 'A' + key) % 26 + 'A');
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

    string text;
    cout << "Plain text: ";
    cin >> text;

    cout << encode(text, key) << endl;

    return 0;
}
