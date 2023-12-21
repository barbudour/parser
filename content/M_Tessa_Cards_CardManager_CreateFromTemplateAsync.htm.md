# CardManager.CreateFromTemplateAsync(CardStoreRequest, CardHeader,
Func<Int64, CancellationToken, ValueTask<SubStream>>,
Func<CardFileContentParameter, ValueTask>, Dictionary<String, Object>,
ICardFileSourceMapping, IValidationResultBuilder, CancellationToken) - метод
Создаёт карточку по шаблону.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(CardNewRequest Request, CardNewResponse Response)> CreateFromTemplateAsync(
    	CardStoreRequest request,
    	CardHeader header = null,
    	Func<long, CancellationToken, ValueTask<SubStream>> readNextFileFuncAsync = null,
    	Func<CardFileContentParameter, ValueTask> processFileActionAsync = null,
    	Dictionary<string, Object> templateInfo = null,
    	ICardFileSourceMapping externalMapping = null,
    	IValidationResultBuilder extraErrorValidation = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CreateFromTemplateAsync ( 
    	request As CardStoreRequest,
    	Optional header As CardHeader = Nothing,
    	Optional readNextFileFuncAsync As Func(Of Long, CancellationToken, ValueTask(Of SubStream)) = Nothing,
    	Optional processFileActionAsync As Func(Of CardFileContentParameter, ValueTask) = Nothing,
    	Optional templateInfo As Dictionary(Of String, Object) = Nothing,
    	Optional externalMapping As ICardFileSourceMapping = Nothing,
    	Optional extraErrorValidation As IValidationResultBuilder = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Request As CardNewRequest, Response As CardNewResponse))
C++ __Копировать
     public:
    virtual Task<ValueTuple<CardNewRequest^, CardNewResponse^>>^ CreateFromTemplateAsync(
    	CardStoreRequest^ request, 
    	CardHeader^ header = nullptr, 
    	Func<long long, CancellationToken, ValueTask<SubStream^>>^ readNextFileFuncAsync = nullptr, 
    	Func<CardFileContentParameter^, ValueTask>^ processFileActionAsync = nullptr, 
    	Dictionary<String^, Object^>^ templateInfo = nullptr, 
    	ICardFileSourceMapping^ externalMapping = nullptr, 
    	IValidationResultBuilder^ extraErrorValidation = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CreateFromTemplateAsync : 
            request : CardStoreRequest * 
            ?header : CardHeader * 
            ?readNextFileFuncAsync : Func<int64, CancellationToken, ValueTask<SubStream>> * 
            ?processFileActionAsync : Func<CardFileContentParameter, ValueTask> * 
            ?templateInfo : Dictionary<string, Object> * 
            ?externalMapping : ICardFileSourceMapping * 
            ?extraErrorValidation : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _header = defaultArg header null
            let _readNextFileFuncAsync = defaultArg readNextFileFuncAsync null
            let _processFileActionAsync = defaultArg processFileActionAsync null
            let _templateInfo = defaultArg templateInfo null
            let _externalMapping = defaultArg externalMapping null
            let _extraErrorValidation = defaultArg extraErrorValidation null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardNewRequest, CardNewResponse>> 
    override CreateFromTemplateAsync : 
            request : CardStoreRequest * 
            ?header : CardHeader * 
            ?readNextFileFuncAsync : Func<int64, CancellationToken, ValueTask<SubStream>> * 
            ?processFileActionAsync : Func<CardFileContentParameter, ValueTask> * 
            ?templateInfo : Dictionary<string, Object> * 
            ?externalMapping : ICardFileSourceMapping * 
            ?extraErrorValidation : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _header = defaultArg header null
            let _readNextFileFuncAsync = defaultArg readNextFileFuncAsync null
            let _processFileActionAsync = defaultArg processFileActionAsync null
            let _templateInfo = defaultArg templateInfo null
            let _externalMapping = defaultArg externalMapping null
            let _extraErrorValidation = defaultArg extraErrorValidation null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardNewRequest, CardNewResponse>> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
     Запрос на сохранение карточки шаблона, в котором содержится как исходная (экспортированная) карточка, из которой создаётся новая карточка, так и дополнительная информация в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm). 
header [CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm) (Optional)
     Заголовок, содержащий информацию о файлах шаблона, или null, если считается, что файлов в шаблоне нет. 
readNextFileFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SubStream](T_Tessa_Platform_IO_SubStream.htm)>>
(Optional)
     Функция, выполняющая чтение контента очередного файла заданного размера, или null, если считается, что файлов в шаблоне нет. Порядок файлов определяется в заголовке header. 
processFileActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CardFileContentParameter](T_Tessa_Cards_CardFileContentParameter.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Метод, выполняющий обработку для каждого из файлов, приложенных к карточке, или null, если считается, что файлов в шаблоне нет. 
templateInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
Дополнительная информация, помещаемая в запрос на создание карточки по
шаблону, или null, если дополнительная информация отсутствует.
Если при экспорте карточки была задана дополнительная информация, то она
совмещается с заданной в этом параметре, причём при совпадении ключей
информация в параметре переопределяет информацию, заданную при экспорте.
externalMapping
[ICardFileSourceMapping](T_Tessa_Cards_ICardFileSourceMapping.htm) (Optional)
    Информация по отображению источников внешнего контента в файлах карточки. Указывает на соответствие внешнего источника для каждого найденного в объекте файла, что переопределяет загрузку контента такого файла на клиенте.
extraErrorValidation
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
    Дополнительная валидация ошибок или null.
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
[ICardManager.CreateFromTemplateAsync(CardStoreRequest, CardHeader,
Func<Int64, CancellationToken, ValueTask<SubStream>>,
Func<CardFileContentParameter, ValueTask>, Dictionary<String, Object>,
ICardFileSourceMapping, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ICardManager_CreateFromTemplateAsync.htm)  
##  __См. также
#### Ссылки
[CardManager - ](T_Tessa_Cards_CardManager.htm)
[CreateFromTemplateAsync -
перегрузка](Overload_Tessa_Cards_CardManager_CreateFromTemplateAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
