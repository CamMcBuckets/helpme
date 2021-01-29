// ################################################################
// File : person.cpp
// Author: Cameron Murillo
// Date : January 19, 2021
// Description: The Code behind the definitions
// ################################################################

#include "person.h"
#include <string>


Person::Person(string const &first, string const &last, string const &address) {
    setFirstName(first);
    setLastName(last);
    setAddress(address);
}


Person::Person(string const &first, string const &last)
        : Person(first, last, "") {}


Person::Person() : Person("", "", "") {}


void Person::setFirstName(string const &first) {
    mFirstName = first;
}


void Person::setLastName(string const &last) {
    mLastName = last;
}


void Person::setAddress(string const &address) {
    mAddress = address;
}


string Person::getFirstName() {
    return std::string(mFirstName);
}


string Person::getLastName() {
    return std::string(mLastName);
}


string Person::getAddress() {
    return std::string(mAddress);
}
