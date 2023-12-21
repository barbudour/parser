# XmlExtensions.GetOuterXml - метод
Возвращает xml - содержимое контейнера container в виде строки включая сам
контейнер
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static string GetOuterXml(
    	[NotNullAttribute] this XContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function GetOuterXml ( 
    	<NotNullAttribute> container As XContainer
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static String^ GetOuterXml(
    	[NotNullAttribute] XContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member GetOuterXml : 
            [<NotNullAttribute>] container : XContainer -> string 
#### Параметры
container
[XContainer](https://learn.microsoft.com/dotnet/api/system.xml.linq.xcontainer)
     Контейнер xml 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Текстовое представление контейнера
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[XContainer](https://learn.microsoft.com/dotnet/api/system.xml.linq.xcontainer).
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
