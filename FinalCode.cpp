#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <chrono>
#include <fstream>
#include <string>
#include <ctime>

using namespace std;
using namespace cv; 
using namespace std::chrono; //stopwatch

//Get system date and time
string datetime()
{
	time_t rawtime;
	struct tm* timeinfo;
	char buffer[80];

	time(&rawtime);
	timeinfo = localtime(&rawtime);

	strftime(buffer, 80, "%m-%d-%Y %H-%M-%S", timeinfo);
	return string(buffer);
}

bool filecopy(string fnamein, string fnameout)
{
	ifstream fin(fnamein, ios::binary);
	if (!fin)
	{
		cout << "could not open input:" << fnamein << '\n';
		return false; 
	}

	ofstream fout(fnameout, ios::binary);
	if (!fout)
	{
		cout << "could not open output" << fnameout << '\n';
		return false;
	}
	fout << fin.rdbuf();
	return bool(fout);
}

int main()
{
	auto start = high_resolution_clock::now(); //Start stopwatch 

	Mat img = imread("C:/Users/me/Desktop/leaf.jpg"); //Read Image

	// Convert BGR to HSV
	Mat hsv; 
	cvtColor(img, hsv, COLOR_BGR2HSV);

	//Mask 1 limits
	Scalar lower_brown1 = Scalar(10, 50, 50);
	Scalar upper_brown1 = Scalar(15, 255, 255);
	//Mask 2 limits
	Scalar lower_brown2 = Scalar(15, 50, 50);
	Scalar upper_brown2 = Scalar(20, 255, 255);

	Mat mask1, mask2;
	inRange(hsv, lower_brown1, upper_brown1, mask1); // Mask for 1st limit
	inRange(hsv, lower_brown2, upper_brown2, mask2); // Mask for 2nd limit

	// Create the mask that combines the two mask 
	Mat mask;
	bitwise_or(mask1, mask2, mask);

	// Create a final result that just show the brown in the mask.  
	Mat res;
	bitwise_and(img, img, res, mask);

	const char* titles[] = { "Brown mask 1", "Brown mask 2", "Final mask", "Result" };
	const Mat* images[] = { &mask1, &mask2, &mask, &res };

	imshow("Origin image", img);
	for (int i = 0; i < 4; i++)
		imshow(titles[i], *(images[i]));

	imwrite("C:/Users/me/Desktop/Result.jpg", res); // Save the image result

	string fnamein = "C:/Users/me/Desktop/Result.jpg";
	string fnameout = "C:/Users/me/Desktop/Result.jpg";
	string path = "C:/Users/me/Desktop/";

	fnameout = path + "Result__" + datetime() + ".jpg";

	bool ok = filecopy(fnamein, fnameout);
	if (ok)
		cout << "succesful copy\n" << fnamein << "\nto\n" << fnameout << '\n';
	else
	{
		cout << "copy failed\n";
	}

	//Delete the Original result
	if (remove("C:/Users/me/Desktop/Result.jpg") != 0)
		perror("Error deleting file");
	else
	{
		puts("File successfully deleted");
	}

	auto stop = high_resolution_clock::now();   // stop clock
	auto duration = duration_cast<microseconds>(stop - start);		//calculate time
	cout << "Time taken : " << duration.count() << "microseconds" << endl; //show time 

	waitKey();
	return 0;
}