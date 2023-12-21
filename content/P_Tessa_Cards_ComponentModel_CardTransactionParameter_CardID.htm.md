# CardTransactionParameter.CardID - свойство
Идентификатор карточки, для которой выполняется транзакция, или null, если
идентификатор карточки не проверяется.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? CardID { get; }
VB __Копировать
     Public ReadOnly Property CardID As Guid?
    	Get
C++ __Копировать
     public:
    virtual property Nullable<Guid> CardID {
    	Nullable<Guid> get () sealed;
    }
F# __Копировать
     abstract CardID : Nullable<Guid> with get
    override CardID : Nullable<Guid> with get
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
#### Реализации
[ICardTransactionParameter.CardID](P_Tessa_Cards_ComponentModel_ICardTransactionParameter_CardID.htm)  
##  __См. также
#### Ссылки
[CardTransactionParameter -
](T_Tessa_Cards_ComponentModel_CardTransactionParameter.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
