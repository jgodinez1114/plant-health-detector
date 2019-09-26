#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;

int main()
{
	Mat image = imread("C:/Users/me/Desktop/leaf.jpg", 1);
	Mat OutputImage;

	inRange(image, Scalar(50,69,101), Scalar(111,138,183),OutputImage);//Blue Green Red

	namedWindow("image", WINDOW_AUTOSIZE);
	imshow("image", image);
	namedWindow("Output", WINDOW_FREERATIO);
	imshow("Output", OutputImage);
	waitKey(0);
}