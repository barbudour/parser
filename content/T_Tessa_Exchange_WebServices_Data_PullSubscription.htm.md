# PullSubscription - класс
Represents a pull subscription.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PullSubscription : SubscriptionBase
VB __Копировать
     Public NotInheritable Class PullSubscription
    	Inherits SubscriptionBase
C++ __Копировать
     public ref class PullSubscription sealed : public SubscriptionBase
F# __Копировать
     [<SealedAttribute>]
    type PullSubscription = 
        class
            inherit SubscriptionBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SubscriptionBase](T_Tessa_Exchange_WebServices_Data_SubscriptionBase.htm) __ PullSubscription
##  __Свойства
[Id](P_Tessa_Exchange_WebServices_Data_SubscriptionBase_Id.htm)|  Gets the Id
of the subscription.  
(Унаследован от
[SubscriptionBase](T_Tessa_Exchange_WebServices_Data_SubscriptionBase.htm))  
---|---  
[MoreEventsAvailable](P_Tessa_Exchange_WebServices_Data_PullSubscription_MoreEventsAvailable.htm)|
Gets a value indicating whether more events are available on the server.
MoreEventsAvailable is undefined (null) until GetEvents is called.  
[UsesWatermark](P_Tessa_Exchange_WebServices_Data_SubscriptionBase_UsesWatermark.htm)|
Gets whether or not this subscription uses watermarks.  
(Унаследован от
[SubscriptionBase](T_Tessa_Exchange_WebServices_Data_SubscriptionBase.htm))  
[Watermark](P_Tessa_Exchange_WebServices_Data_SubscriptionBase_Watermark.htm)|
Gets the latest watermark of the subscription. Watermark is always null for
streaming subscriptions.  
(Унаследован от
[SubscriptionBase](T_Tessa_Exchange_WebServices_Data_SubscriptionBase.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEvents](M_Tessa_Exchange_WebServices_Data_PullSubscription_GetEvents.htm)|
Obtains a collection of events that occurred on the subscribed folders since
the point in time defined by the Watermark property. When GetEvents succeeds,
Watermark is updated.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Unsubscribe](M_Tessa_Exchange_WebServices_Data_PullSubscription_Unsubscribe.htm)|
Unsubscribes from the pull subscription.  
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
