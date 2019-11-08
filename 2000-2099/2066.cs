using System;

namespace Application
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var a = int.Parse(Console.ReadLine());
            var b = int.Parse(Console.ReadLine());
            var c = int.Parse(Console.ReadLine());
            Console.WriteLine(Math.Min((a - b * c), (a - b - c)));
        }
    }
}
