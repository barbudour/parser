# PluginImportingItem - конструктор
Создаёт экземпляр класса с указанием типа плагина, метаданных плагина и списка
дополнительных триггеров.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginImportingItem(
    	string pluginAssemblyQualifiedName,
    	string pluginAssemblyLocation,
    	string pluginTypeFullName,
    	bool supportGracefulStop,
    	IPluginMetadata pluginMetadata,
    	IList<IPluginMetadataTrigger> additionalTriggers
    )
VB __Копировать
     Public Sub New ( 
    	pluginAssemblyQualifiedName As String,
    	pluginAssemblyLocation As String,
    	pluginTypeFullName As String,
    	supportGracefulStop As Boolean,
    	pluginMetadata As IPluginMetadata,
    	additionalTriggers As IList(Of IPluginMetadataTrigger)
    )
C++ __Копировать
     public:
    PluginImportingItem(
    	String^ pluginAssemblyQualifiedName, 
    	String^ pluginAssemblyLocation, 
    	String^ pluginTypeFullName, 
    	bool supportGracefulStop, 
    	IPluginMetadata^ pluginMetadata, 
    	IList<IPluginMetadataTrigger^>^ additionalTriggers
    )
F# __Копировать
     new : 
            pluginAssemblyQualifiedName : string * 
            pluginAssemblyLocation : string * 
            pluginTypeFullName : string * 
            supportGracefulStop : bool * 
            pluginMetadata : IPluginMetadata * 
            additionalTriggers : IList<IPluginMetadataTrigger> -> PluginImportingItem
#### Параметры
pluginAssemblyQualifiedName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Полное имя типа плагина с указанием имени сборки.
pluginAssemblyLocation
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к сборке, содержащей плагин.
pluginTypeFullName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Полное имя типа плагина.
supportGracefulStop
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что плагин поддерживает вежливую остановку через интерфейс [ISupportGracefulStop](T_Chronos_Contracts_ISupportGracefulStop.htm).
pluginMetadata [IPluginMetadata](T_Chronos_Contracts_IPluginMetadata.htm)
    Метаданные плагина.
additionalTriggers
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm)>
    Список дополнительных триггеров (кроме метаданных pluginMetadata).
##  __См. также
#### Ссылки
[PluginImportingItem -
](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
