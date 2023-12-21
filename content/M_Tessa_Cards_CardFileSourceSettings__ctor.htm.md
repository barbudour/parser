# CardFileSourceSettings(IEnumerable<ICardFileSource>, ICardFileSource,
ICardFileSourceOverrideProvider, IUnityDisposableContainer) - конструктор
Создаёт экземпляр класса с указанием его зависимостей для получения значений
вручную.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileSourceSettings(
    	IEnumerable<ICardFileSource> sources,
    	ICardFileSource defaultSource = null,
    	[OptionalDependencyAttribute] ICardFileSourceOverrideProvider overrideProvider = null,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	sources As IEnumerable(Of ICardFileSource),
    	Optional defaultSource As ICardFileSource = Nothing,
    	<OptionalDependencyAttribute> Optional overrideProvider As ICardFileSourceOverrideProvider = Nothing,
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    CardFileSourceSettings(
    	IEnumerable<ICardFileSource^>^ sources, 
    	ICardFileSource^ defaultSource = nullptr, 
    	[OptionalDependencyAttribute] ICardFileSourceOverrideProvider^ overrideProvider = nullptr, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            sources : IEnumerable<ICardFileSource> * 
            ?defaultSource : ICardFileSource * 
            [<OptionalDependencyAttribute>] ?overrideProvider : ICardFileSourceOverrideProvider * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _defaultSource = defaultArg defaultSource null
            let _overrideProvider = defaultArg overrideProvider null
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> CardFileSourceSettings
#### Параметры
sources
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)>
    Список настроек по местоположениям файлов.
defaultSource [ICardFileSource](T_Tessa_Cards_ICardFileSource.htm) (Optional)
     Местоположение по умолчанию или null, если в качестве местоположения по умолчанию задаётся первый элемент перечисления sources или null, если перечисление не возвращает значений. 
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
