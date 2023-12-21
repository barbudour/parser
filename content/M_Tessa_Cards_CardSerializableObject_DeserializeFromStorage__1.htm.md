# CardSerializableObject.DeserializeFromStorage<T>(Dictionary<String, Object>)
- метод
Создаёт и десериализует объект из заданного хранилища Dictionary<string,
object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T DeserializeFromStorage<T>(
    	Dictionary<string, Object> storage
    )
    where T : new(), CardSerializableObject
VB __Копировать
     Public Shared Function DeserializeFromStorage(Of T As {New, CardSerializableObject}) ( 
    	storage As Dictionary(Of String, Object)
    ) As T
C++ __Копировать
     public:
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static T DeserializeFromStorage(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     static member DeserializeFromStorage : 
            storage : Dictionary<string, Object> -> 'T  when 'T : new() and CardSerializableObject
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
#### Параметры типа
T
     Тип объекта, содержащегося в хранилище. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и определять конструктор по умолчанию. 
#### Возвращаемое значение
T  
Десериализованный объект (может подменять значение, при использовании
глобальных ссылок).
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeFromStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
