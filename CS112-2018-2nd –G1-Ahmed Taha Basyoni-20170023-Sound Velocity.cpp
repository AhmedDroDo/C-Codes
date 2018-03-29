// FCI – Programming 1 – 2018 - Assignment 2
// Program Name: Sound Velocity.cpp
// Last Modification Date: 2/3/2018
// Author and ID and Group: Ahmed Taha Basyoni 20170023 G1
// Teaching Assistant:
// Purpose:Write a program calculate sound velocity

#include <iostream>
#define sVelocity 331.3

using namespace std;

int main()
{
    int startDegree,endDegree;
    float velocity;

    cout << "Enter The Start of Temperture: ";
    cin >> startDegree;
    cout << "Enter The End of Temperture: ";
    cin >> endDegree;
    cout << "\n";

    for (int i=startDegree; i<(endDegree+1); i++){
        velocity = sVelocity + 0.61 * i;
        cout << "At " << i << " degrees Celsius the velocity of sound is " << velocity << " m/s" << endl;
    }

    return 0;
}
