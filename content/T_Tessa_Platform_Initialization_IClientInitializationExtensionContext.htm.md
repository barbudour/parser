# IClientInitializationExtensionContext - интерфейс
Контекст расширений для инициализации приложений со стороны клиента.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IClientInitializationExtensionContext : IInitializationExtensionContext, 
    	IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public Interface IClientInitializationExtensionContext
    	Inherits IInitializationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public interface class IClientInitializationExtensionContext : IInitializationExtensionContext, 
    	IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
F# __Копировать
     type IClientInitializationExtensionContext = 
        interface
            interface IInitializationExtensionContext
            interface IApplicationExtensionContextBase
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm), [IInitializationExtensionContext](T_Tessa_Platform_Initialization_IInitializationExtensionContext.htm), [IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
---|---  
[CachedResponse](P_Tessa_Platform_Initialization_IClientInitializationExtensionContext_CachedResponse.htm)|
Ответ на запрос, полученный из локального кэша приложения, или null, если в
кэше нет доступной информации.  
[CancelInitialization](P_Tessa_Platform_Initialization_IClientInitializationExtensionContext_CancelInitialization.htm)|
Признак того, что дальнейшую инициализацию приложения требуется отменить в
связки с возникновением ошибки, такой как ошибка в прочитанных данных. Если в
результате валидации в контексте отсутствуют ошибки, то в таком случае будет
добавлена стандартная ошибка.  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[ConfigurationIsCached](P_Tessa_Platform_Initialization_IClientInitializationExtensionContext_ConfigurationIsCached.htm)|
Признак того, что версия конфигурации не изменилась относительно версии,
которая добавлена в локальный кэш на клиенте, при этом сервер мог не вернуть
часть метаинформации, которая не изменялась, и её необходимо инициализировать
из кэшированного запроса
[IClientInitializationExtensionContext.CachedResponse]. Автоматически
заполняется при выполнении запроса на инициализацию, перед методом расширений
AfterRequest.  
[Container](P_Tessa_Platform_Initialization_IClientInitializationExtensionContext_Container.htm)|
Объект, содержащий информацию, заполняемую при инициализации приложения.  
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
(Унаследован от
[IInitializationExtensionContext](T_Tessa_Platform_Initialization_IInitializationExtensionContext.htm))  
[RequestIsSuccessful](P_Tessa_Platform_Initialization_IInitializationExtensionContext_RequestIsSuccessful.htm)|
Признак того, что запрос был выполнен успешно. Проверять есть смысл в
расширениях AfterRequest.  
(Унаследован от
[IInitializationExtensionContext](T_Tessa_Platform_Initialization_IInitializationExtensionContext.htm))  
[Response](P_Tessa_Platform_Initialization_IInitializationExtensionContext_Response.htm)|
Ответ на запрос на инициализацию. Равен null в расширениях BeforeRequest.
Значение, которое присваивается, не может быть равно null. Если значение
присваивается на клиенте перед запросом на сервер, то запрос не выполняется.  
(Унаследован от
[IInitializationExtensionContext](T_Tessa_Platform_Initialization_IInitializationExtensionContext.htm))  
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
