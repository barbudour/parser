# NotificationRecipientsSource - класс
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая получает список получателей по списку идентификаторов ролей.
Обрабатывает тип параметров
[IDNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_IDNotificationRecipientsSourceParameter.htm).
Учитывает настройки заместителей в
[INotificationSendContext](T_Tessa_Notices_INotificationSendContext.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices.Sources](N_Tessa_Notices_Sources.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NotificationRecipientsSource : INotificationRecipientsSource
VB __Копировать
     Public Class NotificationRecipientsSource
    	Implements INotificationRecipientsSource
C++ __Копировать
     public ref class NotificationRecipientsSource : INotificationRecipientsSource
F# __Копировать
     type NotificationRecipientsSource = 
        class
            interface INotificationRecipientsSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationRecipientsSource
Derived
[Tessa.Notices.Sources.RoleNameNotificationRecipientsSource](T_Tessa_Notices_Sources_RoleNameNotificationRecipientsSource.htm)
Implements
    [INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm)
##  __Конструкторы
[NotificationRecipientsSource](M_Tessa_Notices_Sources_NotificationRecipientsSource__ctor.htm)|
Инициализирует новый экземпляр класса NotificationRecipientsSource  
---|---  
##  __Свойства
[RoleAggregator](P_Tessa_Notices_Sources_NotificationRecipientsSource_RoleAggregator.htm)|
Аггрегатор ролей для формирования списка получателей.  
---|---  
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
[GetRecipientsAsync](M_Tessa_Notices_Sources_NotificationRecipientsSource_GetRecipientsAsync.htm)|
Возвращает список получателей уведомления.  
[GetRoleIDsAsync](M_Tessa_Notices_Sources_NotificationRecipientsSource_GetRoleIDsAsync.htm)|
Метод для получения списка идентификаторов ролей - получателей уведомления.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsOptional](M_Tessa_Notices_Sources_NotificationRecipientsSource_IsOptional.htm)|
Метод для определения, являются ли получатели необязательными.  
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
[Tessa.Notices.Sources - пространство имён](N_Tessa_Notices_Sources.htm)
