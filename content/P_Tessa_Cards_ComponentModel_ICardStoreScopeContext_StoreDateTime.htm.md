# ICardStoreScopeContext.StoreDateTime - свойство
Дата и время, используемые при сохранении карточки внутри транзакции, или
null, если код не выполняется внутри транзакции по сохранению карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    DateTime? StoreDateTime { get; }
VB __Копировать
     ReadOnly Property StoreDateTime As DateTime?
    	Get
C++ __Копировать
    property Nullable<DateTime> StoreDateTime {
    	Nullable<DateTime> get ();
    }
F# __Копировать
     abstract StoreDateTime : Nullable<DateTime> with get
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
##  __См. также
#### Ссылки
[ICardStoreScopeContext -
](T_Tessa_Cards_ComponentModel_ICardStoreScopeContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
