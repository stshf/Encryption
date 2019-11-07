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
    cout << "Input cipher text: ";
    getline(cin, text);
    text.erase(remove(text.begin(), text.end(), ' '), text.end());
    cout << text << "\n";
    string plain_text = encode(key, text);
    cout << plain_text << "\n";
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
    int text_length = text.size();
    int quotient = text_length / key;
    string plain_text;
    for (int i=0;i<quotient; i++) {
        for (int j=0; j<key; j++){
            plain_text += text[j*quotient + i];
        }
    }
    return plain_text;
}

