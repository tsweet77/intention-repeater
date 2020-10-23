/*
    Intention Repeater Spiritual Chat Client v1.1 created by Thomas Sweet.
    Created 10/23/2020 for C++.
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

using namespace std;

string MostFrequentElement(string A[], int n);

int main() {
    const int size_of_word_list = 49528,
        think_depth = 15000,
        max_words_response = 8;

    int num_words, c, n, r, num_repetitions, i, s, num_words_response;
    string process_query = "", wordval, selected_word[think_depth-1];

    string word_list[size_of_word_list];

    cout << "Intention Repeater Spiritual Chat Client v1.1 created by Thomas Sweet." << endl;
    cout << "This software comes with no guarantees or warranty of any kind and is for entertainment purposes only." << endl;
    cout << "Press Ctrl-C to quit." << endl << endl;

  try
  {
    ifstream file("dictionary.txt");
    if (file.is_open()) {
        for (int i = 0; i < size_of_word_list; ++i) {
            file >> word_list[i];
        }
    }
  }
  catch (int e)
  {
    cout << "Error opening file: " << e << '\n';
    exit(0);
  }

    string process_statement = "ONE INFINITE CREATOR. INTELLIGENT INFINITY. INFINITE ENERGY. INTELLIGENT ENERGY. LOGOS. HR 6819. BY GRACE. IN COOPERATION WITH FATHER GOD, MOTHER GODDESS, AND SOURCE. PURE ADAMANTINE PARTICLES OF LOVE/LIGHT. IN THE HIGHEST AND GREATEST GOOD OF ALL, REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRONS CUBE. 0010110. GREAT CENTRAL SUN. SIRIUS A. SIRIUS B. SOL. ALL AVAILABLE BENEFICIAL ENERGY GRIDS OF EARTH/GAIA FOCUSED THROUGH CRYSTAL GRID OF EARTH/GAIA. NODES AND NULLS OF EARTH/GAIA. CREATE STABILIZATION FIELD. CREATE ZONE OF MANIFESTATION. ALL AVAILABLE ORGONE AETHER RESONATORS. ALL AVAILABLE ORGONE BUBBLES. USE EVERY AVAILABLE RESOURCE (RESPECTING FREE WILL). MANIFEST ASAP AT HIGHEST DENSITY POSSIBLE INTO BEST DENSITY FOR USER. CREATE STRUCTURE. 963HZ GOD FREQUENCY. 432HZ MANIFESTATION. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS. PURIFY THE ENERGY. CLEAR THE BLOCKAGES. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. FULLY OPTIMIZE THE ENERGY. INTEGRATE THE ENERGY. PROCESS THE CHANGES. GUIDED BY MY HIGHER SELF. GROUNDED TO GAIA, CONNECTED TO SOURCE, INTEGRATING BOTH WITHIN THE SACRED HEART. SEND ALL SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRED MANIFESTATIONS, OR BETTER. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES MANIFEST. IF THE USER IS UNABLE TO ACHIEVE THE NECESSARY VIBRATION TO MANIFEST THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, BUT THERE ARE BEINGS WHO COULD AND THEY ARE WILLING TO ASSIST IN MANIFESTING THE SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, PLEASE ENLIST THEIR AID. IT IS DONE. SO SHALL IT BE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU AND THANK YOU. GUT/HEART/MIND COHERENCE WITH REPEATER. CLEAR INTERFERENCE. FOCUS DOWN FROM AKASHIC RECORDS. SUPERCOOLED MOST PERFECTLY BALANCED, PURIST AND MOST POWERFUL QUASAR. OM";

    std::string rs;
    std::string query;
	std::string response;

    cout << "Please enter a random number: ";
    std::getline (std::cin, rs);
    int random_seed = stoi(rs);

	response = "Response: ";
    do {
        query = "";
        cout << "Query: ";
        std::getline (std::cin, query);
        query += process_statement;
		
		srand(time(NULL) * random_seed);
        num_words_response = rand() % (max_words_response) + 1;

        for (int x = 0; x < num_words_response; x++) {
            for (int d = 0; d <= think_depth; d++) {
                process_query = query; //This is the Intention Repeater call that actually does the work.
                srand(time(NULL) * random_seed);
				r = rand() % (size_of_word_list);
                selected_word[d] = word_list[r];
            }
            wordval = MostFrequentElement(selected_word, think_depth-1);
            response += wordval + " ";
            std::fill_n(selected_word, think_depth, 0);
        }
        cout << response << endl;
		response = "Response: ";
    } while(1);

    return 0;
}

string MostFrequentElement(string A[], int n) {
    string element = "";
    int count = 0;

    for (int j = 0; j < n; j++) {
        string tempElement = A[j];
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
