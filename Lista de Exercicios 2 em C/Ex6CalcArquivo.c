#include <stdio.h>
int main(){

float megabyte, mbps, minutos , MBps;

printf("Qual e o tamanho do arquivo em MB? ");
scanf("%f", &megabyte);

printf("Qual a velocidade em Mbps da sua internet? ");
scanf("%f", &mbps);

MBps = (mbps/8);
minutos = (megabyte/MBps) / 60;

printf("Tempo aproximado de download: %.2f minutos\n\n", minutos);

return 0;
}
