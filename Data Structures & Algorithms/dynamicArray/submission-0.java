class DynamicArray {
    int size;
    int capacity;
    private int[] arr;
    public DynamicArray(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        arr = new int[capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (this.getCapacity() == this.getSize()) {
            this.resize();
            this.set(this.size, n);
        } else {
            this.set(this.size, n);
        }
        this.size ++;
    }

    public int popback() {
        int lastVal = arr[this.getSize() - 1];
        this.size --;
        return lastVal;
    }

    private void resize() {
        this.capacity *= 2;
        int[] oldarr = arr;
        arr = new int[capacity];
        for(int i = 0; i < this.size; i++){
            arr[i] = oldarr[i];
        }
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
