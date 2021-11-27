<?php


class UnionFind
{
    private array $parent;

    public function __construct(int $size) {
        for($i = 0; $i < $size; $i++) {
            $this->parent []= $i;
        }
    }
    
    public function find() {
    
    }
    
    public function union() {
    
    }
}

$uf = new UnionFind(5);


// end of file
