# StreamingSubscriptionConnection - класс
Represents a connection to an ongoing stream of events.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StreamingSubscriptionConnection : IDisposable
VB __Копировать
     Public NotInheritable Class StreamingSubscriptionConnection
    	Implements IDisposable
C++ __Копировать
     public ref class StreamingSubscriptionConnection sealed : IDisposable
F# __Копировать
     [<SealedAttribute>]
    type StreamingSubscriptionConnection = 
        class
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StreamingSubscriptionConnection
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[StreamingSubscriptionConnection(ExchangeService,
Int32)](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection__ctor_1.htm)|
Initializes a new instance of the StreamingSubscriptionConnection class.  
---|---  
[StreamingSubscriptionConnection(ExchangeService,
IEnumerable<StreamingSubscription>,
Int32)](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection__ctor.htm)|
Initializes a new instance of the StreamingSubscriptionConnection class.  
## __Свойства
[CurrentSubscriptions](P_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_CurrentSubscriptions.htm)|
Getting the current subscriptions in this connection.  
---|---  
[IsOpen](P_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_IsOpen.htm)|
Gets a value indicating whether this connection is opened  
## __Методы
[AddSubscription](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_AddSubscription.htm)|
Adds a subscription to this connection.  
---|---  
[Close](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_Close.htm)|
Closes this connection so it stops receiving events from the server. This
terminates a long-standing call to EWS.  
[Dispose](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_Dispose.htm)|
Frees resources associated with this StreamingSubscriptionConnection.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_Finalize.htm)|
Finalizes an instance of the StreamingSubscriptionConnection class.  
(Переопределяет
[Object.Finalize()](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Open](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_Open.htm)|
Opens this connection so it starts receiving events from the server. This
results in a long-standing call to EWS.  
[RemoveSubscription](M_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_RemoveSubscription.htm)|
Removes the specified streaming subscription from the connection.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[OnDisconnect](E_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_OnDisconnect.htm)|
Occurs when a streaming subscription connection is disconnected from the
server.  
---|---  
[OnNotificationEvent](E_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_OnNotificationEvent.htm)|
Occurs when notifications are received from the server.  
[OnSubscriptionError](E_Tessa_Exchange_WebServices_Data_StreamingSubscriptionConnection_OnSubscriptionError.htm)|
Occurs when a subscription encounters an error.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
