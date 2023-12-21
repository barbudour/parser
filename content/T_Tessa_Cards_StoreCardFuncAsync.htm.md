# StoreCardFuncAsync - делегат
Функция, которая выполняет асинхронное сохранение карточки с файлами по
заданным параметрам. При этом сохраняется контент добавленных или изменённых
файлов и опционально выводится информация по прогрессу сохранения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate CardStoreOperationToken StoreCardFuncAsync(
    	CardStoreRequest request,
    	IFileContainer fileContainer,
    	Func<double, CancellationToken, ValueTask> updateProgressAsync = null,
    	int updateProgressMillisecondInterval = -1,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function StoreCardFuncAsync ( 
    	request As CardStoreRequest,
    	fileContainer As IFileContainer,
    	Optional updateProgressAsync As Func(Of Double, CancellationToken, ValueTask) = Nothing,
    	Optional updateProgressMillisecondInterval As Integer = -1,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As CardStoreOperationToken
C++ __Копировать
     public delegate CardStoreOperationToken^ StoreCardFuncAsync(
    	CardStoreRequest^ request, 
    	IFileContainer^ fileContainer, 
    	Func<double, CancellationToken, ValueTask>^ updateProgressAsync = nullptr, 
    	int updateProgressMillisecondInterval = -1, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type StoreCardFuncAsync = 
        delegate of 
            request : CardStoreRequest * 
            fileContainer : IFileContainer * 
            ?updateProgressAsync : Func<float, CancellationToken, ValueTask> * 
            ?updateProgressMillisecondInterval : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _updateProgressAsync = defaultArg updateProgressAsync null
            let _updateProgressMillisecondInterval = defaultArg updateProgressMillisecondInterval -1
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardStoreOperationToken
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
fileContainer [IFileContainer](T_Tessa_Files_IFileContainer.htm)
    Контейнер с файлами карточки.
updateProgressAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Метод, получающий прогресс сохранения файлов как число от 0 до 1. Метод не вызывается, если карточка сохраняется без файлов. Укажите null, чтобы не обновлять прогресс. 
updateProgressMillisecondInterval
[Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Интервал в миллисекундах между обновлениями прогресса по сохранению файлов. Укажите [Infinite](https://learn.microsoft.com/dotnet/api/system.threading.timeout.infinite), чтобы не обновлять прогресс. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[CardStoreOperationToken](T_Tessa_Cards_CardStoreOperationToken.htm)  
Объект, предоставляющий доступ к асинхронной операции по сохранению карточки с
файлами и к её результату.
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
