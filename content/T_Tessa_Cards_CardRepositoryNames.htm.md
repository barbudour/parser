# CardRepositoryNames - класс
Имена репозиториев [ICardRepository](T_Tessa_Cards_ICardRepository.htm),
которые регистрируются в Unity.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardRepositoryNames
VB __Копировать
     Public NotInheritable Class CardRepositoryNames
C++ __Копировать
     public ref class CardRepositoryNames abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardRepositoryNames = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardRepositoryNames
##  __Поля
[Default](F_Tessa_Cards_CardRepositoryNames_Default.htm)|  Репозиторий с
конфигурацией по умолчанию, т.е. без расширений. Может использоваться при
резолве репозиториев карточек, стратегии
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
и компонентов карточки на клиенте и на сервере.  
---|---  
[DefaultWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_DefaultWithoutTransaction.htm)|
Репозиторий с конфигурацией по умолчанию, т.е. без расширений, не выполняющий
действия в транзакции. Может использоваться при резолве репозиториев карточек,
стратегии
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
и компонентов карточки только на сервере.  
[Extended](F_Tessa_Cards_CardRepositoryNames_Extended.htm)|  Репозиторий с
расширениями (платформенными и пользовательскими). Может использоваться при
резолве репозиториев карточек, стратегии
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
и компонентов карточки на клиенте и на сервере.  
[ExtendedWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_ExtendedWithoutTransaction.htm)|
Репозиторий с расширениями (платформенными и пользовательскими), не
выполняющий действия в транзакции. Может использоваться при резолве
репозиториев карточек, стратегии
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
и компонентов карточки только на сервере.  
[Platform](F_Tessa_Cards_CardRepositoryNames_Platform.htm)|  Репозиторий с
платформенными расширениями. Пользовательские расширения не используются
(клиентские на стороне клиента и серверные на стороне сервера). Может
использоваться при резолве репозиториев карточек, стратегии
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm),
компонентов карточки и контейнера расширений
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm) на клиенте и
на сервере.  
[PlatformWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_PlatformWithoutTransaction.htm)|
Репозиторий с платформенными расширениями, не выполняющий действия в
транзакции. Пользовательские расширения не используются (клиентские на стороне
клиента и серверные на стороне сервера). Может использоваться при резолве
репозиториев карточек, стратегии
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
и компонентов карточки только на сервере.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
