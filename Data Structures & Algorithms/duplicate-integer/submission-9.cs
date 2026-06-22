public class Solution {
    public bool hasDuplicate(int[] nums) {
        GC.Collect();
        HashSet<int> dict = new HashSet<int>();
        foreach(int i in nums){
            if(!dict.Contains(i)){
                dict.Add(i);
            } 
            else{
                return true;
            }            
        }
        return false;
    }
}