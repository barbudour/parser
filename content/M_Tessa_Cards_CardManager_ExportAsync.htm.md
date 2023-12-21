# CardManager.ExportAsync(CardGetRequest, CardFileFormat, CancellationToken) -
метод
Выполняет административный экспорт карточки с файлами и заданиями, но не
загружает контент файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardGetResponse> ExportAsync(
    	CardGetRequest request,
    	CardFileFormat format = CardFileFormat.Binary,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ExportAsync ( 
    	request As CardGetRequest,
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
     public:
    virtual Task<CardGetResponse^>^ ExportAsync(
    	CardGetRequest^ request, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ExportAsync : 
            request : CardGetRequest * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
    override ExportAsync : 
            request : CardGetRequest * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на выполнение загрузки карточки для экспорта.
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm) (Optional)
    Формат файла для экспорта карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)>  
Результат выполнения запроса на экспорт карточки.
#### Реализации
[ICardManager.ExportAsync(CardGetRequest, CardFileFormat,
CancellationToken)](M_Tessa_Cards_ICardManager_ExportAsync.htm)  
##  __См. также
#### Ссылки
[CardManager - ](T_Tessa_Cards_CardManager.htm)
[ExportAsync - перегрузка](Overload_Tessa_Cards_CardManager_ExportAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
