def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10, [])      #[10]
list2 = extendList(123, [])     #[123]
list3 = extendList('a')         #?


