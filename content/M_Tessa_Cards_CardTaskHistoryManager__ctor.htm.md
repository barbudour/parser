# CardTaskHistoryManager - конструктор
Создаёт экземпляр объекта с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTaskHistoryManager(
    	IPlaceholderManager placeholderManager,
    	ISession session,
    	IDbScope dbScope,
    	IUnityContainer unityContainer
    )
VB __Копировать
     Public Sub New ( 
    	placeholderManager As IPlaceholderManager,
    	session As ISession,
    	dbScope As IDbScope,
    	unityContainer As IUnityContainer
    )
C++ __Копировать
     public:
    CardTaskHistoryManager(
    	IPlaceholderManager^ placeholderManager, 
    	ISession^ session, 
    	IDbScope^ dbScope, 
    	IUnityContainer^ unityContainer
    )
F# __Копировать
     new : 
            placeholderManager : IPlaceholderManager * 
            session : ISession * 
            dbScope : IDbScope * 
            unityContainer : IUnityContainer -> CardTaskHistoryManager
#### Параметры
placeholderManager
[IPlaceholderManager](T_Tessa_Platform_Placeholders_IPlaceholderManager.htm)
    Объект, управляющий операциями с плейсхолдерами.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия текущего сотрудника.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для взаимодействия с базой данных.
unityContainer IUnityContainer
    Контейнер с зависимостями для плейсхолдеров.
##  __См. также
#### Ссылки
[CardTaskHistoryManager - ](T_Tessa_Cards_CardTaskHistoryManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
