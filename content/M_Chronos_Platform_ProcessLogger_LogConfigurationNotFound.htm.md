# ProcessLogger.LogConfigurationNotFound - метод
Выполняет логирование ошибки о том, что файл конфигурации плагина не найден.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void LogConfigurationNotFound(
    	string fileName,
    	PluginImportingItem pluginImportingItem
    )
VB __Копировать
     Public Shared Sub LogConfigurationNotFound ( 
    	fileName As String,
    	pluginImportingItem As PluginImportingItem
    )
C++ __Копировать
     public:
    static void LogConfigurationNotFound(
    	String^ fileName, 
    	PluginImportingItem^ pluginImportingItem
    )
F# __Копировать
     static member LogConfigurationNotFound : 
            fileName : string * 
            pluginImportingItem : PluginImportingItem -> unit 
#### Параметры
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя файла конфигурации.
pluginImportingItem
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
    Объект, описывающий плагин.
##  __См. также
#### Ссылки
[ProcessLogger - ](T_Chronos_Platform_ProcessLogger.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
