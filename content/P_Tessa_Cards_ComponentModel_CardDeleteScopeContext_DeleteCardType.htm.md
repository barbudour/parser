# CardDeleteScopeContext.DeleteCardType - свойство
Тип удаляемой карточки, используемый при удалении карточки внутри транзакции,
или null, если код не выполняется внутри транзакции по удалению карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardType DeleteCardType { get; }
VB __Копировать
     Public ReadOnly Property DeleteCardType As CardType
    	Get
C++ __Копировать
     public:
    virtual property CardType^ DeleteCardType {
    	CardType^ get () sealed;
    }
F# __Копировать
     abstract DeleteCardType : CardType with get
    override DeleteCardType : CardType with get
#### Значение свойства
[CardType](T_Tessa_Cards_CardType.htm)
#### Реализации
[ICardDeleteScopeContext.DeleteCardType](P_Tessa_Cards_ComponentModel_ICardDeleteScopeContext_DeleteCardType.htm)  
##  __См. также
#### Ссылки
[CardDeleteScopeContext -
](T_Tessa_Cards_ComponentModel_CardDeleteScopeContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
