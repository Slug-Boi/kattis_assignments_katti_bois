
#include <iostream>
#include <cstring>  
#include <algorithm>

int main() {

    std::string inp;
    std::getline(std::cin, inp);

    inp.erase(remove_if(inp.begin(),inp.end(), isspace),inp.end());

    std::cout << inp;

    return 0;
}
