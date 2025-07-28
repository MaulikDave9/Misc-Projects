import org.apache.spark.sql.SparkSession

object HelloWorldSpark {
  
  def main(args: Array[String]): Unit = {
  
    // Create SparkSession
    val spark = SparkSession.builder()
      .appName("HelloWorldSpark")
      .master("local[*]")  
      .getOrCreate()

    // Print Hello, World!
    println("Hello World - Using Apache Spark")

    // Stop the SparkSession
    spark.stop()
  }
  
}

