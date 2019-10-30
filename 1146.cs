using System;

namespace MaxSum
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var n = int.Parse(Console.ReadLine());
            var inputArray = new int[n, n];

            for (int i = 0; i < n; i++)
            {
                var strings = Console.ReadLine().Split(' ');
                for (int j = 0; j < n; j++)
                {
                    inputArray[i, j] = int.Parse(strings[j]);
                }
            }

            var arr = new int[n, n];

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (j == 0)
                        arr[i, j] = inputArray[i, j];
                    else
                        arr[i, j] = inputArray[i, j] + arr[i, j - 1];
                }    
            }

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (i == 0)
                        continue;
                    else
                        arr[i, j] = arr[i, j] + arr[i - 1, j];
                }
            }

            var max = int.MinValue;
            for (int x1 = 0; x1 < n; x1++)
            {
                for (int x2 = 0; x2 <= x1; x2++)
                {
                    for (int y1 = 0; y1 < n; y1++)
                    {
                        for (int y2 = 0; y2 <= y1; y2++)
                        {
                            var a = 0;
                            if (y2 != 0)
                            {
                                a = arr[x1, y2 - 1];
                            }

                            var b = 0;
                            if (x2 != 0)
                            {
                                b = arr[x2 - 1, y1];
                            }

                            var c = 0;
                            if (x2 != 0 && y2 != 0)
                            {
                                c = arr[x2 - 1, y2 - 1];
                            }

                            var s = arr[x1, y1] - a - b + c;
                            if (s > max) max = s;
                        }
                    }
                }
            }

            Console.WriteLine(max);
        }
    }
}
