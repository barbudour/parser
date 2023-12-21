# ICardExternalSourceLogic.ReadCardAsync - метод
Чтение карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<(CardHeader Header, CardStoreRequest Request, Func<long, CancellationToken, ValueTask<SubStream>> ReadNextFileFuncAsync)> ReadCardAsync(
    	ISourceContentProvider sourceContentProvider,
    	CardFileFormat format,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ReadCardAsync ( 
    	sourceContentProvider As ISourceContentProvider,
    	format As CardFileFormat,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Header As CardHeader, Request As CardStoreRequest, ReadNextFileFuncAsync As Func(Of Long, CancellationToken, ValueTask(Of SubStream))))
C++ __Копировать
    Task<ValueTuple<CardHeader^, CardStoreRequest^, Func<long long, CancellationToken, ValueTask<SubStream^>>^>>^ ReadCardAsync(
    	ISourceContentProvider^ sourceContentProvider, 
    	CardFileFormat format, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReadCardAsync : 
            sourceContentProvider : ISourceContentProvider * 
            format : CardFileFormat * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardHeader, CardStoreRequest, Func<int64, CancellationToken, ValueTask<SubStream>>>> 
#### Параметры
sourceContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса - источинка, откуда производится чтение.
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm)
    Формат файла карточки.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm),
[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm),
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SubStream](T_Tessa_Platform_IO_SubStream.htm)>>>>  
Заголовок, содержаший иформацию о файлах. Объект запроса на сохранение
карточки. Функция, выполняющая чтение контента очередного файла заданного
размера, или null, если файлов нет.
## __См. также
#### Ссылки
[ICardExternalSourceLogic - ](T_Tessa_Cards_ICardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
