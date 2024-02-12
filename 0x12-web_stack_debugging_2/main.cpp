#include <iostream>

class Shape {
	private:
		int length;
		int width;
	public:
		int area(int length, int width)
		{
			return length * width;
		}
};
int main(void)
{
	Shape rectangle;
	int result = rectangle.area(2, 2);
	std::cout << result << std::endl;
	return 0;
}
