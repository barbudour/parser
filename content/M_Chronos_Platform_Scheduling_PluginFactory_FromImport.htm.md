# PluginFactory.FromImport - метод
Возвращает информацию для создания плагина из
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static PluginRemoteCreationInfo FromImport(
    	PluginImportingItem pluginImport,
    	PluginShutdownMode hostShutdownMode
    )
VB __Копировать
     Public Shared Function FromImport ( 
    	pluginImport As PluginImportingItem,
    	hostShutdownMode As PluginShutdownMode
    ) As PluginRemoteCreationInfo
C++ __Копировать
     public:
    static PluginRemoteCreationInfo^ FromImport(
    	PluginImportingItem^ pluginImport, 
    	PluginShutdownMode hostShutdownMode
    )
F# __Копировать
     static member FromImport : 
            pluginImport : PluginImportingItem * 
            hostShutdownMode : PluginShutdownMode -> PluginRemoteCreationInfo 
#### Параметры
pluginImport
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
    Информация об импортируемом плагине.
hostShutdownMode
[PluginShutdownMode](T_Chronos_Platform_Scheduling_PluginShutdownMode.htm)
     Способ завершения процесса хоста, определяющий способ завершения плагинов. 
#### Возвращаемое значение
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)  
Информация для создания плагина.
##  __См. также
#### Ссылки
[PluginFactory - ](T_Chronos_Platform_Scheduling_PluginFactory.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
