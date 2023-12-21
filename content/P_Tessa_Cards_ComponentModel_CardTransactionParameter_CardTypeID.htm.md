# CardTransactionParameter.CardTypeID - свойство
Идентификатор типа карточки, для которой выполняется транзакция, или null,
если идентификатор неизвестен. Обычно идентификатор установлен для транзакции
на чтение карточки и равен null во всех остальных случаях.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? CardTypeID { get; }
VB __Копировать
     Public ReadOnly Property CardTypeID As Guid?
    	Get
C++ __Копировать
     public:
    virtual property Nullable<Guid> CardTypeID {
    	Nullable<Guid> get () sealed;
    }
F# __Копировать
     abstract CardTypeID : Nullable<Guid> with get
    override CardTypeID : Nullable<Guid> with get
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
#### Реализации
[ICardTransactionParameter.CardTypeID](P_Tessa_Cards_ComponentModel_ICardTransactionParameter_CardTypeID.htm)  
##  __См. также
#### Ссылки
[CardTransactionParameter -
](T_Tessa_Cards_ComponentModel_CardTransactionParameter.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
