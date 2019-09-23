#include <opencv2/calib3d.hpp>
#include <iostream>
#include <opencv2/highgui/highgui.hpp> // an interface for UI capabilities
#include <opencv2/core/core.hpp> // module defining data structures, like Mat(multi-dimension array)

using namespace cv; // namespace where all the C++ OpenCV functionality resides
using namespace std;

int main(){
	// import image file
	Mat myFirstMatrix  = imread("7Mar2011.jpg");
	//myFirstMatrix.create(Size(500, 500), CV_8UC3);
	
	// check for absence of data//change
	/*if (!image.data) {
		cout << "Could not open or find an image.\n" << endl;
	}*/
	
	imshow("before:", myFirstMatrix);

	//cvWaitKey(50);
	//cout <<"\n" << endl;

	//change every third pixel
	//for (int i = 0; i < myFirstMatrix.rows; i++) {
		//for (int j = 0; j < myFirstMatrix.cols; j++) {
			//if (j % 3 == 0) {
				//myFirstMatrix.at<uchar>(i, j) = 255;
			//}
	//	}
	//}

	// make image brighter by given factor
	myFirstMatrix *= 2.5;

	imshow("after:", myFirstMatrix);
	waitKey(0);



	// set threshold for color detection
	// between "253 and 255"

	// mask will return values corresponding to threshold set
	// alg: if any white values in this mask, send a notification to end user

}	// end main()

