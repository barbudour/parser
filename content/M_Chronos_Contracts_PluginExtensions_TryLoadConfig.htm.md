# PluginExtensions.TryLoadConfig(IPlugin) - метод
Загружает первый используемый конфигурационный файл для заданного плагина, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement TryLoadConfig(
    	this IPlugin plugin
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryLoadConfig ( 
    	plugin As IPlugin
    ) As XElement
C++ __Копировать
     public:
    [ExtensionAttribute]
    static XElement^ TryLoadConfig(
    	IPlugin^ plugin
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryLoadConfig : 
            plugin : IPlugin -> XElement 
#### Параметры
plugin [IPlugin](T_Chronos_Contracts_IPlugin.htm)
    Плагин, для которого необходимо загрузить конфигурационный файл, указанный в атрибутах.
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
##  __Заметки
Если плагин имеет несколько конфигурационных файлов, то рекомендуется
использовать перегрузку метода, принимающую относительный путь к файлу.
## __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Конфигурационный файл не был указан в атрибутах плагина
[PluginAttribute(XElement,
String)](M_Chronos_Contracts_PluginExtensions_PluginAttribute.htm) или
[PluginTriggerAttribute](T_Chronos_Contracts_PluginTriggerAttribute.htm).  
---|---  
## __См. также
#### Ссылки
[PluginExtensions - ](T_Chronos_Contracts_PluginExtensions.htm)
[TryLoadConfig -
перегрузка](Overload_Chronos_Contracts_PluginExtensions_TryLoadConfig.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
