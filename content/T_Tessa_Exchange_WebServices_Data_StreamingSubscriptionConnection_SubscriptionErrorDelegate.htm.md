# StreamingSubscriptionConnection.SubscriptionErrorDelegate - делегат
Represents a delegate that is invoked when an error occurs within a streaming
subscription connection.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void SubscriptionErrorDelegate(
    	Object sender,
    	SubscriptionErrorEventArgs args
    )
VB __Копировать
     Public Delegate Sub SubscriptionErrorDelegate ( 
    	sender As Object,
    	args As SubscriptionErrorEventArgs
    )
C++ __Копировать
     public delegate void SubscriptionErrorDelegate(
    	Object^ sender, 
    	SubscriptionErrorEventArgs^ args
    )
F# __Копировать
     type SubscriptionErrorDelegate = 
        delegate of 
            sender : Object * 
            args : SubscriptionErrorEventArgs -> unit
#### Параметры
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
    The StreamingSubscriptionConnection instance within which the error occurred.
args
[SubscriptionErrorEventArgs](T_Tessa_Exchange_WebServices_Data_SubscriptionErrorEventArgs.htm)
    The event data.
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
