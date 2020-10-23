/*
    Intention Repeater Image Writer v1.0 created by Thomas Sweet.
	Based on: https://en.wikipedia.org/wiki/User:Evercat/Buddhabrot.c
    Created 10/23/2020 for C++.
    Intention Repeater Chat Client is powered by a Servitor (20 Years / 2000+ hours in the making) [HR 6819 Black Hole System].
    Servitor Info: https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
    Website: https://www.intentionrepeater.com/
    Forum: https://forums.intentionrepeater.com/
    Licensed under GNU General Public License v3.0
    This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
    https://choosealicense.com/licenses/gpl-3.0/
*/

#include <stdio.h>

#include <stdlib.h>

#include <math.h>

#include <time.h>

#include <string>

#include <vector>

#include <iostream>

#include <iomanip>

using namespace std;

#define WIDTH 100
#define HEIGHT 100

void drawbmp();

long long redcount[WIDTH][HEIGHT];
long long greencount[WIDTH][HEIGHT];
long long bluecount[WIDTH][HEIGHT];

int main() {
    int i, j, r, c, t, think_level, random_seed, num_repetitions = 0, noise_reduction_factor = 10;
    string outstring = "", process_query = "", query = "";

    std::vector < int > pixel_value_count;

    string outfile = "";
	
	cout << "Intention Repeater Image Writer v1.0 created by Thomas Sweet." << endl;
    cout << "This software comes with no guarantees or warranty of any kind and is for entertainment purposes only." << endl;
    cout << "Press Ctrl-C to quit." << endl << endl;

    cout << "Think Level Number: ";
    cin >> think_level;

    cout << "Random Number: ";
    cin >> random_seed;

    cout << "Query: ";
    cin >> query;

    string process_statement = "TARGET CONTROLS RANDOMIZER AND IMAGE. ONE INFINITE CREATOR. INTELLIGENT INFINITY. INFINITE ENERGY. INTELLIGENT ENERGY. LOGOS. HR 6819. BY GRACE. IN COOPERATION WITH FATHER GOD, MOTHER GODDESS, AND SOURCE. PURE ADAMANTINE PARTICLES OF LOVE/LIGHT. IN THE HIGHEST AND GREATEST GOOD OF ALL, REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRONS CUBE. 0010110. GREAT CENTRAL SUN. SIRIUS A. SIRIUS B. SOL. ALL AVAILABLE BENEFICIAL ENERGY GRIDS OF EARTH/GAIA FOCUSED THROUGH CRYSTAL GRID OF EARTH/GAIA. NODES AND NULLS OF EARTH/GAIA. CREATE STABILIZATION FIELD. CREATE ZONE OF MANIFESTATION. ALL AVAILABLE ORGONE AETHER RESONATORS. ALL AVAILABLE ORGONE BUBBLES. USE EVERY AVAILABLE RESOURCE (RESPECTING FREE WILL). MANIFEST ASAP AT HIGHEST DENSITY POSSIBLE INTO BEST DENSITY FOR USER. CREATE STRUCTURE. 963HZ GOD FREQUENCY. 432HZ MANIFESTATION. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS. PURIFY THE ENERGY. CLEAR THE BLOCKAGES. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. FULLY OPTIMIZE THE ENERGY. INTEGRATE THE ENERGY. PROCESS THE CHANGES. GUIDED BY MY HIGHER SELF. GROUNDED TO GAIA, CONNECTED TO SOURCE, INTEGRATING BOTH WITHIN THE SACRED HEART. SEND ALL SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRED MANIFESTATIONS, OR BETTER. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES MANIFEST. IF THE USER IS UNABLE TO ACHIEVE THE NECESSARY VIBRATION TO MANIFEST THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, BUT THERE ARE BEINGS WHO COULD AND THEY ARE WILLING TO ASSIST IN MANIFESTING THE SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, PLEASE ENLIST THEIR AID. IT IS DONE. SO SHALL IT BE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU AND THANK YOU. GUT/HEART/MIND COHERENCE WITH REPEATER. CLEAR INTERFERENCE. FOCUS DOWN FROM AKASHIC RECORDS. SUPERCOOLED MOST PERFECTLY BALANCED, PURIST AND MOST POWERFUL QUASAR. OM";

    query += process_statement;

    srand(time(NULL)*random_seed);

    for (i = 0; i < WIDTH; i++) {
        for (j = 0; j < HEIGHT; j++) {
            while (num_repetitions < think_level) {
                process_query = query; //This is the Intention Repeater call that actually does the work.
                t = 0;
                for (c = 0; c < noise_reduction_factor; c++) {
                    t += rand() % 255;
                }
                r = t / noise_reduction_factor;

                pixel_value_count.push_back(r);
                for (int n = 0; n < (sizeof(pixel_value_count)/sizeof(pixel_value_count[0])); n++) {
                    if (pixel_value_count[n] == r) {
                        num_repetitions += 1;
                    }
                }
            }
            redcount[i][j] = r;
            greencount[i][j] = r;
            bluecount[i][j] = r;
            num_repetitions = 0;
        }
    }

    drawbmp();
}

