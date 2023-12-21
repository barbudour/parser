# NumberExtensions.CreateInitializedContextAsync(INumberDirector,
INumberComposer, Card, CardType, Dictionary<String, Object>, Object,
NumberTransactionMode, NumberEventType, CancellationToken) - метод
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, принимая тип номера равным
[Custom](F_Tessa_Cards_Numbers_NumberTypes_Custom.htm), а затем инициализирует
контекст с указанием типа события eventType.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<INumberContext> CreateInitializedContextAsync(
    	this INumberDirector director,
    	INumberComposer composer,
    	Card card,
    	CardType cardType,
    	Dictionary<string, Object> contextInfo = null,
    	Object externalContext = null,
    	NumberTransactionMode transactionMode = NumberTransactionMode.SeparateTransaction,
    	NumberEventType eventType = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CreateInitializedContextAsync ( 
    	director As INumberDirector,
    	composer As INumberComposer,
    	card As Card,
    	cardType As CardType,
    	Optional contextInfo As Dictionary(Of String, Object) = Nothing,
    	Optional externalContext As Object = Nothing,
    	Optional transactionMode As NumberTransactionMode = NumberTransactionMode.SeparateTransaction,
    	Optional eventType As NumberEventType = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberContext)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<INumberContext^> CreateInitializedContextAsync(
    	INumberDirector^ director, 
    	INumberComposer^ composer, 
    	Card^ card, 
    	CardType^ cardType, 
    	Dictionary<String^, Object^>^ contextInfo = nullptr, 
    	Object^ externalContext = nullptr, 
    	NumberTransactionMode transactionMode = NumberTransactionMode::SeparateTransaction, 
    	NumberEventType^ eventType = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CreateInitializedContextAsync : 
            director : INumberDirector * 
            composer : INumberComposer * 
            card : Card * 
            cardType : CardType * 
            ?contextInfo : Dictionary<string, Object> * 
            ?externalContext : Object * 
            ?transactionMode : NumberTransactionMode * 
            ?eventType : NumberEventType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _contextInfo = defaultArg contextInfo null
            let _externalContext = defaultArg externalContext null
            let _transactionMode = defaultArg transactionMode NumberTransactionMode.SeparateTransaction
            let _eventType = defaultArg eventType null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberContext> 
#### Параметры
director [INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm)
     Объект, управляющий взаимодействием с номерами карточек. Не может быть равен null. 
composer [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)
     Объект, обрабатывающий логику выделения и изменения номеров карточек. Не может быть равен null. 
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой производится работа с номером. Не может быть равна null. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки card, для которой будет производиться работа с номером. Не может быть равен null. 
contextInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Доступная только для чтения информация из внешнего контекста, используемая при обработке события, происходящего с номером, или null, если информация не доступна. Обычно в расширениях UI это ICardModel.Info, а в других расширениях, связанных с карточками, это Info запроса. 
externalContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
     Объект внешнего контекста. При генерации номера в расширениях это контекст расширений. 
transactionMode
[NumberTransactionMode](T_Tessa_Cards_Numbers_NumberTransactionMode.htm)
(Optional)
    Способ выполнения запросов, связанных с номерами.
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
(Optional)
     Тип события или null, если используется тип события [CustomAction](F_Tessa_Cards_Numbers_NumberEventTypes_CustomAction.htm). 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)>  
Созданный контекст операции.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[CreateInitializedContextAsync -
перегрузка](Overload_Tessa_Cards_Numbers_NumberExtensions_CreateInitializedContextAsync.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
