/*
Name: Cameron Murillo
Date: 12/12/2020
Github: https://github.com/MSJC-CSIS-DCHernandez/assignment-07-cameronmurillo
*/
#include <iostream>
#include "string"
#include "person.h"
#include "main_functions.h"
#include "address_book.h"

using std::cin;
using std::endl;
using std::cout;
using std::getline;

using std::cin;
using std::cout;
using std::endl;

void print_menu() {
    cout << "-----------------------------------------" << endl;
    cout << "Please make a selection: " << endl;
    cout << "A. Add Person" << endl;
    cout << "B. Find Person" << endl;
    cout << "C. Print List" << endl;
    cout << "Q. Quit " << endl;
    cout << "-----------------------------------------" << endl;
    cout << "Make Selection: ";
}

void menu_decision() {
    size_t const kNumberOfPeople = 5;
    Person listOfPeople[kNumberOfPeople];
    AddressBook k ;
    char user_choice;
    while (toupper(user_choice) != 'Q') {
        print_menu();
        cin >> user_choice;
        cin.ignore(256, '\n');
        switch (toupper(user_choice)) {
            case 'A': {

                getPeople(listOfPeople, kNumberOfPeople);
                continue;
            }
            case 'B': {
                k.findPerson("haha");
                continue;
            }
            case 'C': {
                printPeople(listOfPeople, kNumberOfPeople);
                continue;
            }
            case 'Q': {
                cout << "Thank you for using" << endl;
                break;
            }
            default: {
                cout << "Please enter A, B,C or Q" << endl;
                continue;
            }
        }
    }
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
    AddressBook k;

    for (int i{0}; i < length; ++i) {
        Person &person = people[i];
        string first;
        string last;
        string address;

        cout << "Enter First Name: " ;
        getline(cin, first);
        person.setFirstName(move(user_input));

        cout << "Enter Last Name: " ;
        getline(cin, last);
        person.setLastName(move(user_input));

        cout << "Enter Address: " ;
        getline(cin, address);
        person.setAddress(move(user_input));
        k.setPerson(first,last,address);
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