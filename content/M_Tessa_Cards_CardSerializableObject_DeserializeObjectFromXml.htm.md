# CardSerializableObject.DeserializeObjectFromXml - метод
Десериализует объект из XML-элемента в форме base64 посредством объекта
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static SerializableObject DeserializeObjectFromXml(
    	[NotNullAttribute] XmlReader reader
    )
VB __Копировать
     Protected Shared Function DeserializeObjectFromXml ( 
    	<NotNullAttribute> reader As XmlReader
    ) As SerializableObject
C++ __Копировать
     protected:
    static SerializableObject^ DeserializeObjectFromXml(
    	[NotNullAttribute] XmlReader^ reader
    )
F# __Копировать
     static member DeserializeObjectFromXml : 
            [<NotNullAttribute>] reader : XmlReader -> SerializableObject 
#### Параметры
reader
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader)
    Объект, осуществляющий чтение из XML.
#### Возвращаемое значение
[SerializableObject](T_Tessa_Platform_Storage_SerializableObject.htm)  
Десериализованный объект.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
