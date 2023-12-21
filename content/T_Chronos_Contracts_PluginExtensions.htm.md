# PluginExtensions - класс
Методы-расширения для интерфейса [IPlugin](T_Chronos_Contracts_IPlugin.htm).
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PluginExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class PluginExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class PluginExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type PluginExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginExtensions
##  __Методы
[LoadConfig(IPlugin)](M_Chronos_Contracts_PluginExtensions_LoadConfig.htm)|
Загружает первый используемый конфигурационный файл для заданного плагина, и
возвращает загруженный XML-документ.  
---|---  
[LoadConfig(IPlugin,
String)](M_Chronos_Contracts_PluginExtensions_LoadConfig_1.htm)|  Загружает
конфигурационный файл для заданного плагина и указанного пути к файлу
относительно папки, в которой расположена сборка с плагином, и возвращает
загруженный XML-документ.  
[PluginAttribute](M_Chronos_Contracts_PluginExtensions_PluginAttribute.htm)|
Возвращает XML-атрибут, загруженный из XML-элемента конфигурационного файла
плагина.  
[PluginElement](M_Chronos_Contracts_PluginExtensions_PluginElement.htm)|
Возвращает XML-элемент, загруженный из XML-элемента конфигурационного файла
плагина.  
[TryLoadConfig(IPlugin)](M_Chronos_Contracts_PluginExtensions_TryLoadConfig.htm)|
Загружает первый используемый конфигурационный файл для заданного плагина, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.  
[TryLoadConfig(IPlugin,
String)](M_Chronos_Contracts_PluginExtensions_TryLoadConfig_1.htm)|  Загружает
конфигурационный файл для заданного плагина и указанного пути к файлу
относительно папки, в которой расположена сборка с плагином, и возвращает
загруженный XML-документ или null, если файл отсутствовал по заданному пути.  
## __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
