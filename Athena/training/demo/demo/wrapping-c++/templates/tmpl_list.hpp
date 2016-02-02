template<class T>
class List {
public:
    List(int max) {
      data = new T [max];
      nitems = 0;
      maxitems = max;
    }
    ~List() {
      delete [] data;
    };
    void append(T obj) {
      if (nitems < maxitems) {
        data[nitems++] = obj;
      }
    }
    int length() {
      return nitems;
    }
    T get(int n) {
      return data[n];
    }
private:
    T *data;
    int nitems;
    int maxitems;
};
