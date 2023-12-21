# NumberDependencies - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberDependencies(
    	Func<IPlaceholderManager> getPlaceholderManagerFunc,
    	ICardRepository requestRepository,
    	ISession session,
    	IUnityContainer unityContainer,
    	[OptionalDependencyAttribute] IDbScope dbScope = null
    )
VB __Копировать
     Public Sub New ( 
    	getPlaceholderManagerFunc As Func(Of IPlaceholderManager),
    	requestRepository As ICardRepository,
    	session As ISession,
    	unityContainer As IUnityContainer,
    	<OptionalDependencyAttribute> Optional dbScope As IDbScope = Nothing
    )
C++ __Копировать
     public:
    NumberDependencies(
    	Func<IPlaceholderManager^>^ getPlaceholderManagerFunc, 
    	ICardRepository^ requestRepository, 
    	ISession^ session, 
    	IUnityContainer^ unityContainer, 
    	[OptionalDependencyAttribute] IDbScope^ dbScope = nullptr
    )
F# __Копировать
     new : 
            getPlaceholderManagerFunc : Func<IPlaceholderManager> * 
            requestRepository : ICardRepository * 
            session : ISession * 
            unityContainer : IUnityContainer * 
            [<OptionalDependencyAttribute>] ?dbScope : IDbScope 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
    *)
    -> NumberDependencies
#### Параметры
getPlaceholderManagerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IPlaceholderManager](T_Tessa_Platform_Placeholders_IPlaceholderManager.htm)>
     Функция, которая возвращает объект, управляющий операциями с плейсхолдерами. 
requestRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий, используемый для построения универсальных запросов к API номеров на сервере. 
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия текущего пользователя.
unityContainer IUnityContainer
    Контейнер Unity, который может использоваться для получения дополнительных зависимостей.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
     Объект, предоставляющий доступ к базе данных, или null, если выполнение происходит без доступа к базе данных, например, со стороны клиента. 
## __См. также
#### Ссылки
[NumberDependencies - ](T_Tessa_Cards_Numbers_NumberDependencies.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
