# PluginConfigHelper.CreateXmlImportingElement - метод
Создаёт XML-элемент, содержащий полную информацию об указанном плагине.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement CreateXmlImportingElement(
    	PluginImportingItem pluginImport
    )
VB __Копировать
     Public Shared Function CreateXmlImportingElement ( 
    	pluginImport As PluginImportingItem
    ) As XElement
C++ __Копировать
     public:
    static XElement^ CreateXmlImportingElement(
    	PluginImportingItem^ pluginImport
    )
F# __Копировать
     static member CreateXmlImportingElement : 
            pluginImport : PluginImportingItem -> XElement 
#### Параметры
pluginImport
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
    Информация о плагине, на основании которой будет создан XML-элемент.
#### Возвращаемое значение
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement)  
XML-элемент с информацией о плагине.
##  __См. также
#### Ссылки
[PluginConfigHelper - ](T_Chronos_Platform_PluginConfigHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
