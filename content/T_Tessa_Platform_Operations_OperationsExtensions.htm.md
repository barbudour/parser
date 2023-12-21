# OperationsExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.Operations.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class OperationsExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class OperationsExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class OperationsExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type OperationsExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ OperationsExtensions
##  __Методы
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
---|---  
[Has](M_Tessa_Platform_Operations_OperationsExtensions_Has.htm)| Возвращает
признак того, что заданный флаг установлен.  
[HasAny](M_Tessa_Platform_Operations_OperationsExtensions_HasAny.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasNot](M_Tessa_Platform_Operations_OperationsExtensions_HasNot.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[RegisterOperationsForDatabase](M_Tessa_Platform_Operations_OperationsExtensions_RegisterOperationsForDatabase.htm)|
Выполняет регистрацию API операций на сервере для использования совместно с
регистрацией базы данных [IDbScope](T_Tessa_Platform_Data_IDbScope.htm),
например, в плагине Chronos без полноценной регистрации всех зависимостей.  
[RegisterOperationsOnClient](M_Tessa_Platform_Operations_OperationsExtensions_RegisterOperationsOnClient.htm)|
Выполняет регистрацию API операций на клиенте.  
[RegisterOperationsOnServer](M_Tessa_Platform_Operations_OperationsExtensions_RegisterOperationsOnServer.htm)|
Выполняет регистрацию API операций на сервере.  
## __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
