public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        HashSet<char> checkSet = new HashSet<char>();

        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.Length; right++)
        {
            while (checkSet.Contains(s[right]))
            {
                checkSet.Remove(s[left]);
                left++;
            }

            checkSet.Add(s[right]);

            maxLength = Math.Max(
                maxLength,
                right - left + 1
            );
        }

        return maxLength;
    }
}