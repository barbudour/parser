# XmlExtensions.GetDocumentXml - метод
Возвращает полное xml - содержимое документа document в текстовом виде
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static string GetDocumentXml(
    	[NotNullAttribute] this XDocument document
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function GetDocumentXml ( 
    	<NotNullAttribute> document As XDocument
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static String^ GetDocumentXml(
    	[NotNullAttribute] XDocument^ document
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member GetDocumentXml : 
            [<NotNullAttribute>] document : XDocument -> string 
#### Параметры
document
[XDocument](https://learn.microsoft.com/dotnet/api/system.xml.linq.xdocument)
     Обрабатываемый документ 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Текстовое представление документа
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[XDocument](https://learn.microsoft.com/dotnet/api/system.xml.linq.xdocument).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[XmlExtensions - ](T_Tessa_Applications_Containers_Storage_XmlExtensions.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
