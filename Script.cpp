#include<iostream>
using namespace std;

int main(){
	int matrix1[][2] = {{1,3},{2,4}};
	int matrix2[][2]={{4,2},{3,1}};
	int matrix3[2][2];
	for(int i = 0; i < 2; i++){
		for(int j = 0; j < 2; j++){
			matrix3[i][j] = matrix1[i][j] + matrix2[i][j];
			cout << matrix3[i][j] << endl;
		}
		
	}
	return 0;
}
