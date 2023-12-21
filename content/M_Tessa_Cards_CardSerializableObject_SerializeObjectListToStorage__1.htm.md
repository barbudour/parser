# CardSerializableObject.SerializeObjectListToStorage<T>(Dictionary<String,
Object>, String, ICollection<T>) - метод
Выполняет сериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в хранилище
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectListToStorage<T>(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[CanBeNullAttribute] ICollection<T> items
    )
    where T : CardSerializableObject
VB __Копировать
     Protected Shared Sub SerializeObjectListToStorage(Of T As CardSerializableObject) ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<CanBeNullAttribute> items As ICollection(Of T)
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : CardSerializableObject
    static void SerializeObjectListToStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[CanBeNullAttribute] ICollection<T>^ items
    )
F# __Копировать
     static member SerializeObjectListToStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<CanBeNullAttribute>] items : ICollection<'T> -> unit  when 'T : CardSerializableObject
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
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[SerializeObjectListToStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeObjectListToStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
