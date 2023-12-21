# CardSerializableObject.DeserializeObjectFromXmlToList<T> \- метод
Выполняет десериализацию объекта
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) из XML
посредством объекта
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader) и
добавление десериализованного объекта в заданную коллекцию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeObjectFromXmlToList<T>(
    	[NotNullAttribute] XmlReader reader,
    	[NotNullAttribute] ICollection<T> items
    )
    where T : new(), CardSerializableObject
VB __Копировать
     Protected Shared Sub DeserializeObjectFromXmlToList(Of T As {New, CardSerializableObject}) ( 
    	<NotNullAttribute> reader As XmlReader,
    	<NotNullAttribute> items As ICollection(Of T)
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static void DeserializeObjectFromXmlToList(
    	[NotNullAttribute] XmlReader^ reader, 
    	[NotNullAttribute] ICollection<T>^ items
    )
F# __Копировать
     static member DeserializeObjectFromXmlToList : 
            [<NotNullAttribute>] reader : XmlReader * 
            [<NotNullAttribute>] items : ICollection<'T> -> unit  when 'T : new() and CardSerializableObject
#### Параметры
reader
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader)
    Объект, осуществляющий чтение из XML.
items
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
     Коллекция, в которую будет добавлен десериализованный объект. Значение не может быть равно null. 
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и определять конструктор по умолчанию. 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
