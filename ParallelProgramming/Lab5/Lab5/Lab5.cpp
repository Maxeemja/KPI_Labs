/**
 * Паралельне програмування
 * Лабораторна робота No5 Бібліотека MPI
 * Завдання: A = Z*MS*e + D*(MX*MS)
 * ПВВ2 – MX, A; ПВВ3 – Z, D; ПВВ6 – MS, e
 * Грицюк Максим ІО-02
 * Дата 10 12 2022
 **/
#include <mpi.h>
#include <iostream>
#include <string>
using namespace std;
const int N = 6;
const int P = 6;
const int H = N / P;
int MX[N][N], Z[N], D[N],MS[N][N], MS_H[N][N], e, A[N], A_H[N];
int temp1[N][H], temp2[H], temp3[H];
void calculate();
void inputMatrix(int MX[N][N]);
void inputVector(int X[N]);
void outResult(int A[N]);
int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);
    int tid;
    MPI_Comm_rank(MPI_COMM_WORLD, &tid);
    MPI_Status status;
    cout << "T" << tid + 1 << " started" << endl;
    int index[6] = { 1, 3, 5, 7, 9, 10 };
    int edges[10] = { 1, 0, 2, 1, 3, 2, 4, 3, 5, 4 };
    MPI_Comm graph;
    MPI_Graph_create(MPI_COMM_WORLD, 6, index, edges, 1, &graph);
    if (tid == 1)
    {
        // введення МХ
        inputMatrix(MX);
    }
    else if (tid == 2)
    {
        // введення Z, D
        inputVector(Z);
        inputVector(D);
    }
    else if (tid == 5)
    {
        // введення MS, e
        inputMatrix(MS);
        e = 1;
    }
    // Передати і прийняти: Z
    MPI_Bcast(&Z, N, MPI_INT, 2, graph);
    // Передати і прийняти: D
    MPI_Bcast(&D, N, MPI_INT, 2, graph);
    // Передати і прийняти: MS_H
    MPI_Scatter(&MS, H * N, MPI_INT, &MS_H, H * N, MPI_INT, 5, graph);
    // Передати і прийняти: e
    MPI_Bcast(&e, 1, MPI_INT, 5, graph);
    // Передати і прийняти: MX
    MPI_Bcast(&MX, N * N, MPI_INT, 1, graph);
    // Обчислення 1 Ah = Z*MSh*e + D*(MX*MSh)
    calculate();
    // Збирання частин A
    MPI_Gather(&A_H, H, MPI_INT, &A, H, MPI_INT, 1, graph);
    // Вивід A
    if (tid == 1)
    {
        outResult(A);
    }
    cout << "T" << tid + 1 << " finished" << endl;
    MPI_Finalize();
    return 0;
}
void calculate()
{
    for (int i = 0; i < H; i++) {
        int tmp1 = 0;
        int tmp3 = 0;
        for (int j = 0; j < N; j++) {
            int tmp2 = 0;
            for (int k = 0; k < N; k++) {
                tmp2 += MX[k][j] * MS_H[i][k];
            }
            tmp1 += D[j] * tmp2;
            tmp3 += Z[j] * MS_H[i][j];
        }
        A_H[i] = tmp3 * e + tmp1;
    }
}
void inputMatrix(int MX[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            MX[i][j] = 1;
        }
    }
}
void inputVector(int X[N])
{
    for (int i = 0; i < N; i++)
    {
        X[i] = 1;
    }
}
void outResult(int A[N])
{
    string out;
    for (int i = 0; i < N; i++)
    {
        out += to_string(A[i]) + " ";
    }
    out = "A: " + out;
    cout << out << endl;
}
