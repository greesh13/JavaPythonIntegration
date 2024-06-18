import py4j.GatewayServer;

public class MyJavaEntryPoint {
    private MyJavaClass myJavaClass;

    public MyJavaEntryPoint() {
        myJavaClass = new MyJavaClass();
    }

    public MyJavaClass getMyJavaClass() {
        return myJavaClass;
    }

    public static void main(String[] args) {
        MyJavaEntryPoint entryPoint = new MyJavaEntryPoint();
        GatewayServer server = new GatewayServer(entryPoint);
        server.start();
        System.out.println("Gateway Server Started");
    }
}
