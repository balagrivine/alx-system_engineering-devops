#include <iostream>
using namespace std;

class Person {
	//A class defining a details of a student
	
	private:
		char name[30];
		int age;
	public:
		void setdetails(void);
	        void displaydetails(void);
};

                void Person:: setdetails(void)
		{
		  cout<<"enter your name:"<<endl;
		  cin >> name;
		  cout<<"enter your age:"<<endl;
		  cin>>age;
		}

		void Person ::displaydetails(void)
		{
                cout<<"name:"<<name<<endl;
		cout<<"age:"<<age<<endl;
		}

    
     int main()
{
        Person p;
	p.setdetails();
	p.displaydetails();


	return 0;
	
}
