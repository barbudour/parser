# CardSerializableObject.SerializeObjectListToStorage<T>(Dictionary<String,
Object>, String, IEnumerable<KeyValuePair<String, T>>,
ICardSerializableContext) - метод
Выполняет сериализацию хеш-таблицы объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в хранилище
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectListToStorage<T>(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[CanBeNullAttribute] IEnumerable<KeyValuePair<string, T>> items,
    	ICardSerializableContext context
    )
    where T : CardSerializableObject
VB __Копировать
     Protected Shared Sub SerializeObjectListToStorage(Of T As CardSerializableObject) ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<CanBeNullAttribute> items As IEnumerable(Of KeyValuePair(Of String, T)),
    	context As ICardSerializableContext
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : CardSerializableObject
    static void SerializeObjectListToStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[CanBeNullAttribute] IEnumerable<KeyValuePair<String^, T>>^ items, 
    	ICardSerializableContext^ context
    )
F# __Копировать
     static member SerializeObjectListToStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<CanBeNullAttribute>] items : IEnumerable<KeyValuePair<string, 'T>> * 
            context : ICardSerializableContext -> unit  when 'T : CardSerializableObject
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое должно содержать сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные должны быть расположены в хранилище storage. 
items
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
T>>
     Коллекция пар с ключом, по которому записывается сериализуемый объект, и самим сериализуемым объектом. Если значение равно null, то сериализована будет пустая хеш-таблица. 
context [ICardSerializableContext](T_Tessa_Cards_ICardSerializableContext.htm)
    Контекст, содержащий информацию по сериализации об объекте [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm).
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[SerializeObjectListToStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeObjectListToStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
