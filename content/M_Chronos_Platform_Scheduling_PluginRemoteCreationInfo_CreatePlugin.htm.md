# PluginRemoteCreationInfo.CreatePlugin - метод
Создаёт экземпляр плагина. При необходимости загружается сборка, содержащая
плагин.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IPlugin CreatePlugin(
    	Assembly assembly = null
    )
VB __Копировать
     Public Function CreatePlugin ( 
    	Optional assembly As Assembly = Nothing
    ) As IPlugin
C++ __Копировать
     public:
    IPlugin^ CreatePlugin(
    	Assembly^ assembly = nullptr
    )
F# __Копировать
     member CreatePlugin : 
            ?assembly : Assembly 
    (* Defaults:
            let _assembly = defaultArg assembly null
    *)
    -> IPlugin 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
(Optional)
     Сборка, в которой расположен класс плагина, или null, если сборка загружается автоматически в этом методе. 
#### Возвращаемое значение
[IPlugin](T_Chronos_Contracts_IPlugin.htm)  
Ссылка на экземпляр плагина.
##  __См. также
#### Ссылки
[PluginRemoteCreationInfo -
](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
