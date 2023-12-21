# CardExtensionContextExtensions.CancelOpeningAsync(ICardGetExtensionContext,
Nullable<Guid>, CancellationToken) - метод
Отменяет открытие загружаемой карточки, при необходимости создаётся и
настраивается объект ответа на запрос.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task CancelOpeningAsync(
    	this ICardGetExtensionContext context,
    	Guid? cardTypeID = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CancelOpeningAsync ( 
    	context As ICardGetExtensionContext,
    	Optional cardTypeID As Guid? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ CancelOpeningAsync(
    	ICardGetExtensionContext^ context, 
    	Nullable<Guid> cardTypeID = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CancelOpeningAsync : 
            context : ICardGetExtensionContext * 
            ?cardTypeID : Nullable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardTypeID = defaultArg cardTypeID null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширений на открытие карточки.
cardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор типа карточки, который будет использован при создании ответа на запрос, если такое создание потребуется, или null, если используется автоматически определяемый идентификатор. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensionContextExtensions -
](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm)
[CancelOpeningAsync -
перегрузка](Overload_Tessa_Cards_Extensions_CardExtensionContextExtensions_CancelOpeningAsync.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
