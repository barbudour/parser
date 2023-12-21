# PluginImportingItem.TryResolveConfigs - метод
Возвращает информацию о плагине, которая была загружена из всех
конфигурационных файлов, указанных в триггерах, или null, если доступные
плагины отсуствуют.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginImportingItem TryResolveConfigs()
VB __Копировать
     Public Function TryResolveConfigs As PluginImportingItem
C++ __Копировать
     public:
    PluginImportingItem^ TryResolveConfigs()
F# __Копировать
     member TryResolveConfigs : unit -> PluginImportingItem 
#### Возвращаемое значение
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)  
Преобразованная информация о плагине, в которой удалены триггеры, указывающие
на конфигурационные файлы, и добавлена информация из этих файлов. Возвращается
null, если доступные плагины отсутствуют.
## __См. также
#### Ссылки
[PluginImportingItem -
](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
