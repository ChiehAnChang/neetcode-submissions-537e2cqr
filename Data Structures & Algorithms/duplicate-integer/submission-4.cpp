class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> number_checklist;

        for (const int & num : nums){

            if (!number_checklist.insert(num).second){
                return true;
            }
            
        }

        return false;



    }
};