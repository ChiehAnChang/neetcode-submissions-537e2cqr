class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> res_map;

        for (int i = 0; i < strs.size(); i++) {

            vector<int> temp_count(26, 0);

            for (int each_ch_i = 0; each_ch_i < strs[i].size(); each_ch_i++) {
                char each_ch = strs[i][each_ch_i];
                temp_count[each_ch - 'a']++;
            }

            string each_index_str = "";

            for (int each_i = 0; each_i < temp_count.size(); each_i++) {
                each_index_str += "," + to_string(temp_count[each_i]);
            }

            res_map[each_index_str].push_back(strs[i]);
        }

        vector<vector<string>> res;

        for (const auto& each_group : res_map) {
            res.push_back(each_group.second);
        }

        return res;
    }
};