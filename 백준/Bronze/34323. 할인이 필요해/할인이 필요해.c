#include <stdio.h>

int main(){
    long long n, m, s;
    scanf("%lld %lld %lld", &n, &m, &s);

    long long n_discount = s * (m + 1) * (100 - n) / 100.0;
    long long m_discount = s * m;
    
    printf("%lld", n_discount < m_discount ? n_discount : m_discount);

    return 0;
}