# ApplicationUIInstance - класс
Приложение Tessa с графическим интерфейсом.
## __Definition
 **Пространство имён:** [Tessa.UI.Runtime](N_Tessa_UI_Runtime.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class ApplicationUIInstance : ApplicationInstance
VB __Копировать
     Public Class ApplicationUIInstance
    	Inherits ApplicationInstance
C++ __Копировать
     public ref class ApplicationUIInstance : public ApplicationInstance
F# __Копировать
     type ApplicationUIInstance = 
        class
            inherit ApplicationInstance
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm) __ ApplicationUIInstance
##  __Заметки
Наследники класса могут переопределять методы, связанные с событиями запуска и
завершения приложения.
## __Конструкторы
[ApplicationUIInstance](M_Tessa_UI_Runtime_ApplicationUIInstance__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[Context](P_Tessa_Platform_Runtime_ApplicationInstance_Context.htm)|  Контекст
запускаемого или запущенного приложения, или null, если приложение не
запущено.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
---|---  
[DefaultThemeName](P_Tessa_UI_Runtime_ApplicationUIInstance_DefaultThemeName.htm)|
Имя темы оформления по умолчанию, которая используется вместо сохранённой, или
null, если используется сохранённая тема или тема по умолчанию.  
[Dependencies](P_Tessa_Platform_Runtime_ApplicationInstance_Dependencies.htm)|
Основные зависимости для создаваемого объекта.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[IsDisposed](P_Tessa_Platform_Runtime_ApplicationInstance_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[IsLaunched](P_Tessa_Platform_Runtime_ApplicationInstance_IsLaunched.htm)|
Признак того, что приложение успешно запущено.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
##  __Методы
[CheckDisposed](M_Tessa_Platform_Runtime_ApplicationInstance_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
---|---  
[DisposeAsync()](M_Tessa_Platform_Runtime_ApplicationInstance_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_Runtime_ApplicationInstance_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
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
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[InitializeDefaultLocalizationAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_InitializeDefaultLocalizationAsync.htm)|
Инициализирует локализацию по умолчанию, т.е. до того, как настройки
локализации будут загружены. В качестве культуры по умолчанию используется
язык системы.  
[InitializeLocalizationServiceAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_InitializeLocalizationServiceAsync.htm)|
Инициализирует сервис локализации после того, как настройки локализации будут
загружены.  
[LaunchAsync](M_Tessa_Platform_Runtime_ApplicationInstance_LaunchAsync.htm)|
Выполняет обработку, связанную с запуском приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnConnectionSettingsInitializedAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_OnConnectionSettingsInitializedAsync.htm)|
Асинхронно выполняется после инициализации настроек подключения к базе данных.  
(Переопределяет
[ApplicationInstance.OnConnectionSettingsInitializedAsync(ApplicationContextDeferredEventArgs,
CancellationToken)](M_Tessa_Platform_Runtime_ApplicationInstance_OnConnectionSettingsInitializedAsync.htm))  
[OnExecutingCommand](M_Tessa_Platform_Runtime_ApplicationInstance_OnExecutingCommand.htm)|
Выполняется при выполнении команды, полученной по параметру командной строки.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[OnInitializedAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_OnInitializedAsync.htm)|
Асинхронно выполняется после успешной инициализации приложения.  
(Переопределяет
[ApplicationInstance.OnInitializedAsync(ApplicationContextDeferredEventArgs,
CancellationToken)](M_Tessa_Platform_Runtime_ApplicationInstance_OnInitializedAsync.htm))  
[OnInitializeExtensionsExecuted](M_Tessa_UI_Runtime_ApplicationUIInstance_OnInitializeExtensionsExecuted.htm)|
Метод вызывается после выполнения расширений на инициализацию приложения
IApplicationExtension.Initialize.  
(Переопределяет
[ApplicationInstance.OnInitializeExtensionsExecuted(IApplicationExtensionContext,
Boolean)](M_Tessa_Platform_Runtime_ApplicationInstance_OnInitializeExtensionsExecuted.htm))  
[OnLaunchedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnLaunchedAsync.htm)|
Асинхронно выполняется после успешного запуска приложения (в обычном режиме).  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[OnLaunchingAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_OnLaunchingAsync.htm)|
Асинхронно выполняется перед запуском приложения.  
(Переопределяет
[ApplicationInstance.OnLaunchingAsync(ApplicationContextDeferredEventArgs,
CancellationToken)](M_Tessa_Platform_Runtime_ApplicationInstance_OnLaunchingAsync.htm))  
[OnParsingCommand](M_Tessa_Platform_Runtime_ApplicationInstance_OnParsingCommand.htm)|
Выполняется при разборе параметра командной строки.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[OnPublishedAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_OnPublishedAsync.htm)|
Асинхронно выполняется после успешного запуска приложения в режиме публикации.  
(Переопределяет
[ApplicationInstance.OnPublishedAsync(ApplicationContextDeferredEventArgs,
CancellationToken)](M_Tessa_Platform_Runtime_ApplicationInstance_OnPublishedAsync.htm))  
[OnSessionOpenedAsync](M_Tessa_UI_Runtime_ApplicationUIInstance_OnSessionOpenedAsync.htm)|
Асинхронно выполняется после открытия сессии при запуске приложения.  
(Переопределяет
[ApplicationInstance.OnSessionOpenedAsync(ApplicationContextDeferredEventArgs,
CancellationToken)](M_Tessa_Platform_Runtime_ApplicationInstance_OnSessionOpenedAsync.htm))  
[OnShutdownCompletedAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnShutdownCompletedAsync.htm)|
Асинхронно выполняется после завершения приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[OnShutdownExtensionsExecuted](M_Tessa_Platform_Runtime_ApplicationInstance_OnShutdownExtensionsExecuted.htm)|
Метод вызывается после выполнения расширений на завершение приложения
IApplicationExtension.Shutdown.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[OnShuttingDownAsync](M_Tessa_Platform_Runtime_ApplicationInstance_OnShuttingDownAsync.htm)|
Асинхронно выполняется перед завершением приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[ShutdownAsync](M_Tessa_Platform_Runtime_ApplicationInstance_ShutdownAsync.htm)|
Завершает работу приложения, если оно было запущено. Если приложение не было
запущено, то не выполняет действий.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[ConnectionSettingsInitialized](E_Tessa_Platform_Runtime_ApplicationInstance_ConnectionSettingsInitialized.htm)|
Событие, выполняемое после инициализации настроек подключения к базе данных.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
---|---  
[ExecutingCommand](E_Tessa_Platform_Runtime_ApplicationInstance_ExecutingCommand.htm)|
Выполняется при выполнении команды, полученной по параметру командной строки.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[Initialized](E_Tessa_Platform_Runtime_ApplicationInstance_Initialized.htm)|
Событие, выполняемое после успешной инициализации приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[Launched](E_Tessa_Platform_Runtime_ApplicationInstance_Launched.htm)|
Событие, выполняемое после успешного запуска приложения (в обычном режиме).  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[Launching](E_Tessa_Platform_Runtime_ApplicationInstance_Launching.htm)|
Событие, выполняемое перед запуском приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[ParsingCommand](E_Tessa_Platform_Runtime_ApplicationInstance_ParsingCommand.htm)|
Выполняется при разборе параметра командной строки.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[Published](E_Tessa_Platform_Runtime_ApplicationInstance_Published.htm)|
Событие, выполняемое после успешного запуска приложения в режиме публикации.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[SessionOpened](E_Tessa_Platform_Runtime_ApplicationInstance_SessionOpened.htm)|
Событие, выполняемое после открытия сессии при запуске приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[ShutdownCompleted](E_Tessa_Platform_Runtime_ApplicationInstance_ShutdownCompleted.htm)|
Событие, выполняемое после завершения приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
[ShuttingDown](E_Tessa_Platform_Runtime_ApplicationInstance_ShuttingDown.htm)|
Событие, выполняемое перед завершением приложения.  
(Унаследован от
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm))  
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
[Tessa.UI.Runtime - пространство имён](N_Tessa_UI_Runtime.htm)
