# CardSerializableObject.SerializeObjectToXml - метод
Сериализует объект в XML-элемент в форме base64 посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter), если
сериализуемый объект не равен null и непустой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectToXml(
    	[NotNullAttribute] XmlWriter writer,
    	[NotNullAttribute] string elementName,
    	[CanBeNullAttribute] ISerializableObject obj
    )
VB __Копировать
     Protected Shared Sub SerializeObjectToXml ( 
    	<NotNullAttribute> writer As XmlWriter,
    	<NotNullAttribute> elementName As String,
    	<CanBeNullAttribute> obj As ISerializableObject
    )
C++ __Копировать
     protected:
    static void SerializeObjectToXml(
    	[NotNullAttribute] XmlWriter^ writer, 
    	[NotNullAttribute] String^ elementName, 
    	[CanBeNullAttribute] ISerializableObject^ obj
    )
F# __Копировать
     static member SerializeObjectToXml : 
            [<NotNullAttribute>] writer : XmlWriter * 
            [<NotNullAttribute>] elementName : string * 
            [<CanBeNullAttribute>] obj : ISerializableObject -> unit 
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, осуществляющий запись в XML.
elementName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя XML-элемента сериализуемого объекта.
obj [ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
    Объект, сериализация которого выполняется, если он не равен null и непустой.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
