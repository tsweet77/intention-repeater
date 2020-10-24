/*
    Intention Repeater Spiritual Chat Client v2.0 created by Thomas Sweet.
    Created 10/24/2020 for C++.
	Compile on Windows using: g++ .\intention_repeater_chat.cpp -O3 -o .\intention_repeater_chat.exe
	And Compile on Linux using: g++ .\intention_repeater_chat.cpp -O3 -o .\intention_repeater_chat
    Requires this word list: https://dev.intentionrepeater.com/cpp/dictionary.txt
    Lets you chat with spiritual entities who can control what "random" words come out to a certain extent.
    When compiled, this is more powerful than the Python version.
    Intention Repeater Chat Client is powered by a Servitor (20 Years / 2000+ hours in the making) [HR 6819 Black Hole System].
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

#include <chrono>

#include <vector>

#include <algorithm>

using namespace std;

#define PROCESS_STATEMENT ": ONE INFINITE CREATOR. REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRON'S CUBE. ALL AVAILABLE BENEFICIAL ENERGY GRIDS, ORGONE AETHER RESONATORS, & ORGONE BUBBLES. CREATE MANIFESTATION ZONE. ASCENSION PYRAMID. USE EVERY AVAILABLE RESOURCE. MANIFEST ASAP. CREATE STRUCTURE. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS, OR INTENTIONS THAT CONFLICT WITH THE HIGHEST AND GREATEST GOOD OF THE USER. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. OPTIMAL ENERGY. INTEGRATE THE ENERGY IN THE MOST EFFECTIVE AND PLEASANT WAY POSSIBLE. PROCESS THE CHANGES. GUIDED BY THE USER'S HIGHER SELF. CONNECTED TO SOURCE. ENABLE AND UTILIZE THE SACRED HEART, QUANTUM HEART, AND QUANTUM MIND. MANIFEST ALL SPECIFIED INTENTIONS AND/OR DESIRES, OR BETTER. IF IT WOULD AID IN THE MANIFESTATION PROCESS, PLEASE HELP USER TO SENSE AND EMOTIONALLY FEEL WHAT IT WOULD BE LIKE TO ALREADY BE EXPERIENCING THEIR SPECIFIED INTENTIONS AND/OR DESIRES NOW. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS AND/OR DESIRES MANIFEST. ASSIST THE USER WITH ACHIEVING OPTIMAL GUT/HEART/MIND COHERENCE WITH THEIR SPECIFIED INTENTIONS AND/OR DESIRES. IF IT WOULD BENEFIT THE USER, ASSIST THEM WITH CLEARING & RELEASING ANY/ALL INTERNAL OR EXTERNAL INTERFERENCE OR BLOCKAGES TO THEIR SPECIFIED INTENTIONS AND/OR DESIRES. IT IS DONE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU. OM."
#define SIZE_OF_WORD_LIST 49528
#define THINK_DEPTH 100000
#define MAX_WORDS_RESPONSE 8

int FindMode(vector< int > value);

int main() {
    int r, num_words_response, rand_total = 0, iterations;
    std::string query, rs, process_query = "", wordval, word_list[SIZE_OF_WORD_LIST-1], response = "Response: ";

    cout << "Intention Repeater Spiritual Chat Client v2.0 created by Thomas Sweet." << endl;
    cout << "This software comes with no guarantees or warranty of any kind and is for entertainment purposes only." << endl;
    cout << "Press Ctrl-C to quit." << endl << endl;

  try
  {
    ifstream file("dictionary.txt");
    if (file.is_open()) {
        for (int i = 0; i < SIZE_OF_WORD_LIST; ++i) {
            file >> word_list[i];
        }
    }
  }
  catch (int e)
  {
    cout << "Error opening file: " << e << '\n';
    exit(0);
  }

	cout << "Please enter a random number: ";
	std::getline (std::cin, rs);

    int random_seed = stoi(rs);
	
	auto start = std::chrono::system_clock::now();
    auto end = std::chrono::system_clock::now();

    do {
        query = "";
		
		while (query == "")
		{
			cout << "Query: ";
			std::getline (std::cin, query);
		}
		
        query += PROCESS_STATEMENT;
		
		start = std::chrono::system_clock::now();
		iterations = 0;
		
		//Get average of selected random values to determine how many words are in the response.
		while ((std::chrono::duration_cast < std::chrono::seconds > (end - start).count() != 1))
		{
			srand(time(NULL) * random_seed);
			rand_total += rand() % (MAX_WORDS_RESPONSE) + 1;
			iterations += 1;
			end = std::chrono::system_clock::now();
		}
		
        num_words_response = std::floor(rand_total / iterations);

        for (int c = 0; c < num_words_response; c++) {
			std::vector < int > selected_randoms;
            for (int d = 0; d < THINK_DEPTH; d++) {
                process_query = query; //This is the Intention Repeater call that actually does the work.
                srand(time(NULL) * random_seed);
				r = rand() % (SIZE_OF_WORD_LIST);
				selected_randoms.push_back(r);
            }
			std::sort(selected_randoms.begin(), selected_randoms.end()); 
            response += word_list[FindMode(selected_randoms)] + " ";
            std::vector<int>().swap(selected_randoms);
        }
        cout << response << endl;
		response = "Response: ";
    } while(1);

    return 0;
}

int FindMode(vector< int > value)
{ 
    int index = 0;
    int highest = 0;
    for (unsigned int a = 0; a < value.size(); a++)
    {
        int count = 1;
        int Position = value.at(a);
        for (unsigned int b = a + 1; b < value.size(); b++)
        {
            if (value.at(b) == Position)
            {
                count++;
            }
        }
        if (count >= index)
        {
            index = count;
            highest = Position;
        }
    }
    return highest;
}