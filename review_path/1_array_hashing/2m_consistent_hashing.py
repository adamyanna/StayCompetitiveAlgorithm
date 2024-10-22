#!/usr/bin/env python3

"""
// Golang
type Hash func(data []byte) uint32
type Map struct {
    hash     Hash   // 计算 hash 的函数
    replicas int    // 这个是副本数，这里影响到虚拟节点的个数
    keys     []int  // 有序的列表，从大到小排序的，这个很重要
    hashMap  map[int]string // 可以理解成用来记录虚拟节点和物理节点元数据关系的
}

func New(replicas int, fn Hash) *Map {
    m := &Map{
        replicas: replicas,
        hash:     fn,
        hashMap:  make(map[int]string),
    }
    if m.hash == nil {
        // 默认可以用 crc32 来计算hash值
        m.hash = crc32.ChecksumIEEE
    }
    return m
}

func (m *Map) Add(keys ...string) {
    // keys => [ A, B, C ]
    for _, key := range keys {
        for i := 0; i < m.replicas; i++ {
            // hash 值 = hash (i+key)
            hash := int(m.hash([]byte(strconv.Itoa(i) + key)))
            m.keys = append(m.keys, hash)
            // 虚拟节点 <-> 实际节点
            m.hashMap[hash] = key
        }
    }
    sort.Ints(m.keys)
}

func (m *Map) Get(key string) string {
    if m.IsEmpty() {
        return ""
    }
    // 根据用户输入key值，计算出一个hash值
    hash := int(m.hash([]byte(key)))
    // 查看值落到哪个值域范围？选择到虚节点
    idx := sort.Search(len(m.keys), func(i int) bool { return m.keys[i] >= hash })
    if idx == len(m.keys) {
        idx = 0
    }
    // 选择到对应物理节点
    return m.hashMap[m.keys[idx]]
}
"""