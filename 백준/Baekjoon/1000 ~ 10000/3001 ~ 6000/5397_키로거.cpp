#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stack>

using namespace std;
int main() {
	int testcase;
	stack<char> stack1;
	stack<char> stack2;
	
	cin >> testcase;
	while (testcase--) {
		char input[1000001];
		cin >> input;
		int len = strlen(input); //시간초과 때문에 만든 변수
		//cout << strlen(input);
		for (int i = 0; i < len; i++) {
			if (input[i] != '<' && input[i] != '>' && input[i] != '-') {
				stack1.push(input[i]);
			}
			if (input[i] == '<' && !stack1.empty()) {
				stack2.push(stack1.top());
				//cout <<"stack2: " <<stack1.top()<<"\n";
				stack1.pop();
			}
			if (input[i] == '>' && !stack2.empty()) {
				stack1.push(stack2.top());
				//cout << "stack1: " << stack2.top() << "\n";
				stack2.pop();
			}
			if (input[i] == '-' && !stack1.empty()) {
				stack1.pop();
			}
		}
		while (!stack1.empty()) {
			stack2.push(stack1.top());
			stack1.pop();
		}
		while (!stack2.empty()) {
			cout << stack2.top();
			stack2.pop();
		}
		cout << "\n";
	}
}