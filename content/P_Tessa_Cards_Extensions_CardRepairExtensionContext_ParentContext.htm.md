# CardRepairExtensionContext.ParentContext - свойство
Контекст по исправлению родительской карточки или null, если текущая
исправляемая карточка не связана с родительской карточкой, т.е. не является
сателлитом.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardRepairExtensionContext ParentContext { get; }
VB __Копировать
     Public ReadOnly Property ParentContext As ICardRepairExtensionContext
    	Get
C++ __Копировать
     public:
    virtual property ICardRepairExtensionContext^ ParentContext {
    	ICardRepairExtensionContext^ get () sealed;
    }
F# __Копировать
     abstract ParentContext : ICardRepairExtensionContext with get
    override ParentContext : ICardRepairExtensionContext with get
#### Значение свойства
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
#### Реализации
[ICardRepairExtensionContext.ParentContext](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_ParentContext.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[CardRepairExtensionContext -
](T_Tessa_Cards_Extensions_CardRepairExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
