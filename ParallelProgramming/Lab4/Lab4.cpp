/**
 * Паралельне програмування
 * Лабораторна робота №4 Бібліотека OpenMP. Бар’єри, критичні секції
 * Варіант 21
 * Завдання: R = max(Z)*(B*MV) +e*X*(MM*MC)
 * ПВВ1 – MV, MC, ПВВ2 – MM, R, ПВВ4 – B,X,e, Z
 * Грицюк Максим ІО-02
 * Дата 20 11 2022
 **/
#include <omp.h>
#include <iostream>
using namespace std;

const int N = 8;
int R[N], Z[N], B[N], X[N], MM[N][N], MV[N][N], MC[N][N], e;
int a = 0;
int tempMatrix[N][N];
const int P = 4;
const int H = N / P;

void initMatrix(int MX[N][N]);
void initVector(int X[N]);
int max(int X[N], int i);
void multiplyMatrixAndSubMatrix(int MX[N][N], int MY[N][N], int id);
void calculateResultPart(int ai, int ei, int id);
void printResult();

int main(int argc, char *argv[])
{
    omp_lock_t Lock1;
    omp_lock_t Lock2;
    omp_init_lock(&Lock1);
    omp_init_lock(&Lock2);

    cout << "Lab4 has started" << endl;
    cout << "N = " << N << "; P = " << P << endl
         << endl;
#pragma omp parallel num_threads(P)
    {
        int id = omp_get_thread_num() + 1;
        cout << "T" << id << " is started" << endl;

        // Уведення
        if (id == 1)
        {
            // 1 Уведення MV, MC
            initMatrix(MV);
            initMatrix(MC);
        }
        else if (id == 2)
        {
            // 2 Уведення MM
            initMatrix(MM);
        }
        else if (id == 4)
        {
            // 4 Уведення B, X, e, Z
            initVector(B);
            initVector(X);
            initVector(Z);
            e = 1;
        }

#pragma omp barrier

        int ai;
        // Обчислення 1
        ai = max(Z, id);

// Обчислення 2
#pragma omp critical
        a = a + ai;

#pragma omp barrier

        int ei;
        // Копія a, e
        omp_set_lock(&Lock1);
        ai = a;
        omp_unset_lock(&Lock1);
        omp_set_lock(&Lock2);
        ei = e;
        omp_unset_lock(&Lock2);
        // Обчислення 4
        calculateResultPart(ai, ei, id);

#pragma omp barrier

        if (id == 2)
        {
            printResult();
        }

        string fin = "T" + to_string(id) + " has finished";
        cout << fin << endl;
    }
    cout << "Lab4 has finished" << endl;
}

void initMatrix(int MX[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            MX[i][j] = 1;
        }
    }
}

void initVector(int X[N])
{
    for (int i = 0; i < N; i++)
    {
        X[i] = 1;
    }
}

int max(int X[N], int i)
{
    int start = (i - 1) * H;
    int end = i * H;
    int max = X[start];
    for (int j = start; j < end; j++)
    {
        if (X[j] > max)
        {
            max = X[j];
        }
    }
    return max;
}

void multiplyMatrixAndSubMatrix(int MX[N][N], int MY[N][N], int id)
{
    int start = (id - 1) * H;
    int end = id * H;
    for (int i = 0; i < N; i++)
    {
        int g = 0;
        for (int j = start; j < end; j++)
        {
            tempMatrix[i][g] = 0;
            for (int k = 0; k < N; k++)
            {
                tempMatrix[i][g] += MX[i][k] * MY[k][j];
            }
            g++;
        }
    }
}

void calculateResultPart(int ai, int ei, int id)
{
    int start = (id - 1) * H;
    int finish = id * H;
    multiplyMatrixAndSubMatrix(MM, MC, id);
    for (int i = start; i < finish; i++)
    {
        int temp1 = 0;
        int temp2 = 0;
        for (int j = 0; j < N; j++)
        {
            temp1 += B[j] * MV[i][j];
            temp2 += X[j] * tempMatrix[i][j];
        }
        R[i] = ai * temp1 + ei * temp2;
    }
}

void printResult()
{
    string out;
    for (int i = 0; i < N; i++)
    {
        out += to_string(R[i]) + " ";
    }
    out = "R: " + out;
    cout << out << endl;
}
