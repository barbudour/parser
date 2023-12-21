# PluginImporter.Import - метод
Выполняет импортирование плагинов, используя указанный объект для поиска
плагинов.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginImportingResult Import(
    	IPluginFinder pluginFinder
    )
VB __Копировать
     Public Function Import ( 
    	pluginFinder As IPluginFinder
    ) As PluginImportingResult
C++ __Копировать
     public:
    PluginImportingResult^ Import(
    	IPluginFinder^ pluginFinder
    )
F# __Копировать
     member Import : 
            pluginFinder : IPluginFinder -> PluginImportingResult 
#### Параметры
pluginFinder [IPluginFinder](T_Chronos_Platform_Scheduling_IPluginFinder.htm)
    Объект, позволяющий выполнять поиск плагинов.
#### Возвращаемое значение
[PluginImportingResult](T_Chronos_Platform_Scheduling_PluginImportingResult.htm)  
Результат импортирования.
##  __См. также
#### Ссылки
[PluginImporter - ](T_Chronos_Platform_Scheduling_PluginImporter.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
