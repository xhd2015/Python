#ifndef CPP_VIRT_H
#define CPP_VIRT_H

class base {

    public:

        base();
        virtual ~base();

        virtual int frobnicate(int i);

        int call_frob(int i);

    private:

        double _base_double;
};


class derived1 : public base {

    public:

        derived1();
        ~derived1();

        int frobnicate(int i);

    private:

        int _derived1_int;
};


class derived2 : public base {

    public:

        derived2();
        ~derived2();

        int frobnicate(int i);

    private:

        int _derived2_int;
};

#endif
