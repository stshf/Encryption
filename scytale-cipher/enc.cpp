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
    text.erase(remove(text.begin(), text.end(), ' '), text.end());
    cout << text << "\n";
    string cipher = encode(key, text);
    cout << cipher << "\n";
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
    int reminder = text_length % key;
    int quotient = text_length / key;
    if (reminder != 0) {
        quotient++;
        for (int i=0; i<(key - reminder); i++) {
            text += random_alphabet();
        }
    }
    
    string cipher;
    for (int i=0;i<key; i++) {
        for (int j=0; j<quotient; j++){
            cipher += text[j*key + i];
        }
    }

    return cipher;
}

