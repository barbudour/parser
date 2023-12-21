# Tessa.Views.MessageServices - пространство имён
API для сервисов обмены сообщениями для представлений и рабочих мест.
##  __Классы
[CommandDispatcher](T_Tessa_Views_MessageServices_CommandDispatcher.htm)|
Диспетчер команд  
---|---  
[CommandRouter](T_Tessa_Views_MessageServices_CommandRouter.htm)|  Роутер
команд, осуществляет поиск обработчиков команд и вызывает их исполнение  
[DelegatedCommandDispatcher](T_Tessa_Views_MessageServices_DelegatedCommandDispatcher.htm)|
Диспетчер команд делегирующий выполнение другим объектам к  
[DelegatedQueryDispatcher](T_Tessa_Views_MessageServices_DelegatedQueryDispatcher.htm)|
Диспетчер запросов с возможностью перенаправления запросов  
[MessagesRegistrationHelper](T_Tessa_Views_MessageServices_MessagesRegistrationHelper.htm)|
Вспомогательные методы регистрации команд и запросов  
[QueryDispatcher](T_Tessa_Views_MessageServices_QueryDispatcher.htm)|
Диспетчер запросов  
[QueryRouter](T_Tessa_Views_MessageServices_QueryRouter.htm)|  Сервис
выполнения запросов  
[RoutedCommand<TCommand,
TContext>](T_Tessa_Views_MessageServices_RoutedCommand_2.htm)|  Базовый класс
для перенаправляемых команд  
[RoutedCommand<TCommand, TContext1,
TContext2>](T_Tessa_Views_MessageServices_RoutedCommand_3.htm)|  Базовый класс
для перенаправляемых команд  
[RoutedQuery<TQuery, TResult,
TContext>](T_Tessa_Views_MessageServices_RoutedQuery_3.htm)|  Базовый класс
для создания перенаправляемых запросов  
[SingletonCommand<TCommand>](T_Tessa_Views_MessageServices_SingletonCommand_1.htm)|
Команда присутствующая в системе в единственном экземпляре  
[SingletonQuery<TQuery,
TQueryInstance>](T_Tessa_Views_MessageServices_SingletonQuery_2.htm)|  Запрос
представленный в единственном экземпляре  
## __Интерфейсы
[ICommandDispatcher](T_Tessa_Views_MessageServices_ICommandDispatcher.htm)|
Описание интерфейса диспетчера команд  
---|---  
[ICommandRouter](T_Tessa_Views_MessageServices_ICommandRouter.htm)|  Описание
интерфейса диспетчера команд  
[IQueryDispatcher](T_Tessa_Views_MessageServices_IQueryDispatcher.htm)|
Описание интерфейса диспетчера запросов  
[IQueryRouter](T_Tessa_Views_MessageServices_IQueryRouter.htm)|  Описание
интерфейса сервиса выполнения запросов  
[IRoutedCommand](T_Tessa_Views_MessageServices_IRoutedCommand.htm)|  Описание
интерфейса перенаправляемой команды  
[IRoutedCommandHandler](T_Tessa_Views_MessageServices_IRoutedCommandHandler.htm)|
Описание интерфейса обработчика команды  
[IRoutedCommandHandler<TCommand>](T_Tessa_Views_MessageServices_IRoutedCommandHandler_1.htm)|
Описание интерфейса типизированного обработчика команды  
[IRoutedQuery<TResult>](T_Tessa_Views_MessageServices_IRoutedQuery_1.htm)|
Описание интерфейса запроса  
[IRoutedQueryHandler](T_Tessa_Views_MessageServices_IRoutedQueryHandler.htm)|
Описание обработчика перенаправляемого запроса  
[IRoutedQueryHandler<TQuery,
TResult>](T_Tessa_Views_MessageServices_IRoutedQueryHandler_2.htm)|  Описание
интерфейса обработчика перенаправляемого запроса
