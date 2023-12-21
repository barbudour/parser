# IServerInitializationExtensionContext - интерфейс
Контекст расширений для инициализации приложений со стороны сервера.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServerInitializationExtensionContext : IInitializationExtensionContext, 
    	IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public Interface IServerInitializationExtensionContext
    	Inherits IInitializationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public interface class IServerInitializationExtensionContext : IInitializationExtensionContext, 
    	IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
F# __Копировать
     type IServerInitializationExtensionContext = 
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
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[ConfigurationInfo](P_Tessa_Platform_Initialization_IServerInitializationExtensionContext_ConfigurationInfo.htm)|
Информация по текущей конфигурации. Автоматически заполняется при выполнении
запроса на инициализацию, перед методом расширений AfterRequest, если равен
null на момент выполнения запроса, т.е. после методов расширений
BeforeRequest.  
[ConfigurationIsCached](P_Tessa_Platform_Initialization_IServerInitializationExtensionContext_ConfigurationIsCached.htm)|
Признак того, что версия конфигурации не изменилась относительно версии,
которая добавлена в локальный кэш на клиенте. Автоматически заполняется при
выполнении запроса на инициализацию, перед методом расширений AfterRequest.
Задаётся синхронно со свойством ConfigurationInfo.  
[DbScope](P_Tessa_Platform_Initialization_IServerInitializationExtensionContext_DbScope.htm)|
Объект, обеспечивающий взаимодействие с базой данных.  
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
##  __Методы расширения
[SetTypeIDListToLoad](M_Tessa_Platform_Initialization_InitializationExtensions_SetTypeIDListToLoad.htm)|
Устанавливает список идентификаторов типов карточек, которые должны
загружаться при инициализации.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
---|---  
[TryGetTypeIDListToLoad](M_Tessa_Platform_Initialization_InitializationExtensions_TryGetTypeIDListToLoad.htm)|
Возвращает список идентификаторов типов карточек, которые должны загружаться
при инициализации, или null, если подходящих типов нет.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
