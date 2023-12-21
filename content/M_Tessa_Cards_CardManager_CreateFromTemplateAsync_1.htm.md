# CardManager.CreateFromTemplateAsync(ISourceContentProvider,
Func<CardFileContentParameter, ValueTask>, Dictionary<String, Object>,
CardFileFormat, CancellationToken) - метод
Создаёт карточку по шаблону.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(CardNewRequest Request, CardNewResponse Response)> CreateFromTemplateAsync(
    	ISourceContentProvider sourceContentProvider,
    	Func<CardFileContentParameter, ValueTask> processFileActionAsync,
    	Dictionary<string, Object> templateInfo = null,
    	CardFileFormat format = CardFileFormat.Binary,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CreateFromTemplateAsync ( 
    	sourceContentProvider As ISourceContentProvider,
    	processFileActionAsync As Func(Of CardFileContentParameter, ValueTask),
    	Optional templateInfo As Dictionary(Of String, Object) = Nothing,
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Request As CardNewRequest, Response As CardNewResponse))
C++ __Копировать
     public:
    virtual Task<ValueTuple<CardNewRequest^, CardNewResponse^>>^ CreateFromTemplateAsync(
    	ISourceContentProvider^ sourceContentProvider, 
    	Func<CardFileContentParameter^, ValueTask>^ processFileActionAsync, 
    	Dictionary<String^, Object^>^ templateInfo = nullptr, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CreateFromTemplateAsync : 
            sourceContentProvider : ISourceContentProvider * 
            processFileActionAsync : Func<CardFileContentParameter, ValueTask> * 
            ?templateInfo : Dictionary<string, Object> * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _templateInfo = defaultArg templateInfo null
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardNewRequest, CardNewResponse>> 
    override CreateFromTemplateAsync : 
            sourceContentProvider : ISourceContentProvider * 
            processFileActionAsync : Func<CardFileContentParameter, ValueTask> * 
            ?templateInfo : Dictionary<string, Object> * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _templateInfo = defaultArg templateInfo null
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardNewRequest, CardNewResponse>> 
#### Параметры
sourceContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса, представляющего карточку. Например файл и т.п. 
processFileActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CardFileContentParameter](T_Tessa_Cards_CardFileContentParameter.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
    Метод, выполняющий обработку для каждого из файлов, приложенных к карточке.
templateInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
Дополнительная информация, помещаемая в запрос на создание карточки по
шаблону, или null, если дополнительная информация отсутствует.
Если при экспорте карточки была задана дополнительная информация, то она
совмещается с заданной в этом параметре, причём при совпадении ключей
информация в параметре переопределяет информацию, заданную при экспорте.
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm) (Optional)
    Формат файла для экспортированной карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm),
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>>  
Результат операции, т.е. внутренний запрос на создание карточки по шаблону и
ответ на него. Внутренний запрос может иметь значение null, если его не
удалось создать.
#### Реализации
[ICardManager.CreateFromTemplateAsync(ISourceContentProvider,
Func<CardFileContentParameter, ValueTask>, Dictionary<String, Object>,
CardFileFormat,
CancellationToken)](M_Tessa_Cards_ICardManager_CreateFromTemplateAsync_1.htm)  
##  __См. также
#### Ссылки
[CardManager - ](T_Tessa_Cards_CardManager.htm)
[CreateFromTemplateAsync -
перегрузка](Overload_Tessa_Cards_CardManager_CreateFromTemplateAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
