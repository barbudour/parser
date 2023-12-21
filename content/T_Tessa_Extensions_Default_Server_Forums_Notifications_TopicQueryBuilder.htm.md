# TopicQueryBuilder - класс
Выполняет построение запроса для получения списка уведомлений по топикам.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Forums.Notifications](N_Tessa_Extensions_Default_Server_Forums_Notifications.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class TopicQueryBuilder : ITopicQueryBuilder
VB __Копировать
     Public Class TopicQueryBuilder
    	Implements ITopicQueryBuilder
C++ __Копировать
     public ref class TopicQueryBuilder : ITopicQueryBuilder
F# __Копировать
     type TopicQueryBuilder = 
        class
            interface ITopicQueryBuilder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TopicQueryBuilder
Implements
    [ITopicQueryBuilder](T_Tessa_Forums_Notifications_ITopicQueryBuilder.htm)
##  __Конструкторы
[TopicQueryBuilder](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder__ctor.htm)|
Инциализирует новый экземпляр класса.  
---|---  
## __Свойства
[QueryBuilder](P_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_QueryBuilder.htm)|
Объект, выполняющий построение SQL-запроса.  
---|---  
## __Методы
[Append](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_Append.htm)|
Добавляет пользовательскую часть в запрос.  
---|---  
[AppendJoins](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_AppendJoins.htm)|
Добавляет базовые джойны к запросу.  
[AppendJoinTopicsAndUsers](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_AppendJoinTopicsAndUsers.htm)|
Добавляет базовый Inner Join Lateral в запрос для получения списка пар
идентификаторов топика и сотрудника.  
[AppendOrderBy](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_AppendOrderBy.htm)|
Добавляет базовую сортировку к запросу.  
[AppendSelect](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_AppendSelect.htm)|
Добавляет в запрос базовые колонки.  
[AppendWhere](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_AppendWhere.htm)|
Добавляет базовые условия в запрос.  
[Build](M_Tessa_Extensions_Default_Server_Forums_Notifications_TopicQueryBuilder_Build.htm)|
Возвращает результат построение запроса.  
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
[Tessa.Extensions.Default.Server.Forums.Notifications - пространство
имён](N_Tessa_Extensions_Default_Server_Forums_Notifications.htm)
