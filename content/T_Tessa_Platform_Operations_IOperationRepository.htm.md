# IOperationRepository - интерфейс
Репозиторий, управляющий операциями.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IOperationRepository
VB __Копировать
     Public Interface IOperationRepository
C++ __Копировать
     public interface class IOperationRepository
F# __Копировать
     type IOperationRepository = interface end
##  __Методы
[CompleteAsync](M_Tessa_Platform_Operations_IOperationRepository_CompleteAsync.htm)|
Завершает операцию заданного типа, т.е. переводит её в состояние
[Tessa.Platform.Operations.OperationState.Completed].  
---|---  
[CreateAsync](M_Tessa_Platform_Operations_IOperationRepository_CreateAsync.htm)|
Создаёт операцию с заданными параметрами.  
[DeleteAsync](M_Tessa_Platform_Operations_IOperationRepository_DeleteAsync.htm)|
Удаляет операцию с заданным идентификатором. Если операция не существовала, то
не выдаётся сообщений об ошибках.  
[DeleteOlderThanAsync](M_Tessa_Platform_Operations_IOperationRepository_DeleteOlderThanAsync.htm)|
Выполняет удаление записей, которые были созданы раньше заданных даты и
времени.  
[GetAllAsync(Boolean,
CancellationToken)](M_Tessa_Platform_Operations_IOperationRepository_GetAllAsync.htm)|
Возвращает информацию по всем операциям. При запросе с клиента метод доступен
только администраторам.  
[GetAllAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Platform_Operations_IOperationRepository_GetAllAsync_1.htm)|
Возвращает информацию по всем операциям заданного типа. При запросе с клиента
метод доступен только администраторам.  
[GetStateAndProgressAsync](M_Tessa_Platform_Operations_IOperationRepository_GetStateAndProgressAsync.htm)|
Возвращает состояние и прогресс операции в процентах или null, если операция
не найдена.  
[GetStateAsync](M_Tessa_Platform_Operations_IOperationRepository_GetStateAsync.htm)|
Возвращает состояние операции с заданным идентификатором или null, если
операция не существует.  
[IsAliveAsync](M_Tessa_Platform_Operations_IOperationRepository_IsAliveAsync.htm)|
Возвращает признак того, что операция с заданным идентификатором существует.  
[ReportProgressAsync](M_Tessa_Platform_Operations_IOperationRepository_ReportProgressAsync.htm)|
Сообщает о проценте готовности заданной операции, если операция находится в
состоянии [Tessa.Platform.Operations.OperationState.InProgress]? и возвращает
признак того, что изменение процента готовности удалось.  
[StartAsync](M_Tessa_Platform_Operations_IOperationRepository_StartAsync.htm)|
Запускает операцию с заданным идентификатором. Операция должна быть создана и
находиться в состоянии [Tessa.Platform.Operations.OperationState.Created].  
[StartFirstAsync](M_Tessa_Platform_Operations_IOperationRepository_StartFirstAsync.htm)|
Запускает из созданных операций заданного типа и возвращает идентификатор
запущенной операции или null, если подходящая операция отсутствует.  
[TryGetAsync](M_Tessa_Platform_Operations_IOperationRepository_TryGetAsync.htm)|
Возвращает информацию по операции с заданным идентификатором или null, если
операция отсутствует.  
[TryGetOperationIDByRequestHashAsync](M_Tessa_Platform_Operations_IOperationRepository_TryGetOperationIDByRequestHashAsync.htm)|
Возвращает идентификатор первой попавшейся операции по заданным идентификатору
типа и хешу от запроса или null, если операция не найдена.  
## __Методы расширения
[DeleteOperationSafeAsync](M_Tessa_Extensions_Platform_Server_AdSync_AdHelper_DeleteOperationSafeAsync.htm)|
Безопасное удаление операции  
(Определяется
[AdHelper](T_Tessa_Extensions_Platform_Server_AdSync_AdHelper.htm))  
---|---  
[ExecuteInLockAsync](M_Tessa_Platform_Operations_OperationsExtensions_ExecuteInLockAsync.htm)|
Асинхронно выполняет действие actionFunc внутри эксклюзивной блокировки.
Никакое другое вычисление не сможет быть выполнено, пока выполняется действие.
При этом создаётся операция c ID lockOperationTypeID с указанным описанием
operationDescription. Возвращает признак того, что блокировка была взята и
действие было выполнено. Значение false возвращается, если блокировку взять не
удалось из-за таймаута при ожидании блокировки. Вторым параметром возвращается
идентификатор операции. При взятии блокировки все операции не обязательно
выполняются в одном и том же соединении с базой данных. Использование
нескольких соединений может быть полезно для больших таймаутов, чтобы не
удерживать одно и то же соединение несколько минут. Чтобы гарантировать
выполнение на одном и том же соединении с БД, вызовите метод внутри блока
await using(dbScope.Create()) { ... }.  
(Определяется
[OperationsExtensions](T_Tessa_Platform_Operations_OperationsExtensions.htm))  
[ExecuteInRolesLockAsync](M_Tessa_Roles_RolesExtensions_ExecuteInRolesLockAsync.htm)|
Асинхронно выполняет действие actionFunc внутри эксклюзивной блокировки на
вычисление состава ролей или замещений. Никакое другое вычисление не сможет
быть выполнено, пока выполняется действие. При этом создаётся операция
[LockOperationID](F_Tessa_Roles_RoleHelper_LockOperationID.htm) с указанным
описанием operationDescription. Возвращает признак того, что блокировка была
взята и действие было выполнено. Значение false возвращается, если блокировку
взять не удалось из-за таймаута при ожидании блокировки. При взятии блокировки
все операции не обязательно выполняются в одном и том же соединении с базой
данных. Использование нескольких соединений может быть полезно для больших
таймаутов, чтобы не удерживать одно и то же соединение несколько минут. Чтобы
гарантировать выполнение на одном и том же соединении с БД, вызовите метод
внутри блока using(dbScope.Create()) { ... }.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
