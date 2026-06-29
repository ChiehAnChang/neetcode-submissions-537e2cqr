public class Solution
{
    public bool CheckInclusion(string s1, string s2)
    {
        if (s1.Length > s2.Length)
        {
            return false;
        }

        int[] s1Count = new int[26];
        int[] windowCount = new int[26];

        for (int i = 0; i < s1.Length; i++)
        {
            s1Count[s1[i] - 'a']++;
            windowCount[s2[i] - 'a']++;
        }

        if (IsSame(s1Count, windowCount))
        {
            return true;
        }

        for (int right = s1.Length; right < s2.Length; right++)
        {
            // 新字元進入 window
            windowCount[s2[right] - 'a']++;

            int left = right - s1.Length;
            windowCount[s2[left] - 'a']--;

            if (IsSame(s1Count, windowCount))
            {
                return true;
            }
        }

        return false;
    }

    private bool IsSame(int[] first, int[] second)
    {
        for (int i = 0; i < 26; i++)
        {
            if (first[i] != second[i])
            {
                return false;
            }
        }

        return true;
    }
}