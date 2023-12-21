# CardSerializableObject.DeserializeFromJson(String) - метод
Десериализует объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSerializableObject DeserializeFromJson(
    	string json
    )
VB __Копировать
     Public Function DeserializeFromJson ( 
    	json As String
    ) As CardSerializableObject
C++ __Копировать
     public:
    CardSerializableObject^ DeserializeFromJson(
    	String^ json
    )
F# __Копировать
     member DeserializeFromJson : 
            json : string -> CardSerializableObject 
#### Параметры
json [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текстовый JSON, который десериализуется. Не должен быть равен null.
#### Возвращаемое значение
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)  
Десериализованный объект (может подменять значение, при использовании
глобальных ссылок).
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeFromJson -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromJson.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
