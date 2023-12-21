# IInitializationExtensionContext - интерфейс
Контекст расширений для инициализации приложений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IInitializationExtensionContext : IApplicationExtensionContextBase, 
    	ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public Interface IInitializationExtensionContext
    	Inherits IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public interface class IInitializationExtensionContext : IApplicationExtensionContextBase, 
    	ITraceableExtensionContext, IExtensionContext
F# __Копировать
     type IInitializationExtensionContext = 
        interface
            interface IApplicationExtensionContextBase
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm), [IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
---|---  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
[Info](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
[Request](P_Tessa_Platform_Initialization_IInitializationExtensionContext_Request.htm)|
Запрос на инициализацию.  
[RequestIsSuccessful](P_Tessa_Platform_Initialization_IInitializationExtensionContext_RequestIsSuccessful.htm)|
Признак того, что запрос был выполнен успешно. Проверять есть смысл в
расширениях AfterRequest.  
[Response](P_Tessa_Platform_Initialization_IInitializationExtensionContext_Response.htm)|
Ответ на запрос на инициализацию. Равен null в расширениях BeforeRequest.
Значение, которое присваивается, не может быть равно null. Если значение
присваивается на клиенте перед запросом на сервер, то запрос не выполняется.  
[Session](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_Session.htm)|
Сессия текущего пользователя.  
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
