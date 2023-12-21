# CardStreamClientStoreExtendedComponent - конструктор
Создаёт экземпляр класса с указанием требуемого компонента и контейнера с
используемыми расширениями.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamClientStoreExtendedComponent(
    	ICardStreamClientStoreComponent cardStreamClientStoreComponent,
    	IExtensionContainer extensionContainer
    )
VB __Копировать
     Public Sub New ( 
    	cardStreamClientStoreComponent As ICardStreamClientStoreComponent,
    	extensionContainer As IExtensionContainer
    )
C++ __Копировать
     public:
    CardStreamClientStoreExtendedComponent(
    	ICardStreamClientStoreComponent^ cardStreamClientStoreComponent, 
    	IExtensionContainer^ extensionContainer
    )
F# __Копировать
     new : 
            cardStreamClientStoreComponent : ICardStreamClientStoreComponent * 
            extensionContainer : IExtensionContainer -> CardStreamClientStoreExtendedComponent
#### Параметры
cardStreamClientStoreComponent
[ICardStreamClientStoreComponent](T_Tessa_Cards_ComponentModel_ICardStreamClientStoreComponent.htm)
     Компонент, выполняющий потоковое сохранение карточки с контентом файлов без расширений. 
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер с используемыми расширениями.
##  __См. также
#### Ссылки
[CardStreamClientStoreExtendedComponent -
](T_Tessa_Cards_ComponentModel_CardStreamClientStoreExtendedComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
