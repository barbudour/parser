# PluginExtensions.LoadConfig(IPlugin) - метод
Загружает первый используемый конфигурационный файл для заданного плагина, и
возвращает загруженный XML-документ.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement LoadConfig(
    	this IPlugin plugin
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function LoadConfig ( 
    	plugin As IPlugin
    ) As XElement
C++ __Копировать
     public:
    [ExtensionAttribute]
    static XElement^ LoadConfig(
    	IPlugin^ plugin
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member LoadConfig : 
            plugin : IPlugin -> XElement 
#### Параметры
plugin [IPlugin](T_Chronos_Contracts_IPlugin.htm)
    Плагин, для которого необходимо загрузить конфигурационный файл, указанный в атрибутах.
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
[LoadConfig -
перегрузка](Overload_Chronos_Contracts_PluginExtensions_LoadConfig.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
