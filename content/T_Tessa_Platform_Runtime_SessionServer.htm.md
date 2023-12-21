# SessionServer - класс
Объект, обеспечивающий взаимодействие с сессиями на сервере.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionServer : ISessionServer
VB __Копировать
     Public NotInheritable Class SessionServer
    	Implements ISessionServer
C++ __Копировать
     public ref class SessionServer sealed : ISessionServer
F# __Копировать
     [<SealedAttribute>]
    type SessionServer = 
        class
            interface ISessionServer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionServer
Implements
    [ISessionServer](T_Tessa_Platform_Runtime_ISessionServer.htm)
##  __Конструкторы
[SessionServer](M_Tessa_Platform_Runtime_SessionServer__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[AddSessionAsync](M_Tessa_Platform_Runtime_SessionServer_AddSessionAsync.htm)|
Добавляет информацию по сессии (обычно в базу данных). Сессия автоматически
добавляется в методе открытия сессии.  
---|---  
[ApplyTokenParameters](M_Tessa_Platform_Runtime_SessionServer_ApplyTokenParameters.htm)|
Устанавливает параметры текущего потока для сессии по заданному токену.  
[CloseSessionAsync](M_Tessa_Platform_Runtime_SessionServer_CloseSessionAsync.htm)|
Закрывает сессию с заданным идентификатором. Закрытие сессии удаляет её, а
также может дополнительно добавить запись в логах аудита или выполнить другие
действия. Возвращает признак того, что сессия ещё была открыта на момент
вызова метода.  
[DeleteUserSessionsAsync](M_Tessa_Platform_Runtime_SessionServer_DeleteUserSessionsAsync.htm)|
Удаляет все сессии заданного сотрудника.  
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
[OpenSessionAsync](M_Tessa_Platform_Runtime_SessionServer_OpenSessionAsync.htm)|
Открывает сессию по заданным параметрам. Возвращает токен для открытой сессии.  
[RemoveSessionAsync](M_Tessa_Platform_Runtime_SessionServer_RemoveSessionAsync.htm)|
Удаляет сессию с заданным идентификатором. Возвращает признак того, что сессия
ещё была открыта на момент вызова метода.  
[SetSessionIsActiveAsync](M_Tessa_Platform_Runtime_SessionServer_SetSessionIsActiveAsync.htm)|
Устанавливает признак активности сессии. Возвращает true, если признак
активности был изменён для существующей сессии.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetSessionAsync](M_Tessa_Platform_Runtime_SessionServer_TryGetSessionAsync.htm)|
Загружает информацию по сессии для заданного идентификатора сессии. Возвращает
null, если сессия не найдена.  
[TryGetSessionIDToDeactivateAsync](M_Tessa_Platform_Runtime_SessionServer_TryGetSessionIDToDeactivateAsync.htm)|
Возвращает идентификатор сессии, которую можно деактивировать, чтобы получить
лицензию (обычно конкурентную), или null, если такая сессия отсутствует.  
[UpdateLastActivityAsync](M_Tessa_Platform_Runtime_SessionServer_UpdateLastActivityAsync.htm)|
Обновляет дату последней активности для сессии. Рекомендуется периодически
вызывать метод, чтобы сессия не была удалена автоматически при отсутствии
другой активности. Возвращает признак того, что сессия была открыта на момент
вызова метода.  
[ValidateAndGetSessionAsync](M_Tessa_Platform_Runtime_SessionServer_ValidateAndGetSessionAsync.htm)|
Проверяет всю информацию по сессии, которая может быть получена со стороны
клиента. Возвращает объект сессии (отличный от null) со всей актуальной
информацией. Для сессии также обновляет дату последней активности. В случае
ошибок (в т.ч. при отсутствии сессии, добавленной в системе) выбрасывается
исключение [Tessa.Platform.Runtime.SessionException].  
[ValidateBasicFields](M_Tessa_Platform_Runtime_SessionServer_ValidateBasicFields.htm)|
Проверяет основную информацию по сессии, которая может быть получена со
стороны клиента. В случае ошибок выбрасывается исключение
[Tessa.Platform.Runtime.SessionException].  
## __Поля
[ActionHistoryHostIPKey](F_Tessa_Platform_Runtime_SessionServer_ActionHistoryHostIPKey.htm)|  
---|---  
[ActionHistoryHostNameKey](F_Tessa_Platform_Runtime_SessionServer_ActionHistoryHostNameKey.htm)|  
[ActionHistoryMessageKey](F_Tessa_Platform_Runtime_SessionServer_ActionHistoryMessageKey.htm)|  
[ActionHistorySessionKey](F_Tessa_Platform_Runtime_SessionServer_ActionHistorySessionKey.htm)|  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
