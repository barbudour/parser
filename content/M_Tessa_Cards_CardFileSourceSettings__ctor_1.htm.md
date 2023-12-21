# CardFileSourceSettings(ICardFileSourceOverrideProvider,
IUnityDisposableContainer) - конструктор
Создаёт экземпляр класса без указания местоположений контентов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileSourceSettings(
    	[OptionalDependencyAttribute] ICardFileSourceOverrideProvider overrideProvider = null,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> Optional overrideProvider As ICardFileSourceOverrideProvider = Nothing,
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    CardFileSourceSettings(
    	[OptionalDependencyAttribute] ICardFileSourceOverrideProvider^ overrideProvider = nullptr, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] ?overrideProvider : ICardFileSourceOverrideProvider * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _overrideProvider = defaultArg overrideProvider null
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> CardFileSourceSettings
#### Параметры
overrideProvider
[ICardFileSourceOverrideProvider](T_Tessa_Cards_ICardFileSourceOverrideProvider.htm)
(Optional)
     Объект, предоставляющий доступ к настройкам, переопределяющих местоположение контента файлов, или null, если настройки не переопределяются. 
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
    Контейнер, используемый для регистрации задачи на освобождение текущего объекта.
##  __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[CardFileSourceSettings -
перегрузка](Overload_Tessa_Cards_CardFileSourceSettings__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
