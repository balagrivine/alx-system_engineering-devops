#include <iostream>
#include <cmath>
#define PI 3.142

class Circle {
	//class to calculate the area of a circle
	
	private:
		float radius;
	public:
		void __init__(float r)//initializing funciton
		{
			radius = r;
		}
		float area(void)
		{
			//function to calculate the area
			return PI * pow(radius, 2);
		}
};

class Circumference {
	//class to calculate the circumference of a circle
	private:
		float radius;
		float result;
	public:
		float circ(float radius)
		{
			//function to calculate the circumference
			result = 2 * PI * radius;
			return result;
		}
};

int main(void)
{
	//driver function for the program
	Circle circle;
	Circumference circumference;
	float radius;

	std::cout << "Enter the radius for your circle: " <<std::endl;
	std::cin >> radius;
	circle.__init__(radius);

	//circle.area(radius);
	//circumference.circ(radius*2);

	std::cout << "The area of your circle is: " << circle.area() << std::endl;
	std::cout << "The circumference of your circle is: " << circumference.circ(radius) << std::endl;

	return 0;
}
