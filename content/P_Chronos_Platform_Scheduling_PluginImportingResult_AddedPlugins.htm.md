# PluginImportingResult.AddedPlugins - свойство
Получает список плагинов, которые ранее отсутствовали и были добавлены при
данном импортировании.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<PluginImportingItem> AddedPlugins { get; }
VB __Копировать
     Public ReadOnly Property AddedPlugins As IList(Of PluginImportingItem)
    	Get
C++ __Копировать
     public:
    property IList<PluginImportingItem^>^ AddedPlugins {
    	IList<PluginImportingItem^>^ get ();
    }
F# __Копировать
     member AddedPlugins : IList<PluginImportingItem> with get
#### Значение свойства
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)>
##  __См. также
#### Ссылки
[PluginImportingResult -
](T_Chronos_Platform_Scheduling_PluginImportingResult.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
