# PluginConfigHelper.TryLoadXmlImportingItem - метод
Загружает информацию о плагине из конфигурационного файла.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static PluginImportingItem TryLoadXmlImportingItem(
    	string filename,
    	PluginImportingItem sourcePluginImport
    )
VB __Копировать
     Public Shared Function TryLoadXmlImportingItem ( 
    	filename As String,
    	sourcePluginImport As PluginImportingItem
    ) As PluginImportingItem
C++ __Копировать
     public:
    static PluginImportingItem^ TryLoadXmlImportingItem(
    	String^ filename, 
    	PluginImportingItem^ sourcePluginImport
    )
F# __Копировать
     static member TryLoadXmlImportingItem : 
            filename : string * 
            sourcePluginImport : PluginImportingItem -> PluginImportingItem 
#### Параметры
filename [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя конфигурационного файла. Обычно следует указывать полное имя файла.
sourcePluginImport
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
     Импортированная информация о плагине, на основании которой будут частично заполнены поля возвращаемого объекта. 
#### Возвращаемое значение
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)  
Информация о плагине.
##  __См. также
#### Ссылки
[PluginConfigHelper - ](T_Chronos_Platform_PluginConfigHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
