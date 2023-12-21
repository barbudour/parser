# CardSerializableObject.DeserializeFromStorage(Dictionary<String, Object>) -
метод
Десериализует объект и его дочерние объекты из заданного хранилища
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSerializableObject DeserializeFromStorage(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Public Function DeserializeFromStorage ( 
    	storage As Dictionary(Of String, Object)
    ) As CardSerializableObject
C++ __Копировать
     public:
    CardSerializableObject^ DeserializeFromStorage(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     member DeserializeFromStorage : 
            storage : Dictionary<string, Object> -> CardSerializableObject 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в котором содержатся сериализованные данные.
#### Возвращаемое значение
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)  
Десериализованный объект (может подменять значение, при использовании
глобальных ссылок).
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeFromStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
