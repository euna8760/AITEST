using System;

class Program
{
    static void Main()
    {
        var numbers = new int[] { 1, 2, 3, 4, 5 };
        var result = CalculateAverage(numbers);
        Console.WriteLine($"Average: {result}");
    }

    // 문제 1: null 체크 없음
    static double CalculateAverage(int[] numbers)
    {
        int sum = 0;
        for (int i = 0; i <= numbers.Length; i++)  // 문제 2: 인덱스 오류
        {
            sum += numbers[i];
        }
        return sum / numbers.Length;  // 문제 3: 빈 배열 처리 안됨
    }

    // 문제 4: SQL 인젝션 취약점
    static string GetUserData(string userId)
    {
        string query = "SELECT * FROM Users WHERE Id = " + userId;
        return query;
    }
}