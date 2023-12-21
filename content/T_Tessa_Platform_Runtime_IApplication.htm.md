# IApplication - интерфейс
Приложение Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplication : IAsyncDisposable
VB __Копировать
     Public Interface IApplication
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IApplication : IAsyncDisposable
F# __Копировать
     type IApplication = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[Context](P_Tessa_Platform_Runtime_IApplication_Context.htm)|  Контекст
запускаемого или запущенного приложения, или null, если приложение не
запущено.  
---|---  
[IsLaunched](P_Tessa_Platform_Runtime_IApplication_IsLaunched.htm)| Признак
того, что приложение успешно запущено.  
##  __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[HandleLinksAsync](M_Tessa_Platform_Runtime_IApplication_HandleLinksAsync.htm)|
Обрабатывает ссылки, переданные приложению при запуске. Если приложение не
было запущено или переданные ссылки отсутствуют, то не выполняет действий.  
[LaunchAsync](M_Tessa_Platform_Runtime_IApplication_LaunchAsync.htm)|
Выполняет обработку, связанную с запуском приложения.  
[ShutdownAsync](M_Tessa_Platform_Runtime_IApplication_ShutdownAsync.htm)|
Завершает работу приложения, если оно было запущено. Если приложение не было
запущено, то не выполняет действий.  
## __События
[ConnectionSettingsInitialized](E_Tessa_Platform_Runtime_IApplication_ConnectionSettingsInitialized.htm)|
Событие, выполняемое после инициализации настроек подключения к базе данных.  
---|---  
[ExecutingCommand](E_Tessa_Platform_Runtime_IApplication_ExecutingCommand.htm)|
Выполняется при выполнении команды, полученной по параметру командной строки.  
[Initialized](E_Tessa_Platform_Runtime_IApplication_Initialized.htm)| Событие,
выполняемое после успешной инициализации приложения.  
[Launched](E_Tessa_Platform_Runtime_IApplication_Launched.htm)| Событие,
выполняемое после успешного запуска приложения (в обычном режиме).  
[Launching](E_Tessa_Platform_Runtime_IApplication_Launching.htm)| Событие,
выполняемое перед запуском приложения.  
[ParsingCommand](E_Tessa_Platform_Runtime_IApplication_ParsingCommand.htm)|
Выполняется при разборе параметра командной строки.  
[Published](E_Tessa_Platform_Runtime_IApplication_Published.htm)| Событие,
выполняемое после успешного запуска приложения в режиме публикации.  
[SessionOpened](E_Tessa_Platform_Runtime_IApplication_SessionOpened.htm)|
Событие, выполняемое после открытия сессии при запуске приложения.  
[ShutdownCompleted](E_Tessa_Platform_Runtime_IApplication_ShutdownCompleted.htm)|
Событие, выполняемое после завершения приложения.  
[ShuttingDown](E_Tessa_Platform_Runtime_IApplication_ShuttingDown.htm)|
Событие, выполняемое перед завершением приложения.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
