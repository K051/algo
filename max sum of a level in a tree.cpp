int maxLevelSum(TreeNode* root) {
        queue<TreeNode*> q;
        if(root)q.push(root);
        int sum = INT_MIN;
        int l=1;
        int ans = -1;
        while(!q.empty()) {
            int n = q.size();
            int temp=0;
            while(n--) {
                auto a = q.front();
                if(a->left)q.push(a->left);
                if(a->right)q.push(a->right);
                q.pop();
                temp+=a->val;
            }
            if(temp>sum) {
                ans = l;
                sum=temp;
            }
            l++;
        }
        return ans;
    }
