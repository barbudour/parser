# IUserSecurityLockingStrategy - интерфейс
Объект, управляющий блокировками на параметры безопасности и шифрования
сотрудника.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserSecurityLockingStrategy
VB __Копировать
     Public Interface IUserSecurityLockingStrategy
C++ __Копировать
     public interface class IUserSecurityLockingStrategy
F# __Копировать
     type IUserSecurityLockingStrategy = interface end
##  __Методы
[ExecuteInLockAsync](M_Tessa_Platform_Runtime_IUserSecurityLockingStrategy_ExecuteInLockAsync.htm)|
Выполняет заданное действие в блокировке, связанной с настройкам безопасности
сотрудника с заданным идентификатором. Если в течение короткого времени
блокировку не удалось получить, т.к. параллельно выполняется другая задача в
блокировке, или если сотрудник не найден по заданному идентификатору, то метод
выбрасывает исключение [System.InvalidOperationException]. Блокировка
снимается даже в том случае, если заданный метод выбросил исключение, после
чего исключение выбрасывается наружу.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
