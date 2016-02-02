%module tmpl_list
%{
#include "tmpl_list.hpp"
%}

%include "tmpl_list.hpp"

%template(Listi) List<int>;
%template(Listl) List<long>;
%template(Listf) List<float>;
%template(Listd) List<double>;

%pythoncode %{

listtype_from_type = {
    'i' : Listi,
    'l' : Listl,
    'f' : Listf,
    'd' : Listd,
}

class List(object):
    def __init__(self, maxsize, dtype):
        self.dtype = dtype
        self.maxsize = maxsize
        self._list = listtype_from_type[dtype](maxsize)

    def __getattribute__(self, attr):
        ll = object.__getattribute__(self, '_list')
        return getattr(ll, attr)
    
    def __len__(self):
        return self.length()
%}
