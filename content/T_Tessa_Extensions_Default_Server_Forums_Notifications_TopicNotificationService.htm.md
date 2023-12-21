# TopicNotificationService - класс
Сервис для получения списка почтовых уведомлений по топикам.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Forums.Notifications](N_Tessa_Extensions_Default_Server_Forums_Notifications.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class TopicNotificationService : TopicNotificationServiceBase
VB __Копировать
     Public Class TopicNotificationService
    	Inherits TopicNotificationServiceBase
C++ __Копировать
     public ref class TopicNotificationService : public TopicNotificationServiceBase
F# __Копировать
     type TopicNotificationService = 
        class
            inherit TopicNotificationServiceBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[TopicNotificationServiceBase](T_Tessa_Forums_Notifications_TopicNotificationServiceBase.htm) __ TopicNotificationService
##  __Конструкторы
[TopicNotificationService](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicNotificationService__ctor.htm)|
Сервис для получения списка почтовых уведомлений по топикам.  
---|---  
## __Свойства
[CreateTopicQueryBuilderFunc](P_Tessa_Forums_Notifications_TopicNotificationServiceBase_CreateTopicQueryBuilderFunc.htm)|
Функция, инициализирующая новый экземпляр класса
[ITopicQueryBuilder](T_Tessa_Forums_Notifications_ITopicQueryBuilder.htm).  
(Унаследован от
[TopicNotificationServiceBase](T_Tessa_Forums_Notifications_TopicNotificationServiceBase.htm))  
---|---  
[DbScope](P_Tessa_Forums_Notifications_TopicNotificationServiceBase_DbScope.htm)|
Объект для взаимодействия с базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
(Унаследован от
[TopicNotificationServiceBase](T_Tessa_Forums_Notifications_TopicNotificationServiceBase.htm))  
##  __Методы
[BuildQuery](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicNotificationService_BuildQuery.htm)|
Возвращает запрос для получения списка уведомлений.  
(Переопределяет
[TopicNotificationServiceBase.BuildQuery()](M_Tessa_Forums_Notifications_TopicNotificationServiceBase_BuildQuery.htm))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDefaultUtcOffsetAsync](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicNotificationService_GetDefaultUtcOffsetAsync.htm)|
Получает дефолтное смещение времени в минутах.  
(Переопределяет
[TopicNotificationServiceBase.GetDefaultUtcOffsetAsync(CancellationToken)](M_Tessa_Forums_Notifications_TopicNotificationServiceBase_GetDefaultUtcOffsetAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNormalizedWebAddressAsync](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicNotificationService_GetNormalizedWebAddressAsync.htm)|
Получает нормализованный адресс веб-клиента из карточки настроек сервера.  
(Переопределяет
[TopicNotificationServiceBase.GetNormalizedWebAddressAsync(CancellationToken)](M_Tessa_Forums_Notifications_TopicNotificationServiceBase_GetNormalizedWebAddressAsync.htm))  
[GetNotificationsInfoAsync](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicNotificationService_GetNotificationsInfoAsync.htm)|
Получает список почтовых уведомлений по топикам.  
(Переопределяет
[TopicNotificationServiceBase.GetNotificationsInfoAsync(DateTime, DateTime,
CancellationToken)](M_Tessa_Forums_Notifications_TopicNotificationServiceBase_GetNotificationsInfoAsync.htm))  
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
[Tessa.Extensions.Default.Server.Forums.Notifications - пространство
имён](N_Tessa_Extensions_Default_Server_Forums_Notifications.htm)
