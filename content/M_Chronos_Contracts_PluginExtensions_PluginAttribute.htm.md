# PluginExtensions.PluginAttribute - метод
Возвращает XML-атрибут, загруженный из XML-элемента конфигурационного файла
плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static XAttribute PluginAttribute(
    	this XElement element,
    	string name
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function PluginAttribute ( 
    	element As XElement,
    	name As String
    ) As XAttribute
C++ __Копировать
     public:
    [ExtensionAttribute]
    static XAttribute^ PluginAttribute(
    	XElement^ element, 
    	String^ name
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member PluginAttribute : 
            element : XElement * 
            name : string -> XAttribute 
#### Параметры
element
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement)
    XML-элемент конфигурационного файла плагина.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя требуемого XML-атрибута.
#### Возвращаемое значение
[XAttribute](https://learn.microsoft.com/dotnet/api/system.xml.linq.xattribute)  
XML-атрибут, загруженный из XML-элемента конфигурационного файла плагина.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[PluginExtensions - ](T_Chronos_Contracts_PluginExtensions.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
