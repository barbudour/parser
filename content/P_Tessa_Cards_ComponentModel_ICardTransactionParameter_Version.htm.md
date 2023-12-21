# ICardTransactionParameter.Version - свойство
Номер версии карточки, для которой должна быть открыта транзакция, или
[Tessa.Cards.ComponentModel.CardComponentHelper.DoNotCheckVersion], если
версия карточки не проверяется. Версия всегда не проверяется при чтении
карточки и может проверяться при изменении карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     int Version { get; }
VB __Копировать
     ReadOnly Property Version As Integer
    	Get
C++ __Копировать
    property int Version {
    	int get ();
    }
F# __Копировать
     abstract Version : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[ICardTransactionParameter -
](T_Tessa_Cards_ComponentModel_ICardTransactionParameter.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
