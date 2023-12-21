# CardRequestExtensions.TryGetTypedRequestAsync<TRequest> \- метод
Возвращает строготипизированный запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<TRequest> TryGetTypedRequestAsync<TRequest>(
    	this CardRequest cardRequest,
    	Func<Dictionary<string, Object>, CancellationToken, ValueTask<TRequest>> createRequestFuncAsync,
    	CancellationToken cancellationToken = default
    )
    where TRequest : class, IStorageObjectProvider
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTypedRequestAsync(Of TRequest As {Class, IStorageObjectProvider}) ( 
    	cardRequest As CardRequest,
    	createRequestFuncAsync As Func(Of Dictionary(Of String, Object), CancellationToken, ValueTask(Of TRequest)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of TRequest)
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename TRequest>
    where TRequest : ref class, IStorageObjectProvider
    static ValueTask<TRequest> TryGetTypedRequestAsync(
    	CardRequest^ cardRequest, 
    	Func<Dictionary<String^, Object^>^, CancellationToken, ValueTask<TRequest>>^ createRequestFuncAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTypedRequestAsync : 
            cardRequest : CardRequest * 
            createRequestFuncAsync : Func<Dictionary<string, Object>, CancellationToken, ValueTask<'TRequest>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'TRequest>  when 'TRequest : not struct and IStorageObjectProvider
#### Параметры
cardRequest [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Универсальный запрос к API карточек.
createRequestFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>,
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<TRequest>>
     Создаёт объект запроса по заданному хранилищу Dictionary<string, object>. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
TRequest
     Ссылочный тип строготипизированного запроса. Должен реализовывать интерфейс [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm). 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<TRequest>  
Строготипизированный запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardRequest](T_Tessa_Cards_CardRequest.htm). При вызове метода
для экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
