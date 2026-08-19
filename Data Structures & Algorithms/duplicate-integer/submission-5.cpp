class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> checklist;

        for (const int& each_n : nums){

            if (!checklist.insert(each_n).second){
                return true;
            }


        }
        return false;


        // unordered_set<int> number_checklist;

        // for (const int & num : nums){

        //     if (!number_checklist.insert(num).second){
        //         return true;
        //     }
            
        // }

        // return false;



    }
};