# ProcessLogger.LogHostIsShutdown - метод
Логирует отладочную информацию о том, что хост-процесс в текущем процессе был
остановлен.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void LogHostIsShutdown(
    	string serviceName
    )
VB __Копировать
     Public Shared Sub LogHostIsShutdown ( 
    	serviceName As String
    )
C++ __Копировать
     public:
    static void LogHostIsShutdown(
    	String^ serviceName
    )
F# __Копировать
     static member LogHostIsShutdown : 
            serviceName : string -> unit 
#### Параметры
serviceName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя сервиса Chronos, которое идентифицирует текущий хост-процесс.
##  __См. также
#### Ссылки
[ProcessLogger - ](T_Chronos_Platform_ProcessLogger.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
