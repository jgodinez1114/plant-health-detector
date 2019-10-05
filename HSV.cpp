#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <chrono>
using namespace std;
using namespace cv;
using namespace std::chrono; //clock

int main()
{
	auto start = high_resolution_clock::now(); //clock
	Mat img = imread("C:/Users/me/Desktop/leaf.jpg");
	// Convert BGR to HSV
	Mat hsv;
	cvtColor(img, hsv, COLOR_BGR2HSV);

	//inRange(image, Scalar(50,69,101), Scalar(111,138,183),OutputImage); //Blue Green Red
	// define range of red color in HSV
	Scalar lower_red1 = Scalar(10, 50, 50);//(23, 0, 0);	//0-180,0-255,0-255 
	Scalar upper_red1 = Scalar(15, 255, 255);//(33, 250,250);

	Scalar lower_red2 = Scalar(15 , 50, 50);//(169, 240, 240);
	Scalar upper_red2 = Scalar(20, 255, 255);//(179, 250, 250);

	// Threshold the HSV image to get only red colors
	Mat mask1, mask2;
	inRange(hsv, lower_red1, upper_red1, mask1);
	inRange(hsv, lower_red2, upper_red2, mask2);

	Mat mask;
	bitwise_or(mask1, mask2, mask);

	// Bitwise - AND mask and original image
	Mat res;
	bitwise_and(img, img, res, mask);

	const char* titles[] = { "Red mask 1", "Red mask 2", "Final mask", "Result" };
	const Mat* images[] = { &mask1, &mask2, &mask, &res };

	imshow("Origin image", img);
	for (int i = 0; i < 4; i++)
		imshow(titles[i], *(images[i]));

	auto stop = high_resolution_clock::now();   //clock
	auto duration = duration_cast<microseconds>(stop - start);		//clock
	cout << "Time taken : " << duration.count() << "microseconds" << endl; //clock

	waitKey();
	return 0;
}