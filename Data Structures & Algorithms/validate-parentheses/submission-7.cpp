class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        unordered_map<char, char> bracket_dic = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char each_bracket : s) {
            if (each_bracket == '(' ||
                each_bracket == '[' ||
                each_bracket == '{') {

                st.push(each_bracket);

            } else {
                if (st.empty() ||
                    st.top() != bracket_dic[each_bracket]) {
                    return false;
                }

                st.pop();
            }
        }

        return st.empty();
    }
};