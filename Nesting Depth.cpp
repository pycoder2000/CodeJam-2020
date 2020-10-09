#include <bits/stdc++.h>


int main()
{
    long long t;
    std::cin >> t;
    long long test = 1;
    while (t--)
    {
        std::string a;
        std::cin >> a;
        std::vector<long long> vc;
        long long n = a.length();
        for (long long i = 0; i < a.length(); i++)
        {
            vc.push_back(a[i] - '0');
        }
        std::cout << "Case #" << test << ": ";
        long long cc = vc[0];
        while (cc--)
        {
            std::cout << '(';
        }
        std::cout << vc[0];

        for (long long i = 1; i < n; i++)
        {
            if (vc[i] - vc[i - 1] > 0)
            {
                long long c = abs(vc[i] - vc[i - 1]);
                while (c--)
                {
                    std::cout << '(';
                }
                std::cout << vc[i];
            }
            else if (vc[i] - vc[i - 1] == 0)
            {
                std::cout << vc[i];
            }
            else
            {
                long long c = abs(vc[i] - vc[i - 1]);
                while (c--)
                {
                    std::cout << ')';
                }
                std::cout << vc[i];
            }
        }
        while (vc[n - 1]--)
        {
            std::cout << ')';
        }

        std::cout << " " << std::endl;
        test++;
    }
}
