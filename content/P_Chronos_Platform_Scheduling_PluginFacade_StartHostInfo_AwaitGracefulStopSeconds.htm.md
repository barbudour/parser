# PluginFacade.StartHostInfo.AwaitGracefulStopSeconds - свойство
Количество секунд, которые выполняется ожидание вежливого завершения всех
плагинов со стороны хоста.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public double AwaitGracefulStopSeconds { get; }
VB __Копировать
     Public ReadOnly Property AwaitGracefulStopSeconds As Double
    	Get
C++ __Копировать
     public:
    property double AwaitGracefulStopSeconds {
    	double get ();
    }
F# __Копировать
     member AwaitGracefulStopSeconds : float with get
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
##  __Заметки
Значение используется только для
[ShutdownMode](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_ShutdownMode.htm),
равного [GracefulStop](T_Chronos_Platform_Scheduling_PluginShutdownMode.htm).
## __См. также
#### Ссылки
[PluginFacade.StartHostInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
