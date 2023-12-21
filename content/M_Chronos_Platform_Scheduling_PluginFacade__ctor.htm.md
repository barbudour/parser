# PluginFacade - конструктор
Создаёт экземпляр класса с указанием необязательных параметров.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginFacade(
    	string serviceName = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional serviceName As String = Nothing
    )
C++ __Копировать
     public:
    PluginFacade(
    	String^ serviceName = nullptr
    )
F# __Копировать
     new : 
            ?serviceName : string 
    (* Defaults:
            let _serviceName = defaultArg serviceName null
    *)
    -> PluginFacade
#### Параметры
serviceName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя службы Windows для хост-процесса (используется для логирования). Для дочерних процессов достаточно передать null. 
## __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
