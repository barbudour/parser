# PluginExtensions.LoadConfig(IPlugin, String) - метод
Загружает конфигурационный файл для заданного плагина и указанного пути к
файлу относительно папки, в которой расположена сборка с плагином, и
возвращает загруженный XML-документ.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement LoadConfig(
    	this IPlugin plugin,
    	string relativeFilePath
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function LoadConfig ( 
    	plugin As IPlugin,
    	relativeFilePath As String
    ) As XElement
C++ __Копировать
     public:
    [ExtensionAttribute]
    static XElement^ LoadConfig(
    	IPlugin^ plugin, 
    	String^ relativeFilePath
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member LoadConfig : 
            plugin : IPlugin * 
            relativeFilePath : string -> XElement 
#### Параметры
plugin [IPlugin](T_Chronos_Contracts_IPlugin.htm)
    Плагин, для которого необходимо загрузить конфигурационный файл.
relativeFilePath
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу относительно папки, в которой расположена сборка с плагином.
#### Возвращаемое значение
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement)  
Корневой элемент конфигурационного файла.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [IPlugin](T_Chronos_Contracts_IPlugin.htm). При вызове метода для
экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[PluginExtensions - ](T_Chronos_Contracts_PluginExtensions.htm)
[LoadConfig -
перегрузка](Overload_Chronos_Contracts_PluginExtensions_LoadConfig.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
