# PluginFacade.StartHostInfo.SetAwaitGracefulStopSeconds - метод
Задаёт количество секунд, которые выполняется ожидание вежливого завершения
всех плагинов со стороны хоста.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginFacade.StartHostInfo SetAwaitGracefulStopSeconds(
    	double awaitGracefulStopSeconds
    )
VB __Копировать
     Public Function SetAwaitGracefulStopSeconds ( 
    	awaitGracefulStopSeconds As Double
    ) As PluginFacade.StartHostInfo
C++ __Копировать
     public:
    PluginFacade.StartHostInfo^ SetAwaitGracefulStopSeconds(
    	double awaitGracefulStopSeconds
    )
F# __Копировать
     member SetAwaitGracefulStopSeconds : 
            awaitGracefulStopSeconds : float -> PluginFacade.StartHostInfo 
#### Параметры
awaitGracefulStopSeconds
[Double](https://learn.microsoft.com/dotnet/api/system.double)
     Количество секунд, которые выполняется ожидание вежливого завершения всех плагинов со стороны хоста. 
#### Возвращаемое значение
[PluginFacade.StartHostInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)  
Текущий объект.
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
