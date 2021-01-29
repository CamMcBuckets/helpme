// ################################################################
// File : main.cpp
// Author: Cameron Murillo
// Date : January 19, 2021
// Description: Create an array of length 5 of object type Person.
// ################################################################

#include <iostream>
#include "string"
#include "person.h"

using std::cin;
using std::endl;
using std::cout;
using std::getline;

void getPeople(Person *people, size_t length);
void printPeople(Person *people, size_t length);


int main() {

    size_t const kNumberOfPeople = 5;
    Person listOfPeople[kNumberOfPeople];

    getPeople(listOfPeople, kNumberOfPeople);
    printPeople(listOfPeople, kNumberOfPeople);

    return 0;
}


// ################################################################
//@par Name
//  getPeople
//@purpose
//  initializes an array of type Person.
//@ param[in]:
// people - the array used for holding the people information.
//@ param[in]:
// length - the length of the array being utilized.
//@return
//none
//@par references
//none
//@par Notes
//none
// ################################################################


void getPeople(Person *people, size_t length) {

    string user_input;

    for (int i{0}; i < length; ++i) {
        Person &person = people[i];

        cout << "Enter First Name: " ;
        getline(cin, user_input);
        person.setFirstName(move(user_input));

        cout << "Enter Last Name: " ;
        getline(cin, user_input);
        person.setLastName(move(user_input));

        cout << "Enter Address: " ;
        getline(cin, user_input);
        person.setAddress(move(user_input));
    }
}


// ################################################################
//@par Name
//  printPeople
//@purpose
//  Prints the list of people.
//@ param[in]:
// people - the array used for holding the people information.
//@ param[in]:
// length - the length of the array being utilized.
//@return
//none
//@par references
//none
//@par Notes
//none
// ################################################################

void printPeople(Person *people, size_t length) {
    for (int i{0}; i < length; ++i) {
        Person &person = people[i];

        cout << "Person " << i + 1 << ": " << endl;

        cout << "Name: ";
        cout << person.getFirstName() << " ";
        cout << person.getLastName() << " " << endl;

        cout << "Address: ";
        cout << person.getAddress() << endl;
        cout << endl;
    }
}
