# NumberContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberContext(
    	Card card,
    	CardType cardType,
    	INumberObject numberObject = null,
    	Dictionary<string, Object> contextInfo = null,
    	Object externalContext = null,
    	NumberTransactionMode transactionMode = NumberTransactionMode.SeparateTransaction,
    	bool canChangeNumber = true,
    	bool canCancel = true,
    	bool canHandle = true
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	cardType As CardType,
    	Optional numberObject As INumberObject = Nothing,
    	Optional contextInfo As Dictionary(Of String, Object) = Nothing,
    	Optional externalContext As Object = Nothing,
    	Optional transactionMode As NumberTransactionMode = NumberTransactionMode.SeparateTransaction,
    	Optional canChangeNumber As Boolean = true,
    	Optional canCancel As Boolean = true,
    	Optional canHandle As Boolean = true
    )
C++ __Копировать
     public:
    NumberContext(
    	Card^ card, 
    	CardType^ cardType, 
    	INumberObject^ numberObject = nullptr, 
    	Dictionary<String^, Object^>^ contextInfo = nullptr, 
    	Object^ externalContext = nullptr, 
    	NumberTransactionMode transactionMode = NumberTransactionMode::SeparateTransaction, 
    	bool canChangeNumber = true, 
    	bool canCancel = true, 
    	bool canHandle = true
    )
F# __Копировать
     new : 
            card : Card * 
            cardType : CardType * 
            ?numberObject : INumberObject * 
            ?contextInfo : Dictionary<string, Object> * 
            ?externalContext : Object * 
            ?transactionMode : NumberTransactionMode * 
            ?canChangeNumber : bool * 
            ?canCancel : bool * 
            ?canHandle : bool 
    (* Defaults:
            let _numberObject = defaultArg numberObject null
            let _contextInfo = defaultArg contextInfo null
            let _externalContext = defaultArg externalContext null
            let _transactionMode = defaultArg transactionMode NumberTransactionMode.SeparateTransaction
            let _canChangeNumber = defaultArg canChangeNumber true
            let _canCancel = defaultArg canCancel true
            let _canHandle = defaultArg canHandle true
    *)
    -> NumberContext
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой производится работа с номером. Не может быть равна null. В карточке должны присутствовать системная информация и все секции, но могут отсутствовать файлы и задания. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки card, для которой будет производиться работа с номером. Не может быть равен null. 
numberObject [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
(Optional)
     Объект, определяющий свойства номера и средства его хранения. Может быть равен null, чтобы его можно было задать позднее. Рекомендуется задавать неизвестный номер только перед тем, как выполнить его резервирование для действия [CreatingCard](F_Tessa_Cards_Numbers_NumberEventTypes_CreatingCard.htm) или для аналогичных действий. Во всех остальных случаях это должен быть номер, участвующий в выполнении действия. 
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
canChangeNumber
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что номер [NumberObject](P_Tessa_Cards_Numbers_NumberContext_NumberObject.htm) можно изменить после создания объекта. 
canCancel [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что свойство [Cancel](P_Tessa_Cards_Numbers_NumberContext_Cancel.htm) можно задать.
canHandle [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что свойство [Handled](P_Tessa_Cards_Numbers_NumberContext_Handled.htm) можно задать.
##  __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
