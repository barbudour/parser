# CardStoreRequest.FromTypedJson - метод
Устанавливает содержимое запроса в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением типов. Для десериализации других объектов, у
которых нет метода FromTypedJson (например, request/response), используйте
метод
[DeserializeFromTypedJson(String)](M_Tessa_Platform_Storage_StorageHelper_DeserializeFromTypedJson.htm),
записав полученную структуру в объект obj.SetStorage(storage).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreRequest FromTypedJson(
    	string json
    )
VB __Копировать
     Public Function FromTypedJson ( 
    	json As String
    ) As CardStoreRequest
C++ __Копировать
     public:
    CardStoreRequest^ FromTypedJson(
    	String^ json
    )
F# __Копировать
     member FromTypedJson : 
            json : string -> CardStoreRequest 
#### Параметры
json [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строка с данными запроса, сериализованными в текстовый JSON с сохранением типов. Не может быть равна null или пустой строке. 
#### Возвращаемое значение
[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)  
Текущий запрос для цепочки вызовов.
##  __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
