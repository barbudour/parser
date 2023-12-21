# IApplicationLaunchParameters - интерфейс
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
указаны при запуске.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationLaunchParameters
VB __Копировать
     Public Interface IApplicationLaunchParameters
C++ __Копировать
     public interface class IApplicationLaunchParameters
F# __Копировать
     type IApplicationLaunchParameters = interface end
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_ApplicationID.htm)|
Идентификатор приложения для расширений.  
---|---  
[CommandLineArgs](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_CommandLineArgs.htm)|
Параметры командной строки.  
[Info](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_Info.htm)|
Дополнительная информация, связанная с запуском приложения.  
[SkipApplicationExtensions](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_SkipApplicationExtensions.htm)|
Признак того, что при инициализации и при завершении приложения не будут
выполнены соответствующие клиентские расширения. По умолчанию равен false.  
[SkipApplicationInitialization](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_SkipApplicationInitialization.htm)|
Признак того, что при инициализации приложения не будет инициализированы
стандартные данные приложения запросом к серверу. По умолчанию равен false.  
[SkipFilesInitialization](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_SkipFilesInitialization.htm)|
Признак того, что при инициализации приложения не будет инициализирована
подсистема файлов. При этом не будет, например, выполнено удаление временных
файлов, оставшихся с предыдущих запусков. По умолчанию равен false.  
[Splash](P_Tessa_Platform_Runtime_IApplicationLaunchParameters_Splash.htm)|
Сплэш-окно загрузки приложения, отображаемое в процессе его инициализации, или
null, если такое окно не отображается.  
## __Методы
[ActivateShellAsync](M_Tessa_Platform_Runtime_IApplicationLaunchParameters_ActivateShellAsync.htm)|
Активирует главное окно приложения, если такое окно существует.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
