#include <iostream>
#include <string>

using namespace std;


string encode(string text, int key) {
    // --- parameters ---
    // text: Plain text
    // key : times of shift

    for (int i = 0; i < text.size(); i++) {
        for (int j = 0; j < key; j++) {
            if (text[i] == 'z') {
                text[i] = 'a';
            }
            else if (text[i] == 'Z') {
                text[i] = 'A';
            }
            else {
                text[i]++;
            }
        }
    }

    return text;
}



int main() {
    cout << "--- caeser cipher ---" << endl;

    int key;
    cout << "Choose the key (1 ~ 25): ";
    cin >> key;

    while (key < 1 or 25 < key) {
        cout << "You have entered an invalid key number." << endl;
        cout << "Try again?" << endl;
        cout << "yes[y]/no[n]: ";
        string flag;
        cin >> flag;

        if (flag == "n" or flag == "no" or flag == "NO" or flag == "No") {
            return 0;
        }
    }

    string text;
    cout << "Plain text: ";
    cin >> text;

    cout << encode(text, key) << endl;

    return 0;
}
