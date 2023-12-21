# CardStoreRequest.FromPlainJsonWithRepairAsync - метод
Устанавливает содержимое запроса в соответствии с данными, десериализованными
из текстового JSON. Типы произвольных данных
[Info](P_Tessa_Platform_Storage_InfoStorageObject_Info.htm) для карточки,
файлов и заданий могут быть искажены, т.к. информация об их структуре
неизвестна объекту. В JSON все типы запроса десериализуются как
[String](https://learn.microsoft.com/dotnet/api/system.string),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Int64](https://learn.microsoft.com/dotnet/api/system.int64) и
[Double](https://learn.microsoft.com/dotnet/api/system.double). Возвращает
текущий запрос для цепочки вызовов. Рассмотрите использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе
[FromTypedJson(String)](M_Tessa_Cards_CardStoreRequest_FromTypedJson.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardStoreRequest> FromPlainJsonWithRepairAsync(
    	string json,
    	ICardMetadata cardMetadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function FromPlainJsonWithRepairAsync ( 
    	json As String,
    	cardMetadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardStoreRequest)
C++ __Копировать
     public:
    ValueTask<CardStoreRequest^> FromPlainJsonWithRepairAsync(
    	String^ json, 
    	ICardMetadata^ cardMetadata, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member FromPlainJsonWithRepairAsync : 
            json : string * 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardStoreRequest> 
#### Параметры
json [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строка с данными запроса, сериализованными в текстовый JSON. Не может быть равна null или пустой строке. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
     Метаинформация по типам карточек. Не может быть равна null. Используется для исправления типов данных в секциях карточки, файлов и заданий. Если один из типов отсутствует в метаинформации, то поля этого типа не будут исправлены, но исключение не будет выброшено. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)>  
Текущий запрос для цепочки вызовов.
##  __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
