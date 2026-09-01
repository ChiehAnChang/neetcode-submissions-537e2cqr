class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> check_map;

        for (const int& each_num : nums) {
            if (!check_map.contains(each_num)) {
                check_map[each_num] = 1;
            } else {
                check_map[each_num]++;
            }
        }

        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > min_hp;

        for (const auto& [each_key, frequency] : check_map) {

            if (min_hp.size() < k) {
                min_hp.push({frequency, each_key});

            } else {
                if (frequency > min_hp.top().first) {
                    min_hp.pop();
                    min_hp.push({frequency, each_key});
                }
            }
        }

        vector<int> result;

        while (!min_hp.empty()) {
            result.push_back(min_hp.top().second);
            min_hp.pop();
        }

        return result;
    }
};