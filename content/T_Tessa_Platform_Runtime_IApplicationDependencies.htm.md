# IApplicationDependencies - интерфейс
Основные зависимости для объекта
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationDependencies : IDisposable
VB __Копировать
     Public Interface IApplicationDependencies
    	Inherits IDisposable
C++ __Копировать
     public interface class IApplicationDependencies : IDisposable
F# __Копировать
     type IApplicationDependencies = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[ApplicationDescriptor](P_Tessa_Platform_Runtime_IApplicationDependencies_ApplicationDescriptor.htm)|
Объект описывающий текущее приложение, которое определяется по клиентской
сессии.  
---|---  
[ApplicationInitializer](P_Tessa_Platform_Runtime_IApplicationDependencies_ApplicationInitializer.htm)|
Объект, выполняющий инициализацию приложения заданного типа.  
[ApplicationPublisher](P_Tessa_Platform_Runtime_IApplicationDependencies_ApplicationPublisher.htm)|
Объект, выполняющий публикацию приложения.  
[CommandExecutor](P_Tessa_Platform_Runtime_IApplicationDependencies_CommandExecutor.htm)|
Объект, выполняющий команды при запуске приложения.  
[CommandParser](P_Tessa_Platform_Runtime_IApplicationDependencies_CommandParser.htm)|
Объект, выполняющая разбор аргументов командной строки.  
[ConnectionSettings](P_Tessa_Platform_Runtime_IApplicationDependencies_ConnectionSettings.htm)|
Настройки для подключения к сервисам Tessa.  
[EnvironmentManager](P_Tessa_Platform_Runtime_IApplicationDependencies_EnvironmentManager.htm)|
Объект, управляющий переменными приложения.  
[ExtensionContainer](P_Tessa_Platform_Runtime_IApplicationDependencies_ExtensionContainer.htm)|
Контейнер расширений.  
[LinkManager](P_Tessa_Platform_Runtime_IApplicationDependencies_LinkManager.htm)|
Объект, используемый для обработки ссылок.  
[MessageProvider](P_Tessa_Platform_Runtime_IApplicationDependencies_MessageProvider.htm)|
Объект, обеспечивающий вывод сообщений.  
[ProcessManager](P_Tessa_Platform_Runtime_IApplicationDependencies_ProcessManager.htm)|
Объект, обеспечивающий запуск дочерних процессов.  
[RouteSettings](P_Tessa_Platform_Runtime_IApplicationDependencies_RouteSettings.htm)|
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.  
[RuntimeSettings](P_Tessa_Platform_Runtime_IApplicationDependencies_RuntimeSettings.htm)|
Настройки, связанные с исполняющей средой системы.  
[Session](P_Tessa_Platform_Runtime_IApplicationDependencies_Session.htm)|
Сессия пользователя. Сессию можно использовать только после того, как она была
открыта в процессе запуска приложения.  
[SessionManager](P_Tessa_Platform_Runtime_IApplicationDependencies_SessionManager.htm)|
Объект для управления клиентскими сессиями.  
[UnityContainer](P_Tessa_Platform_Runtime_IApplicationDependencies_UnityContainer.htm)|
Контейнер Unity, используемый для получения зависимостей для расширений.  
##  __Методы
[CreateContext](M_Tessa_Platform_Runtime_IApplicationDependencies_CreateContext.htm)|
Создаёт контекст, связанный с приложением.  
---|---  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
