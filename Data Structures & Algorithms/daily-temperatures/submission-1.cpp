class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> st;
        vector<int> res(temperatures.size(), 0);

        for (int i = 0; i < static_cast<int>(temperatures.size()); i++) {
            int each_temperature = temperatures[i];

            while (!st.empty() &&
                   st.top().first < each_temperature) {

                pair<int, int> prev = st.top();
                st.pop();

                res[prev.second] = i - prev.second;
            }

            st.push({each_temperature, i});
        }

        return res;
    }
};