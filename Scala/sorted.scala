object Main extends App {
    def fib(n: Int): Int = {
      @annotation.tailrec
      def loop(n: Int, prev: Int, curr: Int): Int = {
        if (n <= 0) prev
        else loop(n - 1, curr, prev + curr)
      }

      loop(n, 0, 1)
    }
    
    def isSorted[A](as: Array[A], ordered: (A,A) => Boolean): Boolean = {
        @annotation.tailrec
        def loop(n: Int): Boolean =
            if( n == as.length - 1 ) true
            else if (ordered(as(n),as(n+1))) loop(n+1)
            else false
        loop(0)
        
        
    }
    def int_cmp( num1: Int, num2:Int ) : Boolean = {
        num1 <= num2
        
    }
    val a: Array[Int] =  Array(1, 2, 3, 4, 5)
    print(isSorted(a,int_cmp))
}