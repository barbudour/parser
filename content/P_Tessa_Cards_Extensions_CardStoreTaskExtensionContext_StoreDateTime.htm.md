# CardStoreTaskExtensionContext.StoreDateTime - свойство
Текущие дата и время сохранения для использования в транзакции или null, если
код не выполняется в транзакции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DateTime? StoreDateTime { get; }
VB __Копировать
     Public ReadOnly Property StoreDateTime As DateTime?
    	Get
C++ __Копировать
     public:
    virtual property Nullable<DateTime> StoreDateTime {
    	Nullable<DateTime> get () sealed;
    }
F# __Копировать
     abstract StoreDateTime : Nullable<DateTime> with get
    override StoreDateTime : Nullable<DateTime> with get
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
#### Реализации
[ICardStoreTaskExtensionContext.StoreDateTime](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_StoreDateTime.htm)  
##  __См. также
#### Ссылки
[CardStoreTaskExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