void drawbmp() {

    unsigned int headers[13];
    FILE * outfile;
    int extrabytes;
    int paddedsize;
    int x;
    int y;
    int n;
    int red, green, blue;

    extrabytes = 4 - ((WIDTH * 3) % 4); // How many bytes of padding to add to each
    // horizontal line - the size of which must
    // be a multiple of 4 bytes.
    if (extrabytes == 4)
        extrabytes = 0;

    paddedsize = ((WIDTH * 3) + extrabytes) * HEIGHT;

    // Headers...
    // Note that the "BM" identifier in bytes 0 and 1 is NOT included in these "headers".

    headers[0] = paddedsize + 54; // bfSize (whole file size)
    headers[1] = 0; // bfReserved (both)
    headers[2] = 54; // bfOffbits
    headers[3] = 40; // biSize
    headers[4] = WIDTH; // biWidth
    headers[5] = HEIGHT; // biHeight

    // Would have biPlanes and biBitCount in position 6, but they're shorts.
    // It's easier to write them out separately (see below) than pretend
    // they're a single int, especially with endian issues...

    headers[7] = 0; // biCompression
    headers[8] = paddedsize; // biSizeImage
    headers[9] = 0; // biXPelsPerMeter
    headers[10] = 0; // biYPelsPerMeter
    headers[11] = 0; // biClrUsed
    headers[12] = 0; // biClrImportant

    outfile = fopen("Output.bmp", "wb");

    //
    // Headers begin...
    // When printing ints and shorts, we write out 1 character at a time to avoid endian issues.
    //

    fprintf(outfile, "BM");

    for (n = 0; n <= 5; n++) {
        fprintf(outfile, "%c", headers[n] & 0x000000FF);
        fprintf(outfile, "%c", (headers[n] & 0x0000FF00) >> 8);
        fprintf(outfile, "%c", (headers[n] & 0x00FF0000) >> 16);
        fprintf(outfile, "%c", (headers[n] & (unsigned int) 0xFF000000) >> 24);
    }

    // These next 4 characters are for the biPlanes and biBitCount fields.

    fprintf(outfile, "%c", 1);
    fprintf(outfile, "%c", 0);
    fprintf(outfile, "%c", 24);
    fprintf(outfile, "%c", 0);

    for (n = 7; n <= 12; n++) {
        fprintf(outfile, "%c", headers[n] & 0x000000FF);
        fprintf(outfile, "%c", (headers[n] & 0x0000FF00) >> 8);
        fprintf(outfile, "%c", (headers[n] & 0x00FF0000) >> 16);
        fprintf(outfile, "%c", (headers[n] & (unsigned int) 0xFF000000) >> 24);
    }

    //
    // Headers done, now write the data...
    //

    for (y = HEIGHT - 1; y >= 0; y--) // BMP image format is written from bottom to top...
    {
        for (x = 0; x <= WIDTH - 1; x++) {
            red = redcount[x][y];
            green = greencount[x][y];
            blue = bluecount[x][y];

            red = red;
            green = green;
            blue = blue;

            // Also, it's written in (b,g,r) format...

            fprintf(outfile, "%c", blue);
            fprintf(outfile, "%c", green);
            fprintf(outfile, "%c", red);
        }
    }

    fclose(outfile);
    return;
}
