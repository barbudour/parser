# CardExtendedRepairManager - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardExtendedRepairManager(
    	ICardRepairManager defaultManager,
    	ICardMetadata cardMetadata,
    	IExtensionContainer extensionContainer
    )
VB __Копировать
     Public Sub New ( 
    	defaultManager As ICardRepairManager,
    	cardMetadata As ICardMetadata,
    	extensionContainer As IExtensionContainer
    )
C++ __Копировать
     public:
    CardExtendedRepairManager(
    	ICardRepairManager^ defaultManager, 
    	ICardMetadata^ cardMetadata, 
    	IExtensionContainer^ extensionContainer
    )
F# __Копировать
     new : 
            defaultManager : ICardRepairManager * 
            cardMetadata : ICardMetadata * 
            extensionContainer : IExtensionContainer -> CardExtendedRepairManager
#### Параметры
defaultManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
    Объект, управляющий исправлением структуры карточки без расширений.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер расширений.
##  __См. также
#### Ссылки
[CardExtendedRepairManager - ](T_Tessa_Cards_CardExtendedRepairManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
