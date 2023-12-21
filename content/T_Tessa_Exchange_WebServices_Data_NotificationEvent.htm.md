# NotificationEvent - класс
Represents an event as exposed by push and pull notifications.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NotificationEvent
VB __Копировать
     Public MustInherit Class NotificationEvent
C++ __Копировать
     public ref class NotificationEvent abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type NotificationEvent = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationEvent
Derived
[Tessa.Exchange.WebServices.Data.FolderEvent](T_Tessa_Exchange_WebServices_Data_FolderEvent.htm)
[Tessa.Exchange.WebServices.Data.ItemEvent](T_Tessa_Exchange_WebServices_Data_ItemEvent.htm)
##  __Свойства
[EventType](P_Tessa_Exchange_WebServices_Data_NotificationEvent_EventType.htm)|
Gets the type of this event.  
---|---  
[OldParentFolderId](P_Tessa_Exchange_WebServices_Data_NotificationEvent_OldParentFolderId.htm)|
Gets the Id of the old parent folder of the item or folder this event applies
to. OldParentFolderId is only meaningful when EventType is equal to either
EventType.Moved or EventType.Copied. For all other event types,
OldParentFolderId is null.  
[ParentFolderId](P_Tessa_Exchange_WebServices_Data_NotificationEvent_ParentFolderId.htm)|
Gets the Id of the parent folder of the item or folder this event applie to.  
[TimeStamp](P_Tessa_Exchange_WebServices_Data_NotificationEvent_TimeStamp.htm)|
Gets the date and time when the event occurred.  
## __Методы
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
##  __Методы расширения
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
