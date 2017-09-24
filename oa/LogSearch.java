import java.util.*;
import java.lang.*;
import java.util.regex.*;

class LogSearch {

  public static List<Integer> logParse(String s){
    List<Integer> lp = new ArrayList<>();

    String pattern = "^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2})Z$";
    Pattern p = Pattern.compile(pattern);
    Matcher m = p.matcher(s);
    if(m.find()){
      for(int i = 1; i <= m.groupCount(); ++i){
        lp.add(Integer.parseInt(m.group(i)));
      }
    }
    else{
      throw new IllegalArgumentException();
    }

    return lp;
  }

  public static int logCompare(List<Integer> lhs, List<Integer> rhs){
    return -1;
  }

  public static List<String> logSearch(List<String> logs,
  List<Integer> ts0, List<Integer> ts1){
    List<String> res = new ArrayList<>();
    // regex
    for(String s : logs){
      // logCompare()
    }
    return res;
  }

  public static void main(String[] args){
    String ts0 = "2016-02-12T03:21:55Z";
    String ts1 = "2016-02-12T03:22:00Z";

    Scanner sc = new Scanner(System.in);
    String ts = sc.nextLine();
    List<Integer> dt = logParse(ts);
    for(int num : dt){
      System.out.println(num);
    }

    return;
  }
}
