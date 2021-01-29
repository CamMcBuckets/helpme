// ################################################################
// File : person.h
// Author: Cameron Murillo
// Date : January 19, 2021
// Description: Definitions of the class and its functions
// ################################################################

#ifndef CMURILLO_ASSIGNMENT01_PERSON_H
#define CMURILLO_ASSIGNMENT01_PERSON_H

#include "string"

using std::string;

class Person {
private:
    string mFirstName;
    string mLastName;
    string mAddress;
public:

    //Constructors
    Person();
    Person(string const &first, string const &last);
    Person(string const &first, string const &last, string const &address);

    // Mutators
    void setFirstName(string const &first);
    void setLastName(string const &last);
    void setAddress(string const &address);

    //Accessors
    string getFirstName();
    string getLastName();
    string getAddress();
};


#endif //CMURILLO_ASSIGNMENT01_PERSON_H
