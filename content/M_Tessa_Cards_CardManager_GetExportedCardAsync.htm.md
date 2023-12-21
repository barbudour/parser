# CardManager.GetExportedCardAsync - метод
Загружает карточку, которая была экспортирована в файл.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardGetResponse> GetExportedCardAsync(
    	ISourceContentProvider sourceContentProvider,
    	Func<CardFileContentParameter, ValueTask> processFileActionAsync,
    	CardFileFormat format = CardFileFormat.Binary,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetExportedCardAsync ( 
    	sourceContentProvider As ISourceContentProvider,
    	processFileActionAsync As Func(Of CardFileContentParameter, ValueTask),
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
     public:
    virtual Task<CardGetResponse^>^ GetExportedCardAsync(
    	ISourceContentProvider^ sourceContentProvider, 
    	Func<CardFileContentParameter^, ValueTask>^ processFileActionAsync, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetExportedCardAsync : 
            sourceContentProvider : ISourceContentProvider * 
            processFileActionAsync : Func<CardFileContentParameter, ValueTask> * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
    override GetExportedCardAsync : 
            sourceContentProvider : ISourceContentProvider * 
            processFileActionAsync : Func<CardFileContentParameter, ValueTask> * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
#### Параметры
sourceContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
     Провайдер для ресурса, представляющего карточку. Например файл и т.п. 
processFileActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CardFileContentParameter](T_Tessa_Cards_CardFileContentParameter.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
    Метод, выполняющий обработку для каждого из файлов, приложенных к карточке.
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm) (Optional)
    Формат файла для экспортированной карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)>  
Ответ на запрос на загрузку карточки, экспортированной в файл.
#### Реализации
[ICardManager.GetExportedCardAsync(ISourceContentProvider,
Func<CardFileContentParameter, ValueTask>, CardFileFormat,
CancellationToken)](M_Tessa_Cards_ICardManager_GetExportedCardAsync.htm)  
##  __См. также
#### Ссылки
[CardManager - ](T_Tessa_Cards_CardManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
