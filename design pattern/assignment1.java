interface Notification{
    void notifyUser();
}

class SmsNotification implements Notification{
    @Override
    public void notifyUser(){
        System.out.println("sending sms notification");
    }
}

class EmailNotification implements Notification {
    @Override
    public void notifyUser() {
        System.out.println("sending Email notification");
    }
}


class PushNotification implements Notification {
    @Override
    public void notifyUser() {
        System.out.println("sending Push notification");
    }
}


class NotificationFactory{
    public Notification createNotification(String type){
        if(type.equalsIgnoreCase("sms"))
            return new SmsNotification();
        if (type.equalsIgnoreCase("email"))
            return new EmailNotification();
        if (type.equalsIgnoreCase("push"))
            return new PushNotification();
        return null;
    }
}


public class assignment1 {
    public static void main(String[] args) {
        NotificationFactory factory = new NotificationFactory();
        Notification notification = factory.createNotification("sms");
        notification.notifyUser();
    }
}
