# ServerInitializationExtensionContext - класс
Контекст расширений для инициализации приложений со стороны сервера.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ServerInitializationExtensionContext : InitializationExtensionContext, 
    	IServerInitializationExtensionContext, IInitializationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public NotInheritable Class ServerInitializationExtensionContext
    	Inherits InitializationExtensionContext
    	Implements IServerInitializationExtensionContext, IInitializationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, 
    	IExtensionContext
C++ __Копировать
     public ref class ServerInitializationExtensionContext sealed : public InitializationExtensionContext, 
    	IServerInitializationExtensionContext, IInitializationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type ServerInitializationExtensionContext = 
        class
            inherit InitializationExtensionContext
            interface IServerInitializationExtensionContext
            interface IInitializationExtensionContext
            interface IApplicationExtensionContextBase
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm) __[InitializationExtensionContext](T_Tessa_Platform_Initialization_InitializationExtensionContext.htm) __ ServerInitializationExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm), [IInitializationExtensionContext](T_Tessa_Platform_Initialization_IInitializationExtensionContext.htm), [IServerInitializationExtensionContext](T_Tessa_Platform_Initialization_IServerInitializationExtensionContext.htm), [IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
##  __Конструкторы
[ServerInitializationExtensionContext](M_Tessa_Platform_Initialization_ServerInitializationExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
---|---  
[CancellationToken](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[ConfigurationInfo](P_Tessa_Platform_Initialization_ServerInitializationExtensionContext_ConfigurationInfo.htm)|
Информация по текущей конфигурации. Автоматически заполняется при выполнении
запроса на инициализацию, перед методом расширений AfterRequest, если равен
null на момент выполнения запроса, т.е. после методов расширений
BeforeRequest.  
[ConfigurationIsCached](P_Tessa_Platform_Initialization_ServerInitializationExtensionContext_ConfigurationIsCached.htm)|
Признак того, что версия конфигурации не изменилась относительно версии,
которая добавлена в локальный кэш на клиенте. Автоматически заполняется при
выполнении запроса на инициализацию, перед методом расширений AfterRequest.
Задаётся синхронно со свойством ConfigurationInfo.  
[DbScope](P_Tessa_Platform_Initialization_ServerInitializationExtensionContext_DbScope.htm)|
Объект, обеспечивающий взаимодействие с базой данных.  
[EnableTracing](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[Info](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[Request](P_Tessa_Platform_Initialization_InitializationExtensionContext_Request.htm)|
Запрос на инициализацию.  
(Унаследован от
[InitializationExtensionContext](T_Tessa_Platform_Initialization_InitializationExtensionContext.htm))  
[RequestIsSuccessful](P_Tessa_Platform_Initialization_InitializationExtensionContext_RequestIsSuccessful.htm)|
Признак того, что запрос был выполнен успешно. Проверять есть смысл в
расширениях AfterRequest.  
(Унаследован от
[InitializationExtensionContext](T_Tessa_Platform_Initialization_InitializationExtensionContext.htm))  
[Response](P_Tessa_Platform_Initialization_InitializationExtensionContext_Response.htm)|
Ответ на запрос на инициализацию. Равен null в расширениях BeforeRequest.
Значение, которое присваивается, не может быть равно null. Если значение
присваивается на клиенте перед запросом на сервер, то запрос не выполняется.  
(Унаследован от
[InitializationExtensionContext](T_Tessa_Platform_Initialization_InitializationExtensionContext.htm))  
[Session](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_Session.htm)|
Сессия текущего пользователя.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[ValidationResult](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
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
[SetTypeIDListToLoad](M_Tessa_Platform_Initialization_InitializationExtensions_SetTypeIDListToLoad.htm)|
Устанавливает список идентификаторов типов карточек, которые должны
загружаться при инициализации.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[TryGetTypeIDListToLoad](M_Tessa_Platform_Initialization_InitializationExtensions_TryGetTypeIDListToLoad.htm)|
Возвращает список идентификаторов типов карточек, которые должны загружаться
при инициализации, или null, если подходящих типов нет.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
