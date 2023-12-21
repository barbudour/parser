# ProcessLogger.LogHostIsLaunchingPlugin - метод
Логирует отладочную информацию о том, что начался запуск плагина в дочернем
процессе.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void LogHostIsLaunchingPlugin(
    	PluginRemoteCreationInfo creationInfo
    )
VB __Копировать
     Public Shared Sub LogHostIsLaunchingPlugin ( 
    	creationInfo As PluginRemoteCreationInfo
    )
C++ __Копировать
     public:
    static void LogHostIsLaunchingPlugin(
    	PluginRemoteCreationInfo^ creationInfo
    )
F# __Копировать
     static member LogHostIsLaunchingPlugin : 
            creationInfo : PluginRemoteCreationInfo -> unit 
#### Параметры
creationInfo
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)
    Информация по параметрам запуска плагина.
##  __См. также
#### Ссылки
[ProcessLogger - ](T_Chronos_Platform_ProcessLogger.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
