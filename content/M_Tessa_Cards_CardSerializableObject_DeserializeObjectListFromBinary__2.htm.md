# CardSerializableObject.DeserializeObjectListFromBinary<TItem,
TCollection>(BinaryReader, TCollection, Func<Int32, TCollection>) - метод
Выполняет десериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) из
байтового потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeObjectListFromBinary<TItem, TCollection>(
    	[NotNullAttribute] BinaryReader reader,
    	[CanBeNullAttribute] ref TCollection items,
    	[NotNullAttribute] Func<int, TCollection> createItemsFunc
    )
    where TItem : new(), CardSerializableObject
    where TCollection : class, Object, ICollection<TItem>
VB __Копировать
     Protected Shared Sub DeserializeObjectListFromBinary(Of TItem As {New, CardSerializableObject}, TCollection As {Class, Object, ICollection(Of TItem)}) ( 
    	<NotNullAttribute> reader As BinaryReader,
    	<CanBeNullAttribute> ByRef items As TCollection,
    	<NotNullAttribute> createItemsFunc As Func(Of Integer, TCollection)
    )
C++ __Копировать
     protected:
    generic<typename TItem, typename TCollection>
    where TItem : gcnew(), CardSerializableObject
    where TCollection : ref class, Object, ICollection<TItem>
    static void DeserializeObjectListFromBinary(
    	[NotNullAttribute] BinaryReader^ reader, 
    	[CanBeNullAttribute] TCollection% items, 
    	[NotNullAttribute] Func<int, TCollection>^ createItemsFunc
    )
F# __Копировать
     static member DeserializeObjectListFromBinary : 
            [<NotNullAttribute>] reader : BinaryReader * 
            [<CanBeNullAttribute>] items : 'TCollection byref * 
            [<NotNullAttribute>] createItemsFunc : Func<int, 'TCollection> -> unit  when 'TItem : new() and CardSerializableObject when 'TCollection : not struct and Object and ICollection<'TItem>
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из байтового потока.
items TCollection
     Коллекция, в которую будут записаны десериализованные объекты. Если значение равно null, то будет создана новая коллекция, в противном случае существующая коллекция будет очищена. 
createItemsFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32),
TCollection>
     Функция, получающая размер коллекции TCollection и возвращающая её экземпляр. 
#### Параметры типа
TItem
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и определять конструктор по умолчанию. 
TCollection
     Ссылочный тип коллекции, содержащей объекты типа TItem. Объект должен реализовывать интерфейс [ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1) с типом TItem. 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeObjectListFromBinary -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromBinary.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
