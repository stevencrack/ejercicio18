#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::endl;

int main(){

float y=1.0;
float x=0.0;
float h=0.1;
int n=(3.0/h);
float z=0.0;

for (int i=0;i<n;i++){
	
	y=y-h*y;
	x=x+h;
	
cout << x <<" "<< y << endl;    

	} 
return 0 ;
}
