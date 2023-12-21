# CardStoreResponse.FromTypedJson - метод
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[Tessa.Platform.Storage.StorageObject.ToTypedJson] для сериализации с
сохранением типов. Для десериализации других объектов, у которых нет метода
FromTypedJson (например, request/response), используйте метод
[Tessa.Platform.Storage.StorageHelper.DeserializeFromTypedJson], записав
полученную структуру в объект obj.SetStorage(storage).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreResponse FromTypedJson(
    	string json
    )
VB __Копировать
     Public Function FromTypedJson ( 
    	json As String
    ) As CardStoreResponse
C++ __Копировать
     public:
    CardStoreResponse^ FromTypedJson(
    	String^ json
    )
F# __Копировать
     member FromTypedJson : 
            json : string -> CardStoreResponse 
#### Параметры
json [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строка с данными карточки, сериализованными в текстовый JSON с сохранением типов. Не может быть равна null или пустой строке. 
#### Возвращаемое значение
[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardStoreResponse - ](T_Tessa_Cards_CardStoreResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
