# CardSerializableObject.SerializeGuidListToXml - метод
Выполняет сериализацию заданного объекта SealableList<Guid> в XML-атрибут
посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeGuidListToXml(
    	[NotNullAttribute] XmlWriter writer,
    	[NotNullAttribute] string attributeName,
    	[CanBeNullAttribute] SealableList<Guid> list
    )
VB __Копировать
     Protected Shared Sub SerializeGuidListToXml ( 
    	<NotNullAttribute> writer As XmlWriter,
    	<NotNullAttribute> attributeName As String,
    	<CanBeNullAttribute> list As SealableList(Of Guid)
    )
C++ __Копировать
     protected:
    static void SerializeGuidListToXml(
    	[NotNullAttribute] XmlWriter^ writer, 
    	[NotNullAttribute] String^ attributeName, 
    	[CanBeNullAttribute] SealableList<Guid>^ list
    )
F# __Копировать
     static member SerializeGuidListToXml : 
            [<NotNullAttribute>] writer : XmlWriter * 
            [<NotNullAttribute>] attributeName : string * 
            [<CanBeNullAttribute>] list : SealableList<Guid> -> unit 
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, осуществляющий запись в XML.
attributeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя атрибута XML, в который сериализуется объект.
list
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Сериализуемый объект. Может быть равен null.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
