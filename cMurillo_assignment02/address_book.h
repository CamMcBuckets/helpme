//
// Created by camer on 1/28/2021.
//

#ifndef MAIN_CPP_ADDRESS_BOOK_H
#define MAIN_CPP_ADDRESS_BOOK_H

#include "person.h"
#include "string"
#include <vector>

using namespace std;

class AddressBook {
private:
    vector <Person> mPeople;
    vector<Person>::iterator mpCurrentPerson = mPeople.begin();
public:
    // Constructors
    AddressBook(string const &first, string const &last, const string& address);
    AddressBook(string const &first, string const &last);
    AddressBook();

    // Mutators
    void setPerson(const string& first, const string& last, const string& address);

    // accessors
    Person *getPerson();
    Person *findPerson(string last);
    Person *findPerson(string first, string last);
    void print();

};


#endif //MAIN_CPP_ADDRESS_BOOK_H
