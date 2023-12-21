# StreamingSubscriptionConnection.NotificationEventDelegate - делегат
Represents a delegate that is invoked when notifications are received from the
server
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void NotificationEventDelegate(
    	Object sender,
    	NotificationEventArgs args
    )
VB __Копировать
     Public Delegate Sub NotificationEventDelegate ( 
    	sender As Object,
    	args As NotificationEventArgs
    )
C++ __Копировать
     public delegate void NotificationEventDelegate(
    	Object^ sender, 
    	NotificationEventArgs^ args
    )
F# __Копировать
     type NotificationEventDelegate = 
        delegate of 
            sender : Object * 
            args : NotificationEventArgs -> unit
#### Параметры
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
    The StreamingSubscriptionConnection instance that received the events.
args
[NotificationEventArgs](T_Tessa_Exchange_WebServices_Data_NotificationEventArgs.htm)
    The event data.
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
