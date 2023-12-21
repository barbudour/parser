# CardSchemeInfoProvider(ICardMetadata, IUnityDisposableContainer) -
конструктор
Создаёт экземпляр класса с указанием его зависимостей для регистрации в Unity.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [InjectionConstructorAttribute]
    public CardSchemeInfoProvider(
    	ICardMetadata cardMetadata,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
    <InjectionConstructorAttribute>
    Public Sub New ( 
    	cardMetadata As ICardMetadata,
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    [InjectionConstructorAttribute]
    CardSchemeInfoProvider(
    	ICardMetadata^ cardMetadata, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     [<InjectionConstructorAttribute>]
    new : 
            cardMetadata : ICardMetadata * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> CardSchemeInfoProvider
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
    Контейнер, используемый для регистрации задачи на освобождение текущего объекта.
##  __См. также
#### Ссылки
[CardSchemeInfoProvider - ](T_Tessa_Cards_CardSchemeInfoProvider.htm)
[CardSchemeInfoProvider -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProvider__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
