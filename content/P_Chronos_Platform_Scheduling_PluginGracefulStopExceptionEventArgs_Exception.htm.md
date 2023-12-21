# PluginGracefulStopExceptionEventArgs.Exception - свойство
Исключение, возникшее в методе
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm)
объекта
[GracefulPlugin](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_GracefulPlugin.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Exception Exception { get; }
VB __Копировать
     Public ReadOnly Property Exception As Exception
    	Get
C++ __Копировать
     public:
    property Exception^ Exception {
    	Exception^ get ();
    }
F# __Копировать
     member Exception : Exception with get
#### Значение свойства
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
##  __Заметки
Это может быть любое исключение, кроме
[ThreadAbortException](https://learn.microsoft.com/dotnet/api/system.threading.threadabortexception).
## __См. также
#### Ссылки
[PluginGracefulStopExceptionEventArgs -
](T_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
