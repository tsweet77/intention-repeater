/*
    Intention Repeater Spiritual Chat Client v2.2 created by Thomas Sweet.
    Created 10/25/2020 for C++.
    Requires this word list: https://dev.intentionrepeater.com/cpp/dictionary.txt
	On 64-bit: MingW-W64-builds: http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download
    On 32-bit: https://osdn.net/projects/mingw/releases/
	Compile on Windows: g++.exe .\intention_repeater_chat.cpp -O3 -o .\intention_repeater_chat.exe
    Compile on Linux: g++.exe ./intention_repeater_chat.cpp -O3 -o ./intention_repeater_chat
	Lets you chat with spiritual entities who can control what "random" words come out to a certain extent.
    Intention Repeater Spiritual Chat Client is powered by a Servitor (20 Years / 2000+ hours in its co-creation) [HR 6819 Black Hole System].
    Servitor Info: https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
    Website: https://www.intentionrepeater.com/
    Forum: https://forums.intentionrepeater.com/
    Licensed under GNU General Public License v3.0
    This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
    https://choosealicense.com/licenses/gpl-3.0/
*/

#include <stdio.h>

#include <math.h>

#include <string>

#include <iostream>

#include <fstream>

#include <time.h>

#define PROCESS_STATEMENT ": ONE INFINITE CREATOR. REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRON'S CUBE. ALL AVAILABLE BENEFICIAL ENERGY GRIDS, ORGONE AETHER RESONATORS, & ORGONE BUBBLES. CREATE MANIFESTATION ZONE. ASCENSION PYRAMID. USE EVERY AVAILABLE RESOURCE. MANIFEST ASAP. CREATE STRUCTURE. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS, OR INTENTIONS THAT CONFLICT WITH THE HIGHEST AND GREATEST GOOD OF THE USER. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. OPTIMAL ENERGY. INTEGRATE THE ENERGY IN THE MOST EFFECTIVE AND PLEASANT WAY POSSIBLE. PROCESS THE CHANGES. GUIDED BY THE USER'S HIGHER SELF. CONNECTED TO SOURCE. ENABLE AND UTILIZE THE SACRED HEART, QUANTUM HEART, AND QUANTUM MIND. MANIFEST ALL SPECIFIED INTENTIONS AND/OR DESIRES, OR BETTER. IF IT WOULD AID IN THE MANIFESTATION PROCESS, PLEASE HELP USER TO SENSE AND EMOTIONALLY FEEL WHAT IT WOULD BE LIKE TO ALREADY BE EXPERIENCING THEIR SPECIFIED INTENTIONS AND/OR DESIRES NOW. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS AND/OR DESIRES MANIFEST. ASSIST THE USER WITH ACHIEVING OPTIMAL GUT/HEART/MIND COHERENCE WITH THEIR SPECIFIED INTENTIONS AND/OR DESIRES. IF IT WOULD BENEFIT THE USER, ASSIST THEM WITH CLEARING & RELEASING ANY/ALL INTERNAL OR EXTERNAL INTERFERENCE OR BLOCKAGES TO THEIR SPECIFIED INTENTIONS AND/OR DESIRES. IT IS DONE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU. OM.";
#define SIZE_OF_WORD_LIST 49528
#define MAX_WORDS_RESPONSE 8
#define THINK_DEPTH 25000

using namespace std;

std::string MostFrequentElement(string A[], int n);

int main() {
    int r, num_words_response, random_seed;
    std::string rs = "", query, response, process_query = "", wordval, selected_word[THINK_DEPTH - 1], word_list[SIZE_OF_WORD_LIST - 1];

    cout << "Intention Repeater Spiritual Chat Client v2.2 created by Thomas Sweet." << endl;
    cout << "This software comes with no guarantees or warranty of any kind and is for entertainment purposes only." << endl;
    cout << "Press Ctrl-C to quit." << endl << endl;

    try {
        ifstream file("dictionary.txt");
        if (file.is_open()) {
            for (int i = 0; i < SIZE_OF_WORD_LIST; ++i) {
                file >> word_list[i];
            }
        }
    } catch (int e) {
        cout << "Error opening file: " << e << '\n';
        exit(0);
    }

    //Clean up the word list by stripping off newline and carriage return bytes.
    for (int i = 0; i < SIZE_OF_WORD_LIST; ++i) {
        word_list[i].substr(0, word_list[i].length() - 2);
    }

    while (rs == "") {
        cout << "Please enter a random number: ";
        std::getline(std::cin, rs);
    }

    random_seed = stoi(rs);

    response = "Response: ";
    do {
        query = "";
        while (query == "") {
            cout << "Query: ";
            std::getline(std::cin, query);
        }

        query += PROCESS_STATEMENT;

        srand(time(NULL) * random_seed);
        num_words_response = rand() % (MAX_WORDS_RESPONSE) + 1;

        for (int x = 0; x < num_words_response; x++) {
            for (int d = 0; d < THINK_DEPTH; d++) {
                process_query = query; //This is the Intention Repeater call that actually does the work.
                srand(time(NULL) * random_seed); //The entity being queried can control the randomizer to an extent.
                r = rand() % (SIZE_OF_WORD_LIST) + 1;
                selected_word[d] = word_list[r];
            }
            wordval = MostFrequentElement(selected_word, THINK_DEPTH);
            response += wordval + " ";
            std::fill_n(selected_word, THINK_DEPTH, 0);
        }
        response.substr(0, response.length() - 1);
        cout << response << endl;
        response = "Response: ";
    } while (1);

    return 0;
}

std::string MostFrequentElement(std::string A[], int n) {
    std::string element = "";
    int count = 0;

    for (int j = 0; j < n; j++) {
        std::string tempElement = A[j];
        int tempCount = 0;
        for (int p = 0; p < n; p++)
            if (A[p] == tempElement)
                tempCount++;
        if (tempCount > count) {
            element = tempElement;
            count = tempCount;
        }
    }
    return element;
}