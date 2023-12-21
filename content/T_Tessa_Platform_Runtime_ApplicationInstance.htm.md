# ApplicationInstance - класс
Приложение Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ApplicationInstance : IApplication, 
    	IAsyncDisposable
VB __Копировать
     Public Class ApplicationInstance
    	Implements IApplication, IAsyncDisposable
C++ __Копировать
     public ref class ApplicationInstance : IApplication, 
    	IAsyncDisposable
F# __Копировать
     type ApplicationInstance = 
        class
            interface IApplication
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationInstance
Derived
[Tessa.UI.Runtime.ApplicationUIInstance](T_Tessa_UI_Runtime_ApplicationUIInstance.htm)
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IApplication](T_Tessa_Platform_Runtime_IApplication.htm)
##  __Заметки
Наследники класса могут переопределять методы, связанные с событиями запуска и
завершения приложения.
## __Конструкторы
[ApplicationInstance](M_Tessa_Platform_Runtime_ApplicationInstance__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[Context](P_Tessa_Platform_Runtime_ApplicationInstance_Context.htm)|  Контекст
запускаемого или запущенного приложения, или null, если приложение не
запущено.  
---|---  
[Dependencies](P_Tessa_Platform_Runtime_ApplicationInstance_Dependencies.htm)|
Основные зависимости для создаваемого объекта.  
[IsDisposed](P_Tessa_Platform_Runtime_ApplicationInstance_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
[IsLaunched](P_Tessa_Platform_Runtime_ApplicationInstance_IsLaunched.htm)|
Признак того, что приложение успешно запущено.  
##  __Методы
[CheckDisposed](M_Tessa_Platform_Runtime_ApplicationInstance_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
---|---  
[DisposeAsync()](M_Tessa_Platform_Runtime_ApplicationInstance_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[DisposeAsync(Boolean)](M_Tessa_Platform_Runtime_ApplicationInstance_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[HandleLinksAsync](M_Tessa_Platform_Runtime_ApplicationInstance_HandleLinksAsync.htm)|
Обрабатывает ссылки, переданные приложению при запуске. Если приложение не
было запущено или переданные ссылки отсутствуют, то не выполняет действий.  
[LaunchAsync](M_Tessa_Platform_Runtime_ApplicationInstance_LaunchAsync.htm)|
Выполняет обработку, связанную с запуском приложения.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnConnectionSettingsInitializedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnConnectionSettingsInitializedAsync.htm)|
Асинхронно выполняется после инициализации настроек подключения к базе данных.  
[OnExecutingCommand](M_Tessa_Platform_Runtime_ApplicationInstance_OnExecutingCommand.htm)|
Выполняется при выполнении команды, полученной по параметру командной строки.  
[OnInitializedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnInitializedAsync.htm)|
Асинхронно выполняется после успешной инициализации приложения.  
[OnInitializeExtensionsExecuted](M_Tessa_Platform_Runtime_ApplicationInstance_OnInitializeExtensionsExecuted.htm)|
Метод вызывается после выполнения расширений на инициализацию приложения
IApplicationExtension.Initialize.  
[OnLaunchedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnLaunchedAsync.htm)|
Асинхронно выполняется после успешного запуска приложения (в обычном режиме).  
[OnLaunchingAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnLaunchingAsync.htm)|
Асинхронно выполняется перед запуском приложения.  
[OnParsingCommand](M_Tessa_Platform_Runtime_ApplicationInstance_OnParsingCommand.htm)|
Выполняется при разборе параметра командной строки.  
[OnPublishedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnPublishedAsync.htm)|
Асинхронно выполняется после успешного запуска приложения в режиме публикации.  
[OnSessionOpenedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnSessionOpenedAsync.htm)|
Асинхронно выполняется после открытия сессии при запуске приложения.  
[OnShutdownCompletedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnShutdownCompletedAsync.htm)|
Асинхронно выполняется после завершения приложения.  
[OnShutdownExtensionsExecuted](M_Tessa_Platform_Runtime_ApplicationInstance_OnShutdownExtensionsExecuted.htm)|
Метод вызывается после выполнения расширений на завершение приложения
IApplicationExtension.Shutdown.  
[OnShuttingDownAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnShuttingDownAsync.htm)|
Асинхронно выполняется перед завершением приложения.  
[ShutdownAsync](M_Tessa_Platform_Runtime_ApplicationInstance_ShutdownAsync.htm)|
Завершает работу приложения, если оно было запущено. Если приложение не было
запущено, то не выполняет действий.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[ConnectionSettingsInitialized](E_Tessa_Platform_Runtime_ApplicationInstance_ConnectionSettingsInitialized.htm)|
Событие, выполняемое после инициализации настроек подключения к базе данных.  
---|---  
[ExecutingCommand](E_Tessa_Platform_Runtime_ApplicationInstance_ExecutingCommand.htm)|
Выполняется при выполнении команды, полученной по параметру командной строки.  
[Initialized](E_Tessa_Platform_Runtime_ApplicationInstance_Initialized.htm)|
Событие, выполняемое после успешной инициализации приложения.  
[Launched](E_Tessa_Platform_Runtime_ApplicationInstance_Launched.htm)|
Событие, выполняемое после успешного запуска приложения (в обычном режиме).  
[Launching](E_Tessa_Platform_Runtime_ApplicationInstance_Launching.htm)|
Событие, выполняемое перед запуском приложения.  
[ParsingCommand](E_Tessa_Platform_Runtime_ApplicationInstance_ParsingCommand.htm)|
Выполняется при разборе параметра командной строки.  
[Published](E_Tessa_Platform_Runtime_ApplicationInstance_Published.htm)|
Событие, выполняемое после успешного запуска приложения в режиме публикации.  
[SessionOpened](E_Tessa_Platform_Runtime_ApplicationInstance_SessionOpened.htm)|
Событие, выполняемое после открытия сессии при запуске приложения.  
[ShutdownCompleted](E_Tessa_Platform_Runtime_ApplicationInstance_ShutdownCompleted.htm)|
Событие, выполняемое после завершения приложения.  
[ShuttingDown](E_Tessa_Platform_Runtime_ApplicationInstance_ShuttingDown.htm)|
Событие, выполняемое перед завершением приложения.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
