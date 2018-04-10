#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::endl;

int main(){
	
	float x = 0.0;

	float y = 1.0;

	float z = 0.0;

	float h = 0.1;

	int N = 10/h;

	int i;


	for(i=0; i<N; i++){
		
		float t1 = z;
		float t2 = y;
		y = y + h*z;
		z = z - h*y;
		x = x+h;
		cout << x << " " << y << " " << z << endl;
		
	}	

	return 0;
}
