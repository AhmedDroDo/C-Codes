// FCI – Programming 1 – 2018 - Assignment 2
// Program Name: ROT13.cpp
// Last Modification Date: 2/3/2018
// Author and ID and Group: Ahmed Taha Basyoni 20170023 G1
// Teaching Assistant:
// Purpose:Write a program to cipher a message

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int mode;
    string alphL ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ");
    string cipherL ("nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM ");


    while (true){
        string message;
        string cipher;
        cout << "Welcome To ROT13" << endl;
        cout << "What do you like to do today?" << endl;
        cout << "1-Cipher a message" << endl;
        cout << "2-Decipher a message" << endl;
        cout << "3-End" << endl;
        cout << "\nEnter a Number: ";
        cin >> mode;
        if (mode!=1 && mode!=2 && mode!=3){
            cout << "Oops! You must choose 1,2 or 3" << endl;
            cout << "========================================" << endl;
            continue;
        }

        else if (mode==1){
            cout << "Enter a Message: ";
            cin.get();
            getline(cin, message);

            for (int i=0; i<message.length(); i++){
                for (int j=0; j<alphL.length(); j++){
                    if (message[i]==alphL[j]){
                        cipher+=cipherL[j];
                    }
                }
            }
            cout << "The Cipher Message: " << cipher << endl;
            cout << "========================================" << endl;
        }

        else if (mode==2){
            cout << "Enter a Cipher: ";
            cin.get();
            getline(cin, message);

            for (int i=0; i<message.length(); i++){
                for (int j=0; j<alphL.length(); j++){
                    if (message[i]==alphL[j]){
                        cipher+=cipherL[j];
                    }
                }
            }
            cout << "The Decipher Message: " << cipher << endl;
            cout << "========================================" << endl;
        }

        else if (mode==3){
            cout << "Bye Bye We want to see you again :)" << endl;
            cout << "========================================" << endl;
            return 0;
        }
    }


}
