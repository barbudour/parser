# CardSerializableObject.SerializeObjectListToXml<T, TOrder>(XmlWriter,
ICollection<T>, Func<T, TOrder>) - метод
Выполняет сериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в XML
посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectListToXml<T, TOrder>(
    	[NotNullAttribute] XmlWriter writer,
    	[CanBeNullAttribute] ICollection<T> items,
    	[NotNullAttribute] Func<T, TOrder> getOrderingKey
    )
    where T : CardSerializableObject
VB __Копировать
     Protected Shared Sub SerializeObjectListToXml(Of T As CardSerializableObject, TOrder) ( 
    	<NotNullAttribute> writer As XmlWriter,
    	<CanBeNullAttribute> items As ICollection(Of T),
    	<NotNullAttribute> getOrderingKey As Func(Of T, TOrder)
    )
C++ __Копировать
     protected:
    generic<typename T, typename TOrder>
    where T : CardSerializableObject
    static void SerializeObjectListToXml(
    	[NotNullAttribute] XmlWriter^ writer, 
    	[CanBeNullAttribute] ICollection<T>^ items, 
    	[NotNullAttribute] Func<T, TOrder>^ getOrderingKey
    )
F# __Копировать
     static member SerializeObjectListToXml : 
            [<NotNullAttribute>] writer : XmlWriter * 
            [<CanBeNullAttribute>] items : ICollection<'T> * 
            [<NotNullAttribute>] getOrderingKey : Func<'T, 'TOrder> -> unit  when 'T : CardSerializableObject
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, осуществляющий запись в XML.
items
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
     Коллекция сериализуемых объектов. Если значение равно null, то будет сериализована пустая коллекция. 
getOrderingKey [Func](https://learn.microsoft.com/dotnet/api/system.func-2)<T,
TOrder>
     Функция, возвращающая значение свойства, которое используется для сортировки коллекции перед её сериализацией. Объекты коллекции сортируются по возрастанию с использованием компаратора по умолчанию. 
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
TOrder
     Тип свойства объектов, которое используется для сортировки коллекции перед её сериализацией. 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[SerializeObjectListToXml -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeObjectListToXml.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
