//
// Created by camer on 1/28/2021.
//

#include "address_book.h"
#include <iostream>
#include <utility>

using namespace std;

AddressBook::AddressBook(string const &first,string const &last,const string& address){
    setPerson(first,last,address);
}


AddressBook::AddressBook(string const &first, string const &last)
        : AddressBook(first, last, "") {}


AddressBook::AddressBook (): AddressBook("", "", "") {}


void AddressBook::setPerson(const string& first, const string& last, const string& address) {

    vector<Person> mPeople;

    mPeople.emplace_back(Person(first,last,address));

    auto current_person = mPeople.begin();
}


Person *AddressBook::getPerson() {

    return nullptr;
}


Person *AddressBook::findPerson(string last) {
    vector<Person>::iterator iter;
    for (iter = mPeople.begin(); iter < mPeople.end();iter++)
        if((*iter).getLastName()== last){
            cout << "Hello WORLD" << endl;
            return &(*iter);
    }
    return nullptr;
}


Person *AddressBook::findPerson(string first, string last) {
    return nullptr;
}


void AddressBook::print() {
    for (int i =0; i < mPeople.size(); ++i){
    }
}
