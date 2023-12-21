# Tessa.Platform.Data - пространство имён
Вспомогательные классы, общие интерфейсы и классы API взаимодействия с СУБД.
##  __Классы
[ConditionalQueryBuilder](T_Tessa_Platform_Data_ConditionalQueryBuilder.htm)|  
---|---  
[DatabaseHelper](T_Tessa_Platform_Data_DatabaseHelper.htm)|  Вспомогательные
методы для создания и удаления баз данных.  
[DataConnectionWrapper](T_Tessa_Platform_Data_DataConnectionWrapper.htm)|  
[DataReaderStream](T_Tessa_Platform_Data_DataReaderStream.htm)|  Объект,
выполняющий потоковое чтение массива байт из объекта
[IDataReader](https://learn.microsoft.com/dotnet/api/system.data.idatareader).
При этом
[IDataReader](https://learn.microsoft.com/dotnet/api/system.data.idatareader)
должен быть открыт в режиме
[SequentialAccess](https://learn.microsoft.com/dotnet/api/system.data.commandbehavior).  
[DbManager](T_Tessa_Platform_Data_DbManager.htm)|  Объект, управляющий
взаимодействием с базой данных.  
[DbManagerFactory](T_Tessa_Platform_Data_DbManagerFactory.htm)|  
[DbManagerQueryExecutor](T_Tessa_Platform_Data_DbManagerQueryExecutor.htm)|
Позволяет выполнять SQL-команды, не возвращающие значение, посредством объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
[DbScope](T_Tessa_Platform_Data_DbScope.htm)|  Объект для взаимодействия с
базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
[DbScope.InnerScope](T_Tessa_Platform_Data_DbScope_InnerScope.htm)|  
[DbScope.OuterScope](T_Tessa_Platform_Data_DbScope_OuterScope.htm)|  
[DbScope.SpecificDbAndExeсutorScope](T_Tessa_Platform_Data_DbScope_SpecificDbAndExeсutorScope.htm)|  
[DbScope.SpecificScope](T_Tessa_Platform_Data_DbScope_SpecificScope.htm)|  
[DefaultBulkInsertExecutor](T_Tessa_Platform_Data_DefaultBulkInsertExecutor.htm)|
Реализация объекта для массовой вставки
[IBulkInsertExecutor](T_Tessa_Platform_Data_IBulkInsertExecutor.htm), который
используется по умолчанию для СУБД, не поддерживающих особый синтаксис по
массовой вставке. При этом одна и та же команда выполняется множество раз с
разными параметрами (обычно множество операций INSERT).  
[DeferredQueryExecutor](T_Tessa_Platform_Data_DeferredQueryExecutor.htm)|
Позволяет отложенно выполнять SQL-команды, не возвращающие значение, с
параметрами, а также отложенно создавать параметры. Все отложенные команды
могут быть выполнены позднее посредством метода
[ExecuteAllAsync(IQueryExecutor,
CancellationToken)](M_Tessa_Platform_Data_DeferredQueryExecutorBase_ExecuteAllAsync.htm).  
[DeferredQueryExecutorBase](T_Tessa_Platform_Data_DeferredQueryExecutorBase.htm)|
Базовый класс для объектов, позволяющих отложенно выполнять SQL-команды, не
возвращающие значение, с параметрами, а также отложенно создавать параметры.
Все отложенные команды могут быть выполнены позднее посредством метода
[ExecuteAllAsync(IQueryExecutor,
CancellationToken)](M_Tessa_Platform_Data_DeferredQueryExecutorBase_ExecuteAllAsync.htm).  
[DeleteInstanceExecutor](T_Tessa_Platform_Data_DeleteInstanceExecutor.htm)|
Объект, осуществляющий удаление нескольких объектов из нескольких таблиц по
идентификатору ID.  
[Extensions](T_Tessa_Platform_Data_Extensions.htm)|  
[LogQueryExecutor](T_Tessa_Platform_Data_LogQueryExecutor.htm)|  Позволяет
логировать SQL-команды, не возвращающие значение, посредством метода
[LogQuery(String)](M_Tessa_Platform_Data_SqlHelper_LogQuery.htm).  
[NullObjectQueryExecutor](T_Tessa_Platform_Data_NullObjectQueryExecutor.htm)|
Не выполняет никаких действий, а в качестве параметра возвращает null. Может
использоваться вместо null-ссылки на
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm).  
[ParameterNameCreator](T_Tessa_Platform_Data_ParameterNameCreator.htm)|
Управляет созданием имён SQL-параметров.  
[PlatformDataExtensions](T_Tessa_Platform_Data_PlatformDataExtensions.htm)|
Методы-расширения для пространства имён Tessa.Platform.Data.  
[QueryBuilder](T_Tessa_Platform_Data_QueryBuilder.htm)|  
[QueryBuilderFactory](T_Tessa_Platform_Data_QueryBuilderFactory.htm)|  
[QueryExecutor](T_Tessa_Platform_Data_QueryExecutor.htm)|  Методы, позволяющие
возвращать объект [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
для заданных параметров.  
[SequentialAccessCommandProcessor](T_Tessa_Platform_Data_SequentialAccessCommandProcessor.htm)|
Custom command processor to enable
[SequentialAccess](https://learn.microsoft.com/dotnet/api/system.data.commandbehavior)
query behavior by default.  
[SingleRowParameterNameCreator](T_Tessa_Platform_Data_SingleRowParameterNameCreator.htm)|
Управляет созданием имён SQL-параметров для единственной строки данных. При
этом уникальность параметров не гарантируется.  
[SqlHelper](T_Tessa_Platform_Data_SqlHelper.htm)|  Хэлперы для работы с SQL-
выражениями.  
[SqlServerBulkInsertExecutor](T_Tessa_Platform_Data_SqlServerBulkInsertExecutor.htm)|  
[SqlServerErrorCodeProvider](T_Tessa_Platform_Data_SqlServerErrorCodeProvider.htm)|  
[TransactionFinishedContext](T_Tessa_Platform_Data_TransactionFinishedContext.htm)|
Контекст выполнения обработчиков
[Handlers](P_Tessa_Platform_Data_ITransactionScopeContext_Handlers.htm),
запускаемых после завершения транзакции.  
[TransactionParameter](T_Tessa_Platform_Data_TransactionParameter.htm)|
Реализация параметра делегата выполняемой транзакции для карточек.  
[TransactionQueryExecutor](T_Tessa_Platform_Data_TransactionQueryExecutor.htm)|
Позволяет отложенно выполнять SQL-команды, не возвращающие значение, с
параметрами, а также отложенно создавать параметры. Все отложенные команды
могут быть выполнены позднее посредством метода
[ExecuteAllAsync(IQueryExecutor,
CancellationToken)](M_Tessa_Platform_Data_DeferredQueryExecutorBase_ExecuteAllAsync.htm).
Блоки команд выполняются в отдельных транзакциях. Список исключений, возникших
в процессе последнего выполнения, представлен в свойстве
[CommandExceptions](P_Tessa_Platform_Data_TransactionQueryExecutor_CommandExceptions.htm).  
[TransactionScope](T_Tessa_Platform_Data_TransactionScope.htm)|  Объект для
управления областью выполнения транзакции.  
[TransactionScopeContext](T_Tessa_Platform_Data_TransactionScopeContext.htm)|
Контекст области выполнения транзакции.
Позволяет в процессе обработки транзакции добавить обработчики, которые будут
выполнены после коммита или отката транзакции.  
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm)|
Стратегия выполнения кода в SQL-транзакции. SQL-транзакция открывается только
в том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
[UnityBulkInsertExecutor](T_Tessa_Platform_Data_UnityBulkInsertExecutor.htm)|  
[UnityErrorCodeProvider](T_Tessa_Platform_Data_UnityErrorCodeProvider.htm)|  
[WithoutTransactionStrategy](T_Tessa_Platform_Data_WithoutTransactionStrategy.htm)|
Стратегия выполнения кода без SQL-транзакции.  
## __Структуры
[DeferredCommand](T_Tessa_Platform_Data_DeferredCommand.htm)|  Команда для
отложенного выполнения посредством
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm).  
---|---  
## __Интерфейсы
[IBulkInsertExecutor](T_Tessa_Platform_Data_IBulkInsertExecutor.htm)|  Объект,
выполняющий массовую вставку строк.  
---|---  
[IDbManagerFactory](T_Tessa_Platform_Data_IDbManagerFactory.htm)|  
[IDbmsErrorCodeProvider](T_Tessa_Platform_Data_IDbmsErrorCodeProvider.htm)|  
[IDbmsProvider](T_Tessa_Platform_Data_IDbmsProvider.htm)|  
[IDbScope](T_Tessa_Platform_Data_IDbScope.htm)|  Объект для взаимодействия с
базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
[IDbScopeInstance](T_Tessa_Platform_Data_IDbScopeInstance.htm)|  Экземпляр
области видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm),
который может быть получен из объекта
[IDbScope](T_Tessa_Platform_Data_IDbScope.htm).  
[IDeferredQueryExecutor](T_Tessa_Platform_Data_IDeferredQueryExecutor.htm)|
Позволяет отложенно выполнять SQL-команды, не возвращающие значение, с
параметрами, а также создавать параметры для отложенного выполнения.  
[IDeltaItem](T_Tessa_Platform_Data_IDeltaItem.htm)|  Интерфейс изменений  
[IParameterNameCreator](T_Tessa_Platform_Data_IParameterNameCreator.htm)|
Управляет созданием имён SQL-параметров.  
[IQueryBuilder](T_Tessa_Platform_Data_IQueryBuilder.htm)|  Объект, выполняющий
построение запроса.  
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)|
Объект для генерации текста запросов.  
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)|  Позволяет
выполнять SQL-команды, не возвращающие значение, с параметрами, а также
создавать параметры.  
[ITransactionFinishedContext](T_Tessa_Platform_Data_ITransactionFinishedContext.htm)|
Контекст выполнения обработчиков
[Handlers](P_Tessa_Platform_Data_ITransactionScopeContext_Handlers.htm),
запускаемых после завершения транзакции.  
[ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm)|
Параметр делегата выполняемой транзакции.  
[ITransactionScope](T_Tessa_Platform_Data_ITransactionScope.htm)|  Объект для
управления областью выполнения транзакции.  
[ITransactionScopeContext](T_Tessa_Platform_Data_ITransactionScopeContext.htm)|
Контекст области выполнения транзакции.
Позволяет в процессе обработки транзакции добавить обработчики, которые будут
выполнены после коммита или отката транзакции.  
[ITransactionStrategy](T_Tessa_Platform_Data_ITransactionStrategy.htm)|
Стратегия выполнения кода в SQL-транзакции. SQL-транзакция открывается только
в том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
## __Перечисления
[Dbms](T_Tessa_Platform_Data_Dbms.htm)|  
---|---  
[DbmsErrorCode](T_Tessa_Platform_Data_DbmsErrorCode.htm)|  
[DeferredCommandType](T_Tessa_Platform_Data_DeferredCommandType.htm)|  Тип
отложенной команды
[DeferredCommand](T_Tessa_Platform_Data_DeferredCommand.htm).  
[DeltaKind](T_Tessa_Platform_Data_DeltaKind.htm)|  Тип дельты  
[JoinType](T_Tessa_Platform_Data_JoinType.htm)|  
[QueryExecutorFlags](T_Tessa_Platform_Data_QueryExecutorFlags.htm)|  Флаги,
связанные с выполнением запросов в
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm) и
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
[SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm)|  Перечисление типов
данных в схеме TESSA. Используйте
[ToDbType(SchemeDbType)](M_Tessa_Platform_Data_PlatformDataExtensions_ToDbType.htm),
[ToValidDbType(SchemeDbType)](M_Tessa_Platform_Data_PlatformDataExtensions_ToValidDbType.htm)
и
[ToDataType(SchemeDbType)](M_Tessa_Platform_Data_PlatformDataExtensions_ToDataType.htm)
для преобразования к другим перечислениям, или метод
[ToSchemeDbType(DbType)](M_Tessa_Platform_Data_PlatformDataExtensions_ToSchemeDbType.htm)
для преобразования к этому типу.  
[SortOrder](T_Tessa_Platform_Data_SortOrder.htm)|
