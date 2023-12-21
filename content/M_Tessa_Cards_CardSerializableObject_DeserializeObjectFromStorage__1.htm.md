# CardSerializableObject.DeserializeObjectFromStorage<T>(Dictionary<String,
Object>, String) - метод
Десериализует объект из заданного хранилища Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static T DeserializeObjectFromStorage<T>(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key
    )
    where T : new(), CardSerializableObject
VB __Копировать
     Protected Shared Function DeserializeObjectFromStorage(Of T As {New, CardSerializableObject}) ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String
    ) As T
C++ __Копировать
     protected:
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static T DeserializeObjectFromStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key
    )
F# __Копировать
     static member DeserializeObjectFromStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string -> 'T  when 'T : new() and CardSerializableObject
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные расположены в хранилище storage. 
#### Параметры типа
T
     Тип объекта, содержащегося в хранилище. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и определять конструктор по умолчанию. 
#### Возвращаемое значение
T  
Десериализованный объект.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeObjectFromStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeObjectFromStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
