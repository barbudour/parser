# ICardManager.ReadExportedRequestAsync - метод
Выполняет чтение запроса на импорт карточки из потока, содержащего
экспортированную карточку.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreRequest> ReadExportedRequestAsync(
    	ISourceContentProvider sourceProvider,
    	IValidationResultBuilder validationResult,
    	CardFileFormat format = CardFileFormat.Binary,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ReadExportedRequestAsync ( 
    	sourceProvider As ISourceContentProvider,
    	validationResult As IValidationResultBuilder,
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreRequest)
C++ __Копировать
    Task<CardStoreRequest^>^ ReadExportedRequestAsync(
    	ISourceContentProvider^ sourceProvider, 
    	IValidationResultBuilder^ validationResult, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReadExportedRequestAsync : 
            sourceProvider : ISourceContentProvider * 
            validationResult : IValidationResultBuilder * 
            ?format : CardFileFormat * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _format = defaultArg format CardFileFormat.Binary
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreRequest> 
#### Параметры
sourceProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса, представляющего карточку. Например файл и т.п.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации.
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm) (Optional)
    Формат файла для экспортированной карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)>  
Запрос на импорт карточки, полученный из заданного потока.
##  __См. также
#### Ссылки
[ICardManager - ](T_Tessa_Cards_ICardManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
