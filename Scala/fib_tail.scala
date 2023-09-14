object Main extends App {
    def fib(n: Int): Int = {
      @annotation.tailrec
      def loop(n: Int, prev: Int, curr: Int): Int = {
        if (n <= 0) prev
        else loop(n - 1, curr, prev + curr)
      }

      loop(n, 0, 1)
    }
    print(fib(4))
}