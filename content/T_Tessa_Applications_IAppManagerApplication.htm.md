# IAppManagerApplication - интерфейс
Описание интерфейса первого экземпляра приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAppManagerApplication : IApplication, 
    	IAsyncDisposable
VB __Копировать
     Public Interface IAppManagerApplication
    	Inherits IApplication, IAsyncDisposable
C++ __Копировать
     public interface class IAppManagerApplication : IApplication, 
    	IAsyncDisposable
F# __Копировать
     type IAppManagerApplication = 
        interface
            interface IApplication
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IApplication](T_Tessa_Platform_Runtime_IApplication.htm)
##  __Свойства
[Context](P_Tessa_Platform_Runtime_IApplication_Context.htm)|  Контекст
запускаемого или запущенного приложения, или null, если приложение не
запущено.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
---|---  
[IsLaunched](P_Tessa_Platform_Runtime_IApplication_IsLaunched.htm)| Признак
того, что приложение успешно запущено.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[LauncherPath](P_Tessa_Applications_IAppManagerApplication_LauncherPath.htm)|
Gets Путь к лаунчеру  
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[HandleLinksAsync](M_Tessa_Platform_Runtime_IApplication_HandleLinksAsync.htm)|
Обрабатывает ссылки, переданные приложению при запуске. Если приложение не
было запущено или переданные ссылки отсутствуют, то не выполняет действий.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[IsFirstInstanceAsync](M_Tessa_Applications_IAppManagerApplication_IsFirstInstanceAsync.htm)|
Gets a value indicating whether Признак запуска первого экземпляра приложения  
[LaunchAsync](M_Tessa_Platform_Runtime_IApplication_LaunchAsync.htm)|
Выполняет обработку, связанную с запуском приложения.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[ShutdownAsync](M_Tessa_Platform_Runtime_IApplication_ShutdownAsync.htm)|
Завершает работу приложения, если оно было запущено. Если приложение не было
запущено, то не выполняет действий.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
##  __События
[ConnectionSettingsInitialized](E_Tessa_Platform_Runtime_IApplication_ConnectionSettingsInitialized.htm)|
Событие, выполняемое после инициализации настроек подключения к базе данных.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
---|---  
[ExecutingCommand](E_Tessa_Platform_Runtime_IApplication_ExecutingCommand.htm)|
Выполняется при выполнении команды, полученной по параметру командной строки.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[Initialized](E_Tessa_Platform_Runtime_IApplication_Initialized.htm)| Событие,
выполняемое после успешной инициализации приложения.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[Launched](E_Tessa_Platform_Runtime_IApplication_Launched.htm)| Событие,
выполняемое после успешного запуска приложения (в обычном режиме).  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[Launching](E_Tessa_Platform_Runtime_IApplication_Launching.htm)| Событие,
выполняемое перед запуском приложения.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[ParsingCommand](E_Tessa_Platform_Runtime_IApplication_ParsingCommand.htm)|
Выполняется при разборе параметра командной строки.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[Published](E_Tessa_Platform_Runtime_IApplication_Published.htm)| Событие,
выполняемое после успешного запуска приложения в режиме публикации.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[SessionOpened](E_Tessa_Platform_Runtime_IApplication_SessionOpened.htm)|
Событие, выполняемое после открытия сессии при запуске приложения.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[ShutdownCompleted](E_Tessa_Platform_Runtime_IApplication_ShutdownCompleted.htm)|
Событие, выполняемое после завершения приложения.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
[ShuttingDown](E_Tessa_Platform_Runtime_IApplication_ShuttingDown.htm)|
Событие, выполняемое перед завершением приложения.  
(Унаследован от [IApplication](T_Tessa_Platform_Runtime_IApplication.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
