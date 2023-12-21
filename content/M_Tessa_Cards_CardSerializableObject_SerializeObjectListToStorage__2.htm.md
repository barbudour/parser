# CardSerializableObject.SerializeObjectListToStorage<T,
TOrder>(Dictionary<String, Object>, String, ICollection<T>, Func<T, TOrder>) -
метод
Выполняет сериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в хранилище
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectListToStorage<T, TOrder>(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[CanBeNullAttribute] ICollection<T> items,
    	[NotNullAttribute] Func<T, TOrder> getOrderingKey
    )
    where T : CardSerializableObject
VB __Копировать
     Protected Shared Sub SerializeObjectListToStorage(Of T As CardSerializableObject, TOrder) ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<CanBeNullAttribute> items As ICollection(Of T),
    	<NotNullAttribute> getOrderingKey As Func(Of T, TOrder)
    )
C++ __Копировать
     protected:
    generic<typename T, typename TOrder>
    where T : CardSerializableObject
    static void SerializeObjectListToStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[CanBeNullAttribute] ICollection<T>^ items, 
    	[NotNullAttribute] Func<T, TOrder>^ getOrderingKey
    )
F# __Копировать
     static member SerializeObjectListToStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<CanBeNullAttribute>] items : ICollection<'T> * 
            [<NotNullAttribute>] getOrderingKey : Func<'T, 'TOrder> -> unit  when 'T : CardSerializableObject
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое должно содержать сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные должны быть расположены в хранилище storage. 
items
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
     Коллекция сериализуемых объектов. Если значение равно null, то сериализована будет пустая коллекция. 
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
[SerializeObjectListToStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeObjectListToStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
