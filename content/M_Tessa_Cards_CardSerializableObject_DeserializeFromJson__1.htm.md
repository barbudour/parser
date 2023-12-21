# CardSerializableObject.DeserializeFromJson<T>(String) - метод
Создаёт и объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T DeserializeFromJson<T>(
    	string json
    )
    where T : new(), CardSerializableObject
VB __Копировать
     Public Shared Function DeserializeFromJson(Of T As {New, CardSerializableObject}) ( 
    	json As String
    ) As T
C++ __Копировать
     public:
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static T DeserializeFromJson(
    	String^ json
    )
F# __Копировать
     static member DeserializeFromJson : 
            json : string -> 'T  when 'T : new() and CardSerializableObject
#### Параметры
json [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текстовый JSON, который десериализуется. Не должен быть равен null.
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
[DeserializeFromJson -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromJson.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
