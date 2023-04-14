/**
 * Курсова робота. Частина 2
 * Варіант 9
 * Завдання: a = min(B + Z*(MR*MX)) + (B*Z)
 * ПВВ1 – a, MX, B
 * ПВВP – Z, MZ, MR
 * Грицюк Максим ІО-02
 * Дата: 14.04.2023
 **/
#include <omp.h>
#include <iostream>
#include <string>
using namespace std;
const int N = 12;
const int P = 12;
const int H = N / P;
int MA[N][N];
int MX[N][N];
int B[N];
int MZ[N][N];
int MR[N][N];
int Z[N];
int a;
int b = 100000;
int c;

void FillMatrix(int Matrix[N][N]);
void FillVector(int Vector[N]);
int Calculation1(int id);
void Calculation2(int bi);
int Calculation3(int id);
void Calculation4(int ci);
void Calculation5(int id);
int main(int argc, char* argv[])
{
    // Ініціалізація Lock об'єктів критичних секцій для операції копіювання b, c
    omp_lock_t Lock1;
    omp_lock_t Lock2;
    omp_init_lock(&Lock1);
    omp_init_lock(&Lock2);
    // Початок виконання
#pragma omp parallel num_threads(P)
    {
        // Визначення id потоку
        int id = omp_get_thread_num() + 1;
        printf("T%d is started\n", id);

        // Уведення
        if (id == 1)
        {
            // Уведення MX, B
            FillMatrix(MX);
            FillVector(B);
        }
        else if (id == P)
        {
            // Уведення Z, MZ, MR
            FillVector(Z);
            FillMatrix(MZ);
            FillMatrix(MR);
        }
        // Бар'єр (чекаємо введення у потоках 1 та P)
#pragma omp barrier
        int b_i;
        // Обчислення 1
        b_i = Calculation1(id);
        // Обчислення 2 (Критична секція 1)
#pragma omp critical
        Calculation2(b_i);
        int c_i;
        // Обчислення 3
        c_i = Calculation3(id);
        // Обчислення 4 (Критична секція 2)
#pragma omp critical
        Calculation4(c_i);
        // Бар'єр (чекати закінчення обчислення 1,2,3,4)
#pragma omp barrier
        // Копія b_i = b (Критична секція 3)
        omp_set_lock(&Lock1);
        b_i = b;
        omp_unset_lock(&Lock1);
        // Копія c_i = c (Критична секція 4)
        omp_set_lock(&Lock2);
        c_i = c;
        omp_unset_lock(&Lock2);

        // Обчислення 5
        Calculation5(id);
        // Бар'єр (чекаємо закінчення обчислення 5)
#pragma omp barrier
    // Вивід
        printf("T%d is finished\n", id);
        if (id == 1)
        {
            printf("Result is %d \n", a);
        }
    }
}
void FillMatrix(int Matrix[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            Matrix[i][j] = 1;
        }
    }
}
void FillVector(int Vector[N])
{
    for (int i = 0; i < N; i++)
    {
        Vector[i] = 1;
    }
}
int Calculation1(int id)
{
    int start = (id - 1) * H;
    int finish = id * H;
    // (MR*MX_H)
    int temp1[N][H];
    for (int i = 0; i < N; i++)
    {
        int g = 0;
        for (int j = 0; j < H; j++)
        {
            temp1[i][g] = 0;
            for (int k = 0; k < N; k++)
            {
                temp1[i][g] += MR[i][k] * MX[k][j];
            }
            g++;
        }
    }
    // Z * temp1 -> temp2
    int temp2[H];
    for (int i = 0; i < H; i++)
    {
        temp2[i] = 0;
        for (int j = 0; j < N; j++)
        {
            temp2[i] += Z[j] * temp1[j][i];
        }
    }
    // B + temp2 -> temp3
    int temp3[H];
    for (int i = 0; i < N; i++) {
        temp3[i] = B[i] + temp2[i];
    }
    // min(temp3)
    int min = temp3[0];
    for (int i = 0; i < H; i++) {
        if (min > temp3[i]) {
            min = temp3[i];
        }
    }
    return min;
}

void Calculation2(int b_i)
{
    if (b_i < b)
    {
        b = b_i;
    }
}
int Calculation3(int id)
{
    int start = (id - 1) * H;
    int finish = id * H;
    int res = 0;
    for (int i = start; i < finish; i++) {
        res += B[i] * Z[i];
    }
    return res;
}
void Calculation4(int ci)
{
    c = c + ci;
}
void Calculation5(int id)
{
    a = b + c;
}