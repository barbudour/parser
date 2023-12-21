# PluginExtensions.TryLoadConfig(IPlugin, String) - метод
Загружает конфигурационный файл для заданного плагина и указанного пути к
файлу относительно папки, в которой расположена сборка с плагином, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement TryLoadConfig(
    	this IPlugin plugin,
    	string relativeFilePath
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryLoadConfig ( 
    	plugin As IPlugin,
    	relativeFilePath As String
    ) As XElement
C++ __Копировать
     public:
    [ExtensionAttribute]
    static XElement^ TryLoadConfig(
    	IPlugin^ plugin, 
    	String^ relativeFilePath
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryLoadConfig : 
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
Корневой элемент конфигурационного файла или null, если файл отсутствовал по
заданному пути.
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
[TryLoadConfig -
перегрузка](Overload_Chronos_Contracts_PluginExtensions_TryLoadConfig.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
