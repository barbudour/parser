# CardSerializableObject.SerializeObjectListToXml<T>(XmlWriter,
ICollection<T>) - метод
Выполняет сериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в XML
посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectListToXml<T>(
    	[NotNullAttribute] XmlWriter writer,
    	[CanBeNullAttribute] ICollection<T> items
    )
    where T : CardSerializableObject
VB __Копировать
     Protected Shared Sub SerializeObjectListToXml(Of T As CardSerializableObject) ( 
    	<NotNullAttribute> writer As XmlWriter,
    	<CanBeNullAttribute> items As ICollection(Of T)
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : CardSerializableObject
    static void SerializeObjectListToXml(
    	[NotNullAttribute] XmlWriter^ writer, 
    	[CanBeNullAttribute] ICollection<T>^ items
    )
F# __Копировать
     static member SerializeObjectListToXml : 
            [<NotNullAttribute>] writer : XmlWriter * 
            [<CanBeNullAttribute>] items : ICollection<'T> -> unit  when 'T : CardSerializableObject
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, осуществляющий запись в XML.
items
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
     Коллекция сериализуемых объектов. Если значение равно null, то будет сериализована пустая коллекция. 
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[SerializeObjectListToXml -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeObjectListToXml.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
