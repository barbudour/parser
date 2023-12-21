# CardGetExtendedComponent - конструктор
Создаёт экземпляр класса с указанием компонента, выполняющего загрузку
карточки, и контейнера с используемыми расширениями.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetExtendedComponent(
    	ICardGetComponent component,
    	IExtensionContainer extensionContainer,
    	IDbScope dbScope = null
    )
VB __Копировать
     Public Sub New ( 
    	component As ICardGetComponent,
    	extensionContainer As IExtensionContainer,
    	Optional dbScope As IDbScope = Nothing
    )
C++ __Копировать
     public:
    CardGetExtendedComponent(
    	ICardGetComponent^ component, 
    	IExtensionContainer^ extensionContainer, 
    	IDbScope^ dbScope = nullptr
    )
F# __Копировать
     new : 
            component : ICardGetComponent * 
            extensionContainer : IExtensionContainer * 
            ?dbScope : IDbScope 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
    *)
    -> CardGetExtendedComponent
#### Параметры
component
[ICardGetComponent](T_Tessa_Cards_ComponentModel_ICardGetComponent.htm)
    Компонент, выполняющий загрузку карточки.
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер с используемыми расширениями.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
     Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и не равно null на сервере. 
## __См. также
#### Ссылки
[CardGetExtendedComponent -
](T_Tessa_Cards_ComponentModel_CardGetExtendedComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
