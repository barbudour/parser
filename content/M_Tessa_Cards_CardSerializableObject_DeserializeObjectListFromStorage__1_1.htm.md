#
CardSerializableObject.DeserializeObjectListFromStorage<T>(Dictionary<String,
Object>, String, SealableObjectList<T>) - метод
Выполняет десериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) из
хранилища Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeObjectListFromStorage<T>(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[CanBeNullAttribute] ref SealableObjectList<T> items
    )
    where T : new(), CardSerializableObject
VB __Копировать
     Protected Shared Sub DeserializeObjectListFromStorage(Of T As {New, CardSerializableObject}) ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<CanBeNullAttribute> ByRef items As SealableObjectList(Of T)
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static void DeserializeObjectListFromStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[CanBeNullAttribute] SealableObjectList<T>^% items
    )
F# __Копировать
     static member DeserializeObjectListFromStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<CanBeNullAttribute>] items : SealableObjectList<'T> byref -> unit  when 'T : new() and CardSerializableObject
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные расположены в хранилище storage. 
items
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<T>
     Коллекция, в которую будут записаны десериализованные объекты. Если значение равно null, то будет создана новая коллекция, в противном случае существующая коллекция будет очищена. 
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и определять конструктор по умолчанию. 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeObjectListFromStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
