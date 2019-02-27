#include <iostream>
#include <string>

using namespace std;


string decode(string text, int key) {
    // --- parameters ---
    // text: encrypted text
    // key : times of shift

    for (int i = 0; i < text.size(); i++) {
        if (text[i] >= 'a' and text[i] <= 'z'){
            text[i] = char((text[i] - 'a' +(26- key)) % 26 + 'a');
        }
        else if (text[i] >= 'A' and text[i] <= 'Z'){
            text[i] = char((text[i] - 'A' +(26- key)) % 26 + 'A');
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

    string text;
    cout << "Encrypted text: ";
    cin >> text;

    cout << decode(text, key) << endl;

    return 0;
}
