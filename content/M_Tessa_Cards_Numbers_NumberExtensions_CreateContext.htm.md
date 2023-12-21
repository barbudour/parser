# NumberExtensions.CreateContext - метод
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданным номером
и другими параметрами. После создания контекста номер нельзя изменить.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static INumberContext CreateContext(
    	this INumberComposer composer,
    	Card card,
    	CardType cardType,
    	INumberObject number,
    	Dictionary<string, Object> contextInfo = null,
    	Object externalContext = null,
    	NumberTransactionMode transactionMode = NumberTransactionMode.SeparateTransaction
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CreateContext ( 
    	composer As INumberComposer,
    	card As Card,
    	cardType As CardType,
    	number As INumberObject,
    	Optional contextInfo As Dictionary(Of String, Object) = Nothing,
    	Optional externalContext As Object = Nothing,
    	Optional transactionMode As NumberTransactionMode = NumberTransactionMode.SeparateTransaction
    ) As INumberContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    static INumberContext^ CreateContext(
    	INumberComposer^ composer, 
    	Card^ card, 
    	CardType^ cardType, 
    	INumberObject^ number, 
    	Dictionary<String^, Object^>^ contextInfo = nullptr, 
    	Object^ externalContext = nullptr, 
    	NumberTransactionMode transactionMode = NumberTransactionMode::SeparateTransaction
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CreateContext : 
            composer : INumberComposer * 
            card : Card * 
            cardType : CardType * 
            number : INumberObject * 
            ?contextInfo : Dictionary<string, Object> * 
            ?externalContext : Object * 
            ?transactionMode : NumberTransactionMode 
    (* Defaults:
            let _contextInfo = defaultArg contextInfo null
            let _externalContext = defaultArg externalContext null
            let _transactionMode = defaultArg transactionMode NumberTransactionMode.SeparateTransaction
    *)
    -> INumberContext 
#### Параметры
composer [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)
     Объект, обрабатывающий логику выделения и изменения номеров карточек. Не может быть равен null. 
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой производится работа с номером. Не может быть равна null. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки card, для которой будет производиться работа с номером. Не может быть равен null. 
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
     Номер, который задаётся для создаваемого объекта. Не может быть равен null. 
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
#### Возвращаемое значение
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)  
Созданный контекст операции.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm). При
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
