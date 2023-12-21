# CardRequestExtensions.TryGetTypedResponseAsync<TResponse> \- метод
Возвращает строготипизированный ответ на запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой ответ на запрос не задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<TResponse> TryGetTypedResponseAsync<TResponse>(
    	this CardResponse cardResponse,
    	Func<Dictionary<string, Object>, CancellationToken, ValueTask<TResponse>> createResponseFuncAsync,
    	CancellationToken cancellationToken = default
    )
    where TResponse : class, IStorageObjectProvider
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTypedResponseAsync(Of TResponse As {Class, IStorageObjectProvider}) ( 
    	cardResponse As CardResponse,
    	createResponseFuncAsync As Func(Of Dictionary(Of String, Object), CancellationToken, ValueTask(Of TResponse)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of TResponse)
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename TResponse>
    where TResponse : ref class, IStorageObjectProvider
    static ValueTask<TResponse> TryGetTypedResponseAsync(
    	CardResponse^ cardResponse, 
    	Func<Dictionary<String^, Object^>^, CancellationToken, ValueTask<TResponse>>^ createResponseFuncAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTypedResponseAsync : 
            cardResponse : CardResponse * 
            createResponseFuncAsync : Func<Dictionary<string, Object>, CancellationToken, ValueTask<'TResponse>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'TResponse>  when 'TResponse : not struct and IStorageObjectProvider
#### Параметры
cardResponse [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Универсальный ответ на запрос к API карточек.
createResponseFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>,
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<TResponse>>
     Создаёт объект запроса по заданному хранилищу Dictionary<string, object>. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
TResponse
     Ссылочный тип строготипизированного запроса. Должен реализовывать интерфейс [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm). 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<TResponse>  
Строготипизированный ответ на запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой ответ на запрос не задан.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponse](T_Tessa_Cards_CardResponse.htm). При вызове метода
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
