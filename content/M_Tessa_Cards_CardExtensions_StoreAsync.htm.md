# CardExtensions.StoreAsync - метод
Сохраняет карточку из текущего контейнера и контент её файлов, при этом
позволяет асинхронно отслеживать её состояние. В процессе сохранения карточка
в контейнере и её файлы не изменяются, поэтому метод безопасно вызывать
повторно.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<CardStoreResponse> StoreAsync(
    	this ICardFileContainer container,
    	Func<ICardFileContainer, CardStoreRequest, CancellationToken, ValueTask> modifyRequestActionAsync = null,
    	Func<double, CancellationToken, ValueTask> updateProgressAsync = null,
    	int updateProgressMillisecondInterval = -1,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function StoreAsync ( 
    	container As ICardFileContainer,
    	Optional modifyRequestActionAsync As Func(Of ICardFileContainer, CardStoreRequest, CancellationToken, ValueTask) = Nothing,
    	Optional updateProgressAsync As Func(Of Double, CancellationToken, ValueTask) = Nothing,
    	Optional updateProgressMillisecondInterval As Integer = -1,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<CardStoreResponse^>^ StoreAsync(
    	ICardFileContainer^ container, 
    	Func<ICardFileContainer^, CardStoreRequest^, CancellationToken, ValueTask>^ modifyRequestActionAsync = nullptr, 
    	Func<double, CancellationToken, ValueTask>^ updateProgressAsync = nullptr, 
    	int updateProgressMillisecondInterval = -1, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member StoreAsync : 
            container : ICardFileContainer * 
            ?modifyRequestActionAsync : Func<ICardFileContainer, CardStoreRequest, CancellationToken, ValueTask> * 
            ?updateProgressAsync : Func<float, CancellationToken, ValueTask> * 
            ?updateProgressMillisecondInterval : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _modifyRequestActionAsync = defaultArg modifyRequestActionAsync null
            let _updateProgressAsync = defaultArg updateProgressAsync null
            let _updateProgressMillisecondInterval = defaultArg updateProgressMillisecondInterval -1
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
container [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)
    Контейнер, содержащий информацию по карточке и её файлам.
modifyRequestActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm),
[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Метод, выполняющий изменение запроса на сохранение карточки, или null, если выполняется запрос по умолчанию. В метод передаётся текущий объект контейнера и запрос с сохраняемой карточкой. В запросе доступна копия карточки, которая содержит только изменённые данные. 
updateProgressAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Метод, получающий прогресс сохранения файлов как число от 0 до 1. Метод не вызывается, если карточка сохраняется без файлов. 
updateProgressMillisecondInterval
[Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Интервал в миллисекундах между обновлениями прогресса по сохранению файлов. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Объект, предоставляющий доступ к асинхронной операции по сохранению карточки с
файлами и к её результату.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
