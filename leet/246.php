<?php
class Solution {
    
    /**
     * @param String $num
     * @return Boolean
     */
    static function isStrobogrammatic(string $num): bool {
        $sb = [];
        
        foreach(str_split(strrev($num)) as $c) {
            if(in_array($c, ['0', '1', '8'])) $sb []= $c;
            else if($c == '6') $sb []= '9';
            else if($c == '9') $sb []= '6';
            else return false;
        }
        
        return implode('', $sb) == $num;
    }
}

echo Solution::isStrobogrammatic('69');